#!/usr/bin/env python3
"""Validate portable skill contracts, catalogs, source links, and public hygiene."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

from skilllib import (HEADINGS, PLATFORMS, PRIMARY_HOSTS, RULE, SLUG, catalog,
                      frontmatter, generated_docs, iter_files, local_links,
                      safe_path, source_registry, valid_review_date)

SECRET = re.compile(r"(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-(?:proj-)?[A-Za-z0-9_-]{24,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)")
LOCAL_PATH = re.compile("/" + "Users" + r"/[A-Za-z0-9._-]+|/(?:private/)?" + "var" + r"/folders/")
VENDOR_CORE = re.compile(r"\b(?:Codex|ChatGPT|Claude|OpenAI|XcodeBuildMCP|CODEX_HOME)\b|\$[a-z]+-[a-z-]+", re.I)
MAX_ENTRY_WORDS = 650
MAX_REFERENCE_WORDS = 1800


def validate(root: Path, check_generated: bool = True) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    if not root.is_dir():
        return ["repository directory does not exist"]
    try:
        data, registry = catalog(root), source_registry(root)
    except (OSError, ValueError, UnicodeError) as exc:
        return [str(exc)]
    items = data["skills"]
    ids: set[str] = set()
    source_ids: set[str] = set()
    source_urls: dict[str, str] = {}
    for item in registry["sources"]:
        sid = item.get("id")
        if not isinstance(sid, str) or not SLUG.fullmatch(sid):
            errors.append("sources.json: invalid source id")
            continue
        if sid in source_ids:
            errors.append(f"sources.json: duplicate source {sid}")
        source_ids.add(sid)
        url = item.get("url", "")
        if not isinstance(url, str):
            errors.append(f"source {sid}: URL must be a string")
            continue
        try:
            parsed = urlsplit(url)
        except ValueError:
            errors.append(f"source {sid}: malformed URL")
            continue
        if parsed.scheme != "https" or parsed.hostname not in PRIMARY_HOSTS or parsed.username or parsed.password:
            errors.append(f"source {sid}: expected an HTTPS primary-source URL")
        source_urls[sid] = url
        if not isinstance(item.get("title"), str) or not item["title"].strip():
            errors.append(f"source {sid}: missing title")
        status, reviewed = item.get("status"), item.get("reviewed")
        if status == "content-reviewed":
            if not valid_review_date(reviewed):
                errors.append(f"source {sid}: reviewed content requires an ISO date")
        elif status == "reference-only":
            if reviewed is not None:
                errors.append(f"source {sid}: reference-only must not claim a review date")
        else:
            errors.append(f"source {sid}: unknown review status")
    all_rules: set[str] = set()
    for item in items:
        sid = item.get("id")
        if not isinstance(sid, str) or not SLUG.fullmatch(sid) or len(sid) > 64:
            errors.append("catalog.json: invalid skill id")
            continue
        if sid in ids:
            errors.append(f"catalog.json: duplicate skill {sid}")
        ids.add(sid)
        for field in ("title", "summary", "limits"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{sid}: missing {field}")
        if item.get("coverage") != "practical":
            errors.append(f"{sid}: coverage must be practical; do not imply exhaustive coverage")
        arrays_ok = True
        for field in ("triggers", "platforms", "references", "sources"):
            values = item.get(field)
            if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                errors.append(f"{sid}: {field} must be a nonempty string array")
                arrays_ok = False
            elif len(values) != len(set(values)):
                errors.append(f"{sid}: duplicate {field} entry")
        if not arrays_ok:
            continue
        if not set(item["platforms"]) <= PLATFORMS:
            errors.append(f"{sid}: unknown platform")
        try:
            folder = safe_path(root, f"skills/{sid}")
            entry = safe_path(folder, "SKILL.md")
            text = entry.read_text(encoding="utf-8")
            meta = frontmatter(text)
            if meta["name"] != sid:
                errors.append(f"{sid}: frontmatter name must equal folder name")
            if meta["description"] != item.get("summary"):
                errors.append(f"{sid}: description and catalog summary differ")
            if len(meta["description"]) > 1024:
                errors.append(f"{sid}: description exceeds 1024 characters")
            if len(text.split()) > MAX_ENTRY_WORDS:
                errors.append(f"{sid}: entrypoint exceeds {MAX_ENTRY_WORDS} words")
            for heading in HEADINGS:
                if f"\n## {heading}\n" not in text:
                    errors.append(f"{sid}: missing {heading} section")
            rules = RULE.findall(text)
            if not rules:
                errors.append(f"{sid}: no stable rule IDs")
            for rule in rules:
                if rule in all_rules:
                    errors.append(f"{sid}: duplicate rule ID {rule}")
                all_rules.add(rule)
            reference_texts = []
            for relative in item["references"]:
                reference = safe_path(folder, relative)
                if not relative.startswith("references/") or reference.suffix != ".md":
                    errors.append(f"{sid}: references must be Markdown under references/")
                body = reference.read_text(encoding="utf-8")
                reference_texts.append(body)
                if relative not in set(local_links(text)):
                    errors.append(f"{sid}: reference is not linked from SKILL.md: {relative}")
                if len(body.split()) > MAX_REFERENCE_WORDS:
                    errors.append(f"{sid}: reference exceeds {MAX_REFERENCE_WORDS} words: {relative}")
            full_text = "\n".join([text, *reference_texts])
            if VENDOR_CORE.search(full_text):
                errors.append(f"{sid}: core guidance contains vendor-specific names/invocations")
            for source in item["sources"]:
                if source not in source_ids:
                    errors.append(f"{sid}: unknown source {source}")
                elif source_urls.get(source, "MISSING") not in full_text:
                    errors.append(f"{sid}: source {source} is not linked from its playbook")
            actual_refs = {str(p.relative_to(folder)) for p in (folder / "references").glob("*.md") if p.is_file()}
            if actual_refs != set(item["references"]):
                errors.append(f"{sid}: reference directory and catalog differ")
        except (OSError, ValueError, UnicodeError) as exc:
            errors.append(f"{sid}: {exc}")
    if data.get("entrypoint") not in ids:
        errors.append("catalog.json: unknown entrypoint")
    actual_ids = {p.name for p in (root / "skills").iterdir() if p.is_dir()} if (root / "skills").is_dir() else set()
    if actual_ids != ids:
        errors.append("catalog.json: published skill directories and catalog differ")
    for path in iter_files(root):
        if path.suffix not in {".md", ".json", ".py", ".yaml", ".yml", ".swift", ".toml"}:
            continue
        relative = str(path.relative_to(root))
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"{relative}: cannot read UTF-8 text")
            continue
        for label, pattern in (("possible credential", SECRET), ("local-machine path", LOCAL_PATH)):
            if pattern.search(text):
                errors.append(f"{relative}: {label}; content redacted")
        if path.suffix == ".md":
            for target in local_links(text):
                # Documentation may link up to the repository, but never outside it.
                destination = path.parent / target
                if not destination.resolve().is_relative_to(root) or any(p.is_symlink() for p in [destination, *destination.parents] if p != root):
                    errors.append(f"{relative}: unsafe local link")
                elif not destination.exists():
                    errors.append(f"{relative}: broken local link: {target}")
    if check_generated and not errors:
        try:
            for relative, expected in generated_docs(root).items():
                if not (root / relative).is_file() or (root / relative).read_text(encoding="utf-8") != expected:
                    errors.append(f"{relative}: generated documentation is stale; run skillctl.py docs")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"generated docs: {exc}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)
    errors = validate(args.repo)
    if args.format == "json":
        print(json.dumps({"ok": not errors, "errors": errors}, indent=2))
    elif errors:
        print("\n".join(errors), file=sys.stderr)
    else:
        print("ok: skill contracts, catalogs, local links, generated docs, and public hygiene")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
