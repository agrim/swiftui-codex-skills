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
RULE = re.compile(r"- \*\*(?P<id>[A-Z]+-[0-9]{3}) — (?P<title>[^*\s][^*]*?\.)\*\* (?P<instruction>\S.*)")
HEADINGS = ("Inputs", "Rules", "Workflow", "Verify", "Output", "References")
GUIDE_HEADINGS = ("Start here", "How to proceed", "Check the result", "What to report")
DECISION_HEADINGS = ("Design choices", "Try it")
RULE_ID = r"[A-Z]+-[0-9]{3}"
ACTION = re.compile(rf"(?P<number>[0-9]+)\. \*\*(?P<title>[^*\s][^*]*?\.)\*\* (?P<instruction>\S.*?) <!-- (?P<id>{RULE_ID}) -->")
CHECK = re.compile(rf"- (?P<check>\S.*?) <!-- (?P<ids>{RULE_ID}(?: {RULE_ID})*) -->")
REFERENCE = re.compile(r"- \[(?P<label>[^\]\s][^\]\n]*)\]\((?P<path>references/[^()\s]+\.md)\)")
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
            # Linked worktrees store their private Git pointer as a file.
            if name == ".git":
                continue
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
        if key == "description" and not raw.startswith('"'):
            raise ValueError("description must be a JSON-quoted single-line string")
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


def _paragraph(heading: str, content: str) -> str:
    if not content.strip() or re.search(r"\n\s*\n|^(?: {4}|\t| {0,3}(?:#+ |[-*+] |[0-9]+[.)] |>|\|))", content, re.M):
        raise ValueError(f"{heading} must be one paragraph")
    return " ".join(line.strip() for line in content.splitlines())


def _entries(heading: str, content: str, pattern: str | re.Pattern[str]) -> list[re.Match[str]]:
    matches = []
    for number, line in enumerate(content.splitlines(), 1):
        if not line.strip():
            continue
        match = re.fullmatch(pattern, line)
        if match is None:
            raise ValueError(f"invalid {heading} entry on section line {number}")
        if "number" in match.re.groupindex and match["number"] != str(len(matches) + 1):
            raise ValueError(f"expected {heading} step {len(matches) + 1}")
        matches.append(match)
    if not matches:
        raise ValueError(f"empty {heading} section")
    return matches


def _legacy_fields(intro: str, sections: dict[str, str]) -> dict[str, Any]:
    title = re.fullmatch(r"# (\S[^\n]*)", intro)
    if title is None:
        raise ValueError("expected a title followed by " + ", ".join(HEADINGS) + " in order")
    rules = _entries("Rules", sections["Rules"], RULE)
    workflow = _entries("Workflow", sections["Workflow"], r"(?P<number>[0-9]+)\. (\S.*)")
    checks = _entries("Verify", sections["Verify"], r"- ([^:]+): (\S.*)")
    return {"title": title[1], "inputs": _paragraph("Inputs", sections["Inputs"]),
            "rules": [match.groupdict() for match in rules], "workflow": [match[2] for match in workflow],
            "verify": [{"rule_ids": match[1].split(", "), "check": match[2]} for match in checks],
            "output": _paragraph("Output", sections["Output"]),
            "references": [m.groupdict() for m in _entries("References", sections["References"], REFERENCE)]}


def _guide_fields(intro: str, sections: dict[str, str]) -> dict[str, Any]:
    opening = re.fullmatch(r"# (\S[^\n]*)\n[ \t]*\n(.+)", intro, re.S)
    if opening is None:
        raise ValueError("expected a title followed by an opening paragraph")
    first_paragraph = _paragraph("Opening", opening[2])
    fields = {"title": opening[1]}
    if "Design choices" in sections:
        trial = re.split(r"\n[ \t]*\n", sections["Try it"])
        if len(trial) != 3:
            raise ValueError("Try it requires an acceptance goal, checks and local case links")
        outcome, check_text, links = trial
        fields.update(inputs=first_paragraph, output=_paragraph("Acceptance goal", outcome))
        step_text = sections["Design choices"]
    else:
        report = re.split(r"\n[ \t]*\n", sections["What to report"], maxsplit=1)
        if len(report) != 2:
            raise ValueError("What to report must end with a blank line and playbook links")
        outcome, links = report
        fields.update(purpose=first_paragraph, inputs=_paragraph("Start here", sections["Start here"]),
                      output=_paragraph("What to report", outcome))
        step_text, check_text = sections["How to proceed"], sections["Check the result"]
    steps = _entries("Design choices", step_text, ACTION)
    checks = _entries("Checks", check_text, CHECK)
    return {**fields,
            "rules": [{key: m[key] for key in ("id", "title", "instruction")} for m in steps],
            "workflow": [m["title"] for m in steps],
            "verify": [{"rule_ids": m["ids"].split(), "check": m["check"]} for m in checks],
            "references": [m.groupdict() for m in _entries("Playbook links", links, REFERENCE)]}


def skill_contract(folder: Path, item: dict[str, Any], text: str, seen_rules: set[str]) -> dict[str, Any]:
    """Export current and previously published entry formats through the same interface."""
    text = text.replace("\r\n", "\n")
    meta = frontmatter(text)
    if meta["name"] != item["id"] or meta["description"] != item["summary"]:
        raise ValueError("frontmatter name and description must match the catalog")

    body = text.split("\n---\n", 1)[1]
    if re.search(r"^\s*(?:`{3,}|~{3,})", body, re.M):
        raise ValueError("put fenced examples in a playbook")
    parts = re.split(r"^## ([^\n]*)$", body, flags=re.M)
    headings = tuple(parts[1::2])
    intro = parts[0].strip("\n")
    sections = dict(zip(headings, (part.strip("\n") for part in parts[2::2])))
    for heading, content in sections.items():
        if heading != "Rules" and re.search(r"^- \*\*[A-Z]+-[0-9]{3} — ", content, re.M):
            raise ValueError(f"rule declaration outside Rules in {heading}")
    if headings in (DECISION_HEADINGS, GUIDE_HEADINGS):
        fields = _guide_fields(intro, sections)
        expected_comments = len(fields["rules"]) + len(fields["verify"])
        if body.count("<!--") != expected_comments or body.count("-->") != expected_comments:
            raise ValueError("only actions and checks may carry rule comments")
    elif headings == HEADINGS:
        fields = _legacy_fields(intro, sections)
    else:
        raise ValueError("expected guide headings in order: " + ", ".join(DECISION_HEADINGS))

    declared: set[str] = set()
    for rule in fields["rules"]:
        rule_id = rule["id"]
        if rule_id in declared or rule_id in seen_rules:
            raise ValueError(f"duplicate rule ID {rule_id}")
        declared.add(rule_id)
    for check in fields["verify"]:
        rule_ids = check["rule_ids"]
        if not declared.issuperset(rule_ids) or len(rule_ids) != len(set(rule_ids)):
            raise ValueError("each verification check must cite distinct rule IDs from this skill")

    for relative in item["references"]:
        if not safe_path(folder, relative).is_file():
            raise ValueError(f"missing reference: {relative}")
    paths = [ref["path"] for ref in fields["references"]]
    if len(paths) != len(set(paths)) or sorted(paths) != sorted(item["references"]):
        raise ValueError("References must list each catalog path once")
    seen_rules.update(declared)
    title = fields.pop("title")
    return {"id": meta["name"], "title": title, "description": meta["description"], **fields}


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
    active = {item.get("id") for item in data["skills"] if isinstance(item.get("id"), str)}
    retired = data.get("retired", {})
    if not isinstance(retired, dict) or any(
        not SLUG.fullmatch(name) or name in active or
        (target is not None and (not isinstance(target, str) or target not in active))
        for name, target in retired.items()
    ):
        raise ValueError("catalog.json: invalid retired skill mapping")
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
    coverage = ["# Coverage map", "", "Generated from `catalog.json`; run `python3 scripts/skillctl.py docs` to update.", "", "Select a skill for the engineering decision you face. Each folder includes its own checks and worked cases. Review provenance is available in the [source registry](sources.md).", "", "| Skill | Scope | Platforms | Boundary |", "| --- | --- | --- | --- |"]
    for item in items:
        cells = [f'[{item["id"]}](../skills/{item["id"]}/SKILL.md)', item["summary"], ", ".join(item["platforms"]), item["limits"]]
        coverage.append("| " + " | ".join(cell.replace("|", "\\|") for cell in cells) + " |")
    coverage += ["", "## Applicability versus execution", "", "The Platforms column describes where the engineering guidance may apply, not a list of tested destinations. The example package configures macOS 14 and iOS 17 minimums. CI is configured for macOS example execution and iOS SDK compilation; those definitions alone are not successful run receipts. Other listed platforms require their own relevant builds and runtime evidence. See the examples README and evaluation records for the precise contracts exercised.", "", "## Deliberate limits", "", "Select a guide when you face the product decision it describes. Use framework documentation for API mechanics and tool help for build and distribution commands. The [migration guide](skill-migration.md) explains the revised scope. The [evaluation protocol](evaluation.md) describes how to assess behavior on an app task."]
    refs = ["# Primary-source registry", "", "Generated from `sources.json`; run `python3 scripts/skillctl.py docs` to update.", "", "`content-reviewed` means relevant page content was inspected for this revision; it is not a guarantee that every linked API, platform, or rule was verified. `reference-only` is a discovery route whose content has not been reviewed in this revision. A successful HTTP request does not upgrade this status. Dates are review records, not automatic freshness guarantees.", "", "| ID | Official source | Status | Reviewed |", "| --- | --- | --- | --- |"]
    for item in sorted(sources, key=lambda s: s["id"]):
        refs.append(f'| `{item["id"]}` | [{item["title"]}]({item["url"]}) | {item["status"]} | {item["reviewed"] or "—"} |')
    scoped = [item for item in sources if item.get("review_scope")]
    if scoped:
        refs += ["", "## Scoped review notes", ""]
        for item in sorted(scoped, key=lambda s: s["id"]):
            refs += [f'`{item["id"]}`: {item["review_scope"]}', ""]
    refs += ["", "## Refresh policy", "", "Before using a version-sensitive API or a release/privacy requirement, inspect the current official page and installed SDK. Re-review affected sources on relevant SDK/HIG releases or reported contradictions. Update dates only after inspecting content and recording any resulting changes. Prefer the precise symbol/article over a framework landing page. Never infer API availability from a source review date."]
    return {"docs/coverage.md": "\n".join(coverage) + "\n", "docs/sources.md": "\n".join(refs) + "\n"}
