"""Local installation receipts and read-only content comparison.

Receipts describe the bytes copied, not a trusted signature or an update policy.
No absolute source/destination paths or remote URLs are recorded.
"""
from __future__ import annotations

import hashlib
import json
import re
import stat
import subprocess
from pathlib import Path
from typing import Any

from skilllib import read_json, safe_path

RECEIPT = ".skill-install.json"


def check_destination(destination: Path) -> None:
    if not destination.is_dir() or any(p.is_symlink() for p in [destination, *destination.parents]):
        raise ValueError("destination must be an existing, non-symlink directory")


def fingerprint(folder: Path, *, installed: bool = False) -> dict[str, str]:
    """Hash all regular files, rejecting links/special files before reading them."""
    if not folder.is_dir() or folder.is_symlink():
        raise ValueError("skill must be a regular directory")
    files = {}
    for path in sorted(folder.rglob("*")):
        mode = path.lstat().st_mode
        if not (stat.S_ISDIR(mode) or stat.S_ISREG(mode)):
            raise ValueError("refusing symlink or special file in skill")
        relative = path.relative_to(folder).as_posix()
        if relative == RECEIPT:
            if not installed or not stat.S_ISREG(mode):
                raise ValueError("reserved installation receipt in source or invalid receipt")
            continue
        if stat.S_ISREG(mode):
            files[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
    return files


def revision(root: Path, name: str) -> dict[str, Any]:
    """Git identity is supplementary; hashes also work for exports and dirty trees."""
    try:
        def git(*args: str) -> str:
            return subprocess.check_output(
                ["git", "-C", str(root), *args], stderr=subprocess.DEVNULL,
                text=True, timeout=5,
            ).strip()
        if Path(git("rev-parse", "--show-toplevel")).resolve() != root.resolve():
            return {"commit": None, "skill_dirty": None}
        return {"commit": git("rev-parse", "HEAD"),
                "skill_dirty": bool(git("status", "--porcelain", "--untracked-files=all", "--", f"skills/{name}"))}
    except (OSError, subprocess.SubprocessError):
        return {"commit": None, "skill_dirty": None}


def write_receipt(target: Path, name: str, files: dict[str, str], source: dict[str, Any]) -> None:
    # Check copied bytes before declaring an installation recorded.
    if fingerprint(target) != files:
        raise ValueError("copied skill differs from preflight; installation has no receipt")
    with (target / RECEIPT).open("x", encoding="utf-8") as stream:
        json.dump({"schema_version": 1, "skill": name, "source": source, "files": files},
                  stream, indent=2, sort_keys=True)
        stream.write("\n")


def read_receipt(folder: Path, name: str) -> dict[str, Any] | None:
    path = folder / RECEIPT
    if not path.exists():
        return None
    data = read_json(path)
    files, source = data.get("files"), data.get("source")
    if data.get("schema_version") != 1 or data.get("skill") != name or not isinstance(files, dict) or not files:
        raise ValueError("invalid installation receipt")
    for relative, digest in files.items():
        # Validate names without trusting receipt paths to read arbitrary files.
        safe_path(folder, relative)
        if relative == RECEIPT or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError("invalid installation receipt file hash")
    if not isinstance(source, dict):
        raise ValueError("invalid installation source identity")
    commit = source.get("commit")
    if commit is not None and (not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40,64}", commit)):
        raise ValueError("invalid installation source commit")
    if source.get("skill_dirty") is not None and type(source["skill_dirty"]) is not bool:
        raise ValueError("invalid installation source state")
    return data


def differences(current: dict[str, str], desired: dict[str, str]) -> dict[str, list[str]]:
    return {
        "installed_only": sorted(current.keys() - desired.keys()),
        "source_only": sorted(desired.keys() - current.keys()),
        "modified": sorted(name for name in current.keys() & desired.keys() if current[name] != desired[name]),
    }


def installation_status(root: Path, names: list[str], destination: Path) -> list[dict[str, Any]]:
    check_destination(destination)
    results = []
    for name in names:
        desired = fingerprint(safe_path(root, f"skills/{name}"))
        target = safe_path(destination, name)
        if not target.exists():
            results.append({"id": name, "state": "missing", "matches_source": False})
            continue
        current = fingerprint(target, installed=True)
        receipt = read_receipt(target, name)
        item: dict[str, Any] = {"id": name, "matches_source": current == desired,
                                "changes": differences(current, desired)}
        if receipt is None:
            item["state"] = "untracked"
        else:
            local_changed = current != receipt["files"]
            source_changed = desired != receipt["files"]
            item.update({"state": "both-changed" if local_changed and source_changed else
                         "local-changed" if local_changed else "source-changed" if source_changed else "current",
                         "installed_from": receipt["source"],
                         "local_changed": local_changed, "source_changed": source_changed})
        results.append(item)
    return results
