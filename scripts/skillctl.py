#!/usr/bin/env python3
"""List, route, bundle, install, and document portable SwiftUI skills."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

from skilllib import catalog, frontmatter, generated_docs, safe_path
from skill_installation import (check_destination, fingerprint, installation_status,
                                revision, write_receipt)

DEFAULT_ROOT = Path(__file__).resolve().parents[1]


def select(root: Path, names: list[str]) -> list[dict[str, Any]]:
    if not names:
        raise ValueError("select at least one skill")
    items = {item["id"]: item for item in catalog(root)["skills"]}
    if len(names) != len(set(names)):
        raise ValueError("select each skill only once")
    missing = [name for name in names if name not in items]
    if missing:
        raise ValueError("unknown skill: " + ", ".join(missing))
    return [items[name] for name in names]


def route(root: Path, query: str, limit: int = 3) -> list[dict[str, Any]]:
    """Deterministic phrase retrieval, not an LLM or a correctness classifier."""
    normalized = " ".join(query.casefold().split())
    results = []
    for item in catalog(root)["skills"]:
        matches = [phrase for phrase in item["triggers"]
                   if re.search(r"(?<!\w)" + re.escape(phrase.casefold()) + r"(?!\w)", normalized)]
        if matches:
            score = sum(1 + len(phrase.split()) for phrase in matches)
            results.append({"id": item["id"], "score": score, "matched": sorted(matches)})
    return sorted(results, key=lambda item: (-item["score"], item["id"]))[:limit]


def bundle(root: Path, names: list[str], entrypoints_only: bool = False) -> str:
    items = select(root, names)
    lines = ["# Selected SwiftUI skills", "", "Portable Markdown bundle. Load only the modules needed for the task. Official links remain authoritative; no model or tool adapter is required.", ""]
    for item in items:
        sid = item["id"]
        folder = safe_path(root, f"skills/{sid}")
        text = safe_path(folder, "SKILL.md").read_text(encoding="utf-8")
        for index, reference in enumerate(item["references"]):
            # Generated anchors avoid basename collisions between selected skills.
            destination = f"#{sid}-reference-{index + 1}"
            if entrypoints_only:
                text = re.sub(r"\[([^\]\n]+)\]\(" + re.escape(reference) + r"\)",
                              r"\1 (not included; load it from the skill folder)", text)
            else:
                text = text.replace(f"]({reference})", f"]({destination})")
        lines += [f'<a id="{sid}"></a>', "", text.strip(), ""]
        if not entrypoints_only:
            for index, reference in enumerate(item["references"]):
                body = safe_path(folder, reference).read_text(encoding="utf-8")
                lines += [f'<a id="{sid}-reference-{index + 1}"></a>', "", body.strip(), ""]
    return "\n".join(lines).rstrip() + "\n"


def install(root: Path, names: list[str], destination: Path, dry_run: bool = False) -> list[str]:
    """Copy self-contained folders to an explicit directory without overwriting.

Preflight every selected source, required file, file type, and target before
copying. A disk/I/O failure or concurrent filesystem change can still leave
already-copied folders; this is not a transaction or an adversarial-filesystem
sandbox. Never remove existing user folders to recover from that failure.
"""
    items = select(root, names)
    check_destination(destination)
    pairs = []
    for item in items:
        source = safe_path(root, f'skills/{item["id"]}')
        target = safe_path(destination, item["id"])
        if target.exists():
            raise ValueError(f"refusing to overwrite installed skill: {item['id']}")
        if not source.is_dir():
            raise ValueError(f"missing skill directory: {item['id']}")
        files = fingerprint(source)
        entry = safe_path(source, "SKILL.md")
        if not entry.is_file():
            raise ValueError(f"missing SKILL.md: {item['id']}")
        if frontmatter(entry.read_text(encoding="utf-8"))["name"] != item["id"]:
            raise ValueError(f"frontmatter name differs from skill: {item['id']}")
        for reference in item["references"]:
            if not safe_path(source, reference).is_file():
                raise ValueError(f"missing skill reference: {item['id']}/{reference}")
        pairs.append((source, target, files, revision(root, item["id"])))
    if not dry_run:
        for source, target, files, identity in pairs:
            shutil.copytree(source, target, symlinks=True)
            write_receipt(target, target.name, files, identity)
    return [target.name for _, target, _, _ in pairs]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=DEFAULT_ROOT)
    subs = parser.add_subparsers(dest="command", required=True)
    listing = subs.add_parser("list")
    listing.add_argument("--json", action="store_true")
    routing = subs.add_parser("route")
    routing.add_argument("query")
    routing.add_argument("--json", action="store_true")
    routing.add_argument("--limit", type=int, default=3)
    bundling = subs.add_parser("bundle")
    bundling.add_argument("skills", nargs="+")
    bundling.add_argument("--entrypoints-only", action="store_true")
    bundling.add_argument("--output", type=Path)
    installing = subs.add_parser("install")
    installing.add_argument("skills", nargs="+")
    installing.add_argument("--dest", required=True, type=Path)
    installing.add_argument("--dry-run", action="store_true")
    status = subs.add_parser("status", help="compare installed bytes without changing them")
    status.add_argument("skills", nargs="+")
    status.add_argument("--dest", required=True, type=Path)
    status.add_argument("--json", action="store_true")
    status.add_argument("--diff", action="store_true", help="list changed file names, never file contents")
    subs.add_parser("docs").add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            items = catalog(args.repo)["skills"]
            print(json.dumps(items, indent=2) if args.json else "\n".join(f'{i["id"]}: {i["summary"]}' for i in items))
        elif args.command == "route":
            if not 1 <= args.limit <= 20:
                raise ValueError("limit must be between 1 and 20")
            result = route(args.repo, args.query, args.limit)
            print(json.dumps({"method": "deterministic-phrase-match", "matches": result}, indent=2) if args.json else "\n".join(f'{i["id"]} ({i["score"]}): {", ".join(i["matched"])}' for i in result) or "No phrase match. Read the catalog; do not infer that no skill applies.")
        elif args.command == "bundle":
            result = bundle(args.repo, args.skills, args.entrypoints_only)
            if args.output:
                # Explicit file output, but avoid silent destruction of an existing file.
                with args.output.open("x", encoding="utf-8") as output:
                    output.write(result)
                print(f"Wrote {args.output}")
            else:
                print(result, end="")
        elif args.command == "install":
            names = install(args.repo, args.skills, args.dest, args.dry_run)
            print(("Would install: " if args.dry_run else "Installed: ") + ", ".join(names))
        elif args.command == "status":
            names = [item["id"] for item in select(args.repo, args.skills)]
            results = installation_status(args.repo, names, args.dest)
            if args.json:
                print(json.dumps(results, indent=2))
            else:
                for item in results:
                    print(f'{item["id"]}: {item["state"]}; matches source: {item["matches_source"]}')
                    if args.diff:
                        for kind, files in item.get("changes", {}).items():
                            for filename in files:
                                print(f"  {kind}: {filename}")
        elif args.command == "docs":
            stale = []
            for relative, expected in generated_docs(args.repo).items():
                target = safe_path(args.repo, relative)
                if args.check:
                    if not target.is_file() or target.read_text(encoding="utf-8") != expected:
                        stale.append(relative)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(expected, encoding="utf-8")
            if stale:
                raise ValueError("stale generated docs: " + ", ".join(stale))
            print("ok: generated documentation " + ("matches" if args.check else "updated"))
        return 0
    except (OSError, ValueError, KeyError, TypeError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
