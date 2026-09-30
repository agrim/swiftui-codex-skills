#!/usr/bin/env python3
"""Plan or explicitly run one Apple build/test; preserve raw results, never publish.

This is not a sandbox. Xcode projects, package plugins, and build scripts can run
arbitrary code. Review the project before using --execute. Logs remain local and
may contain private data. No command is executed by the default plan action.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Callable

from skilllib import read_json, safe_path

ALLOWED = {"schema_version", "project", "workspace", "scheme", "configuration", "destination"}
CONTRACT_FIELDS = ("scheme", "configuration", "destination")


def _text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip() or value.startswith("-"):
        raise ValueError(f"{name} must be nonempty text, not an option")
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise ValueError(f"{name} contains a control character")
    return value


def validate_config(root: Path, config: dict[str, Any]) -> dict[str, Any]:
    """Require exactly one real project/workspace and explicit build identity."""
    if type(config.get("schema_version")) is not int or config["schema_version"] != 1:
        raise ValueError("unsupported build config schema_version")
    if set(config) - ALLOWED:
        raise ValueError("unknown build config keys: " + ", ".join(sorted(set(config) - ALLOWED)))
    selectors = [key for key in ("project", "workspace") if key in config]
    if len(selectors) != 1:
        raise ValueError("select exactly one project or workspace")
    kind = selectors[0]
    relative = _text(config[kind], kind)
    path = safe_path(root, relative)
    suffix = ".xcodeproj" if kind == "project" else ".xcworkspace"
    if not path.is_dir() or path.suffix != suffix:
        raise ValueError(f"{kind} must name an existing {suffix} directory")
    for key in CONTRACT_FIELDS:
        _text(config.get(key), key)
    return dict(config)


def plan(root: Path, config: dict[str, Any], action: str = "build") -> dict[str, Any]:
    if action not in {"build", "test"}:
        raise ValueError("only build and test are supported; no clean, install, sign, or publish action")
    root = root.resolve(strict=True)
    config = validate_config(root, config)
    kind = "project" if "project" in config else "workspace"
    command = ["xcodebuild", "-" + kind, config[kind]]
    for key in CONTRACT_FIELDS:
        command.extend(["-" + key, config[key]])
    command.extend(["-showBuildTimingSummary", action])
    return {"schema_version": 1, "status": "planned", "action": action,
            "config": config, "command": command, "cwd": str(root),
            "effects": "Execution may run project scripts, resolve packages, write build output, and use configured signing. No install, launch, reset, or publication is requested."}


def execute(root: Path, config: dict[str, Any], action: str, output: Path,
            *, authorized: bool, timeout: float = 1800,
            runner: Callable[..., Any] = subprocess.run) -> dict[str, Any]:
    """Run one reviewed plan and capture output. No deletion or retry is implicit."""
    if not authorized:
        raise ValueError("execution requires --execute")
    if type(timeout) not in {int, float} or not math.isfinite(timeout) or not 0 < timeout <= 86400:
        raise ValueError("timeout must be finite, positive, and no more than 86400 seconds")
    result = plan(root, config, action)
    # The user chooses a new output directory; no existing files are overwritten.
    output = Path(output)
    if output.name in {"", ".", ".."} or output.is_symlink():
        raise ValueError("output must be a new directory")
    parent = output.parent.resolve(strict=True)
    output = parent / output.name
    if output.exists():
        raise ValueError("output already exists; choose a new directory")
    output.mkdir(mode=0o700)
    command = result["command"][:-1] + ["-derivedDataPath", str(output / "DerivedData"),
               "-resultBundlePath", str(output / "result.xcresult"), action]
    result["command"] = command
    result["cache_policy"] = "New scoped DerivedData; external package/compiler caches are not cleared. This is not a fully cold-build guarantee."
    start = time.monotonic()
    exit_code: int | None = None
    status = "launch-failed"
    log_path = output / "build.log"
    try:
        with log_path.open("x", encoding="utf-8") as log:
            completed = runner(command, cwd=result["cwd"], stdout=log,
                               stderr=subprocess.STDOUT, timeout=timeout, check=False)
            exit_code = completed.returncode
            status = "completed" if exit_code == 0 else "failed"
    except subprocess.TimeoutExpired:
        status = "timed-out"
    except OSError as exc:
        result["launch_error"] = type(exc).__name__
    elapsed = time.monotonic() - start
    result.update(status=status, exit_code=exit_code, elapsed_seconds=elapsed,
                  raw_log="build.log", result_bundle="result.xcresult",
                  claim="Process result only. Inspect executed test counts and artifacts; this does not establish launch, rendering, hardware, or performance improvement.")
    # A launcher exception or timeout may leave diagnostic output. Preserve it.
    (output / "result.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


def summarize(data: dict[str, Any]) -> dict[str, Any]:
    """Summarize explicitly comparable elapsed samples, never cumulative task time.

Input contract: schema_version=1, contract is a nonempty object containing the
same context for the samples, and samples are {phase, seconds, exit_code}.
Warm-up samples should be recorded separately, not silently filtered here.
"""
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ValueError("unsupported benchmark schema_version")
    required = {"source", "toolchain", "destination", "configuration", "workload", "cache_policy"}
    contract = data.get("contract")
    if not isinstance(contract, dict) or not required.issubset(contract):
        raise ValueError("benchmark contract is missing identity/workload fields")
    for key in required:
        _text(contract[key], "contract." + key)
    samples = data.get("samples")
    if not isinstance(samples, list) or not samples:
        raise ValueError("samples must be a nonempty array")
    groups: dict[str, list[dict[str, Any]]] = {}
    for sample in samples:
        if not isinstance(sample, dict) or set(sample) != {"phase", "seconds", "exit_code"}:
            raise ValueError("each sample requires phase, seconds, and exit_code only")
        phase = _text(sample["phase"], "phase")
        seconds = sample["seconds"]
        if type(seconds) not in {int, float} or not math.isfinite(seconds) or seconds < 0:
            raise ValueError("seconds must be finite and nonnegative")
        if type(sample["exit_code"]) is not int:
            raise ValueError("exit_code must be an integer")
        groups.setdefault(phase, []).append(sample)
    summaries = []
    for phase, values in sorted(groups.items()):
        failed = sum(v["exit_code"] != 0 for v in values)
        successful = [v["seconds"] for v in values if v["exit_code"] == 0]
        summaries.append({"phase": phase, "sample_count": len(values), "failed_count": failed,
                          "successful_count": len(successful),
                          "median_seconds": statistics.median(successful) if successful else None,
                          "min_seconds": min(successful) if successful else None,
                          "max_seconds": max(successful) if successful else None,
                          "meets_reporting_minimum": failed == 0 and len(successful) >= 3})
    return {"schema_version": 1, "contract": contract, "phases": summaries,
            "limitations": "Descriptive elapsed-time statistics only. Three successful samples are a reporting minimum, not statistical significance or proof that environments are comparable. Failed samples remain visible; no speedup is inferred."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    for mode in ("plan", "run"):
        command = sub.add_parser(mode)
        command.add_argument("--root", type=Path, default=Path.cwd())
        command.add_argument("--config", type=Path, required=True)
        command.add_argument("--action", choices=("build", "test"), default="build")
        if mode == "run":
            command.add_argument("--execute", action="store_true")
            command.add_argument("--output", type=Path, required=True)
            command.add_argument("--timeout", type=float, default=1800)
    summary = sub.add_parser("summarize")
    summary.add_argument("artifact", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.mode == "summarize":
            result = summarize(read_json(args.artifact))
        elif args.mode == "plan":
            result = plan(args.root, read_json(args.config), args.action)
        else:
            result = execute(args.root, read_json(args.config), args.action, args.output,
                             authorized=args.execute, timeout=args.timeout)
        print(json.dumps(result, indent=2))
        if args.mode != "run" or result["status"] == "completed":
            return 0
        code = result["exit_code"]
        return code if type(code) is int and 1 <= code <= 125 else 1
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
