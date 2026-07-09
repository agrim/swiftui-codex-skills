#!/usr/bin/env python3
"""Scan an Apple app repository for common SwiftUI and project hygiene risks."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


SKIP_DIRS = {
    ".build",
    ".git",
    "Build",
    "DerivedData",
    "Pods",
    "Carthage",
    "node_modules",
}


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: re.Pattern[str]
    extensions: tuple[str, ...] | None
    message: str


RULES = [
    Rule(
        "forced-button-foreground",
        re.compile(r"\.(foregroundStyle|foregroundColor)\s*\(\s*\.(white|black)\b"),
        (".swift",),
        "hard-coded white/black foreground can fight system-resolved button ink",
    ),
    Rule(
        "platform-bridge",
        re.compile(r"\b(import UIKit|import AppKit|UIViewControllerRepresentable|UIViewRepresentable|NSViewRepresentable)\b"),
        (".swift",),
        "platform bridge needs an explicit native-SwiftUI justification",
    ),
    Rule(
        "gesture-as-button",
        re.compile(r"\.onTapGesture\s*\{"),
        (".swift",),
        "tap gesture may be a fake button; prefer Button/Menu/NavigationLink when semantic",
    ),
    Rule(
        "absolute-local-path",
        re.compile("/" + "Users" + r"/[A-Za-z0-9._-]+|/(?:private/)?" + "var" + r"/folders/"),
        None,
        "absolute local path should not be committed",
    ),
    Rule(
        "private-token",
        re.compile(r"gh[oprsu]_[A-Za-z0-9_]+|github_pat_[A-Za-z0-9_]+|sk-[A-Za-z0-9_-]{20,}"),
        None,
        "possible secret token",
    ),
]


def should_scan(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    return path.is_file()


def iter_files(root: Path) -> list[Path]:
    return sorted(path for path in root.rglob("*") if should_scan(path))


def scan_file(path: Path, root: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    findings: list[str] = []
    for rule in RULES:
        if rule.extensions is not None and path.suffix not in rule.extensions:
            continue
        for match in rule.pattern.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            rel = path.relative_to(root)
            findings.append(f"{rel}:{line}: {rule.name}: {rule.message}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path)
    args = parser.parse_args()

    root = args.repo.resolve()
    if not root.exists():
        print(f"{root}: does not exist", file=sys.stderr)
        return 2

    findings: list[str] = []
    for path in iter_files(root):
        findings.extend(scan_file(path, root))

    if findings:
        for finding in findings:
            print(finding)
        return 1

    print(f"ok: no configured Apple repo hygiene findings in {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
