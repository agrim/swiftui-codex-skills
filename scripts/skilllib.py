"""Shared, standard-library-only support for the portable skill library.

The frontmatter reader deliberately accepts a documented scalar subset of YAML;
it is not a general YAML parser. Published descriptions use JSON-quoted strings,
which are valid YAML scalars and avoid ambiguous punctuation.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
from pathlib import Path
from typing import Any, Iterator
from urllib.parse import unquote, urlsplit

SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
RULE = re.compile(r"\*\*([A-Z]+-\d{3})\s+—")
HEADINGS = ("Inputs", "Rules", "Workflow", "Verify", "Output", "References")
PLATFORMS = {"iOS", "iPadOS", "macOS", "watchOS", "tvOS", "visionOS"}
IGNORED = {".git", ".build", ".build-ios", "__pycache__", ".pytest_cache", "DerivedData", "node_modules", "Pods", "Carthage", ".venv", "venv", "build", "Build", "dist"}
PRIMARY_HOSTS = {"developer.apple.com", "support.apple.com", "www.apple.com", "docs.swift.org", "www.swift.org", "swift.org"}


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path: Path) -> dict[str, Any]:
    def invalid_constant(value: str) -> None:
        raise ValueError(f"invalid JSON constant: {value}")
    value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object, parse_constant=invalid_constant)
    if not isinstance(value, dict):
        raise ValueError(f"{path.name}: expected a JSON object")
    return value


def safe_path(root: Path, relative: str) -> Path:
    """Resolve an existing or prospective child without accepting symlink escapes."""
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError("expected a nonempty POSIX relative path")
    parts = relative.split("/")
    if relative.startswith("/") or any(part in {"", ".", ".."} for part in parts):
        raise ValueError(f"unsafe relative path: {relative}")
    current = root.resolve()
    for part in parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"symlink is not allowed: {relative}")
    if not current.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"path escapes root: {relative}")
    return current


def iter_files(root: Path) -> Iterator[Path]:
    """Prune ignored descendants, never follow directory or file symlinks."""
    for directory, dirs, names in os.walk(root, followlinks=False):
        base = Path(directory)
        dirs[:] = sorted(d for d in dirs if d not in IGNORED and not (base / d).is_symlink())
        for name in sorted(names):
            path = base / name
            if not path.is_symlink() and path.is_file():
                yield path


def frontmatter(text: str) -> dict[str, str]:
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("missing or unterminated frontmatter")
    block = text[4:].split("\n---\n", 1)[0]
    result: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_-]*): (.+)", line)
        if not match:
            raise ValueError("frontmatter requires single-line key: scalar fields")
        key, raw = match.groups()
        if key in result:
            raise ValueError(f"duplicate frontmatter key: {key}")
        if key not in {"name", "description"}:
            raise ValueError(f"unsupported frontmatter key: {key}")
        if raw.startswith('"'):
            try:
                value = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise ValueError("invalid quoted frontmatter scalar") from exc
            if not isinstance(value, str):
                raise ValueError("frontmatter values must be strings")
        else:
            if raw[0] in "'|>[{&*!" or ": " in raw or " #" in raw or raw in {"null", "true", "false", "~"}:
                raise ValueError("ambiguous YAML scalar; use a JSON-quoted string")
            value = raw
        if not value.strip() or "\n" in value:
            raise ValueError("frontmatter values must be nonempty single-line strings")
        result[key] = value
    if set(result) != {"name", "description"}:
        raise ValueError("frontmatter requires name and description")
    return result


def without_fences(text: str) -> str:
    lines: list[str] = []
    fence: str | None = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines.append("")
        else:
            lines.append(line if fence is None else "")
    return "\n".join(lines)


def local_links(text: str) -> Iterator[str]:
    # Published local URLs contain no parentheses/spaces. External URLs are not
    # linted as local paths; network availability is a separate, opt-in check.
    for target in re.findall(r"\[[^\]\n]*\]\(([^\s)]+)\)", without_fences(text)):
        if not urlsplit(target).scheme and not target.startswith(("#", "//")):
            yield unquote(target.split("#", 1)[0])


def catalog(root: Path) -> dict[str, Any]:
    data = read_json(root / "catalog.json")
    if data.get("schema_version") != 1 or not isinstance(data.get("skills"), list):
        raise ValueError("catalog.json: unsupported schema or missing skills array")
    if not data["skills"] or not all(isinstance(item, dict) for item in data["skills"]):
        raise ValueError("catalog.json: skills must be a nonempty object array")
    return data


def source_registry(root: Path) -> dict[str, Any]:
    data = read_json(root / "sources.json")
    if data.get("schema_version") != 1 or not isinstance(data.get("sources"), list):
        raise ValueError("sources.json: unsupported schema or missing sources array")
    if not all(isinstance(item, dict) for item in data["sources"]):
        raise ValueError("sources.json: sources must be an object array")
    return data


def valid_review_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError:
        return False
    return value == parsed.isoformat()


def generated_docs(root: Path) -> dict[str, str]:
    items = catalog(root)["skills"]
    sources = source_registry(root)["sources"]
    coverage = ["# Coverage map", "", "Generated from `catalog.json`; run `python3 scripts/skillctl.py docs` to update.", "", "**Practical coverage is not exhaustive Apple documentation coverage.** Each module provides a decision workflow, failure cases, verification, and primary-source routes. Framework details still require the current SDK and linked documentation. No percentage of all Apple APIs or HIG pages is claimed.", "", "| Skill | Scope | Platforms | Boundary |", "| --- | --- | --- | --- |"]
    for item in items:
        cells = [f'[{item["id"]}](../skills/{item["id"]}/SKILL.md)', item["summary"], ", ".join(item["platforms"]), item["limits"]]
        coverage.append("| " + " | ".join(cell.replace("|", "\\|") for cell in cells) + " |")
    coverage += ["", "## Deliberate limits", "", "This is not a replacement for Apple documentation, legal review, platform testing, or specialist implementations of graphics engines, media pipelines, security protocols, machine learning, or medical algorithms. Platform and framework coverage is uneven by design: common SwiftUI decisions are deeper than specialist APIs. The source registry distinguishes reviewed content from discovery links. Behavioral quality across models requires the evaluation procedure, not just passing repository lint."]
    refs = ["# Primary-source registry", "", "Generated from `sources.json`; run `python3 scripts/skillctl.py docs` to update.", "", "`content-reviewed` means relevant page content was inspected for this revision; it is not a guarantee that every linked API, platform, or rule was verified. `reference-only` is a discovery route whose content has not been reviewed in this revision. A successful HTTP request does not upgrade this status. Dates are review records, not automatic freshness guarantees.", "", "| ID | Official source | Status | Reviewed |", "| --- | --- | --- | --- |"]
    for item in sorted(sources, key=lambda s: s["id"]):
        refs.append(f'| `{item["id"]}` | [{item["title"]}]({item["url"]}) | {item["status"]} | {item["reviewed"] or "—"} |')
    refs += ["", "## Refresh policy", "", "Before using a version-sensitive API or a release/privacy requirement, inspect the current official page and installed SDK. Re-review affected sources on relevant SDK/HIG releases or reported contradictions. Update dates only after inspecting content and recording any resulting changes. Prefer the precise symbol/article over a framework landing page. Never infer API availability from a source review date."]
    return {"docs/coverage.md": "\n".join(coverage) + "\n", "docs/sources.md": "\n".join(refs) + "\n"}
