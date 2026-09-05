#!/usr/bin/env python3
"""Advisory Swift source triage, not a Swift parser or HIG compliance checker."""
from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from skilllib import iter_files
from validate_skills import LOCAL_PATH, SECRET

MAX_BYTES = 2 * 1024 * 1024
STRING_START = re.compile(r'(#+)?("""|")')
SEVERITIES = {"info": 0, "warning": 1, "error": 2}


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    rule: str
    severity: str
    message: str


@dataclass(frozen=True)
class Rule:
    id: str
    pattern: re.Pattern[str]
    severity: str
    message: str


RULES = (
    Rule("volatile-identity", re.compile(r"\.id\s*\(\s*UUID\s*\(\s*\)\s*\)"), "warning", "A fresh UUID can reset view identity; inspect the lifetime contract."),
    Rule("fixed-foreground", re.compile(r"\.(?:foregroundStyle|foregroundColor)\s*\(\s*\.(?:white|black)\b"), "info", "Review appearance and contrast in context; custom foregrounds are not inherently wrong."),
    Rule("tap-semantics", re.compile(r"\.onTapGesture\s*(?:\([^)]*\))?\s*\{"), "info", "Check whether this is an action needing Button semantics or a legitimate gesture."),
    Rule("detached-task", re.compile(r"\bTask\s*\.\s*detached\b"), "warning", "Review task lifetime, cancellation, isolation, and why unstructured work is needed."),
    Rule("unchecked-sendable", re.compile(r"@unchecked\s+Sendable\b"), "warning", "Require an explicit synchronization invariant; do not suppress isolation errors blindly."),
    Rule("forced-try", re.compile(r"\btry!"), "warning", "Verify the failure is impossible by contract or replace the crash path."),
)


def mask_noncode(text: str) -> str:
    """Blank Swift comments and strings while preserving offsets and line breaks.

Handles nested block comments and ordinary/raw/multiline strings. Interpolation
is deliberately masked too, so code within interpolation is a known blind spot.
Regex literals, inactive conditional branches, and semantic types are not parsed.
"""
    output = list(text)
    n, i = len(text), 0

    def blank(start: int, end: int) -> None:
        for position in range(start, end):
            if text[position] not in "\r\n":
                output[position] = " "

    while i < n:
        start = i
        if text.startswith("//", i):
            end = text.find("\n", i)
            i = n if end == -1 else end
            blank(start, i)
        elif text.startswith("/*", i):
            depth, i = 1, i + 2
            while i < n and depth:
                if text.startswith("/*", i):
                    depth, i = depth + 1, i + 2
                elif text.startswith("*/", i):
                    depth, i = depth - 1, i + 2
                else:
                    i += 1
            blank(start, i)
        else:
            prefix = STRING_START.match(text, i) if text[i] in {'#', '"'} else None
            if prefix:
                hashes = prefix.group(1) or ""
                quote = prefix.group(2)
                terminator = quote + hashes
                i += len(prefix.group(0))
                while i < n:
                    if text.startswith("\\" + hashes, i):
                        i = min(n, i + 2 + len(hashes))
                    elif text.startswith(terminator, i):
                        i += len(terminator)
                        break
                    else:
                        i += 1
                blank(start, i)
            else:
                i += 1
    return "".join(output)


def scan(root: Path) -> dict[str, object]:
    if not root.is_dir():
        raise ValueError("repository must be an existing directory")
    root = root.resolve()
    findings: list[Finding] = []
    skipped: list[dict[str, str]] = []
    scanned = 0
    for path in iter_files(root):
        relative = path.relative_to(root).as_posix()
        try:
            if path.stat().st_size > MAX_BYTES:
                skipped.append({"path": relative, "reason": "larger than 2 MiB"})
                continue
            raw = path.read_bytes()
            if b"\x00" in raw:
                skipped.append({"path": relative, "reason": "binary"})
                continue
            text = raw.decode("utf-8")
        except UnicodeError:
            skipped.append({"path": relative, "reason": "not UTF-8"})
            continue
        except OSError:
            skipped.append({"path": relative, "reason": "unreadable"})
            continue
        scanned += 1
        line_starts = [0] + [m.end() for m in re.finditer("\n", text)]
        for rule_id, pattern, severity, message in (
            ("possible-credential", SECRET, "error", "Possible credential; content is redacted. Review and rotate if real."),
            ("local-path", LOCAL_PATH, "warning", "Local-machine path may leak private information or break portability."),
        ):
            for match in pattern.finditer(text):
                findings.append(Finding(relative, bisect.bisect_right(line_starts, match.start()), rule_id, severity, message))
        if path.suffix == ".swift":
            code = mask_noncode(text)
            for rule in RULES:
                for match in rule.pattern.finditer(code):
                    findings.append(Finding(relative, bisect.bisect_right(line_starts, match.start()), rule.id, rule.severity, rule.message))
    findings.sort(key=lambda f: (f.path, f.line, f.rule))
    return {"method": "advisory-lexical-scan", "scanned_files": scanned,
            "findings": [asdict(f) for f in findings], "skipped": skipped,
            "limitations": "Not an AST, compiler, security audit, or HIG certification. Comments/strings are masked for Swift hints; interpolation code and regex literals are not fully parsed. Secrets are heuristic; symlinks and ignored build/dependency directories are not scanned."}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--fail-on", choices=tuple(SEVERITIES), default="error")
    args = parser.parse_args(argv)
    try:
        result = scan(args.repo)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        for finding in result["findings"]:
            print(f'{finding["path"]}:{finding["line"]}: {finding["severity"]}: {finding["rule"]}: {finding["message"]}')
        print(f'Advisory scan: {result["scanned_files"]} text files, {len(result["findings"])} findings, {len(result["skipped"])} skipped files. No finding is not proof of correctness.')
    threshold = SEVERITIES[args.fail_on]
    return int(any(SEVERITIES[f["severity"]] >= threshold for f in result["findings"]))


if __name__ == "__main__":
    raise SystemExit(main())
