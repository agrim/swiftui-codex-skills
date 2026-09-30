#!/usr/bin/env python3
"""Validate review provenance and generate its human-readable map, without network I/O."""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

from skilllib import catalog, read_json, safe_path, valid_review_date

STATUSES = {"entrypoint-reviewed", "excerpt-reviewed", "overview-reviewed",
            "landing-page-only", "discovery-only", "unavailable"}
RELATIONS = {"recovered-list", "collection-member", "directory-discovery", "supporting-source"}
NOT_REVIEWED = {"discovery-only", "unavailable"}


def _text(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field}: expected nonempty text")
    if any(ord(c) < 32 for c in value):
        raise ValueError(f"{field}: control characters are not allowed")
    return value


def _url(value: object) -> str:
    value = _text(value, "url")
    parsed = urlsplit(value)
    if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password:
        raise ValueError("url: expected credential-free HTTPS URL")
    if any(c.isspace() for c in value):
        raise ValueError("url: whitespace is not allowed")
    return value


def validate(root: Path, data: dict) -> None:
    """Reject unsupported statuses, malformed hashes, unsafe paths, and unknown mappings.

A valid ledger is still a human review assertion, not independent proof that a
source was read, that its content is correct, or that every article link exists.
"""
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        raise ValueError("unsupported upstream schema_version")
    date = data.get("inventory_date")
    if not valid_review_date(date) or dt.date.fromisoformat(date) > dt.date.today():
        raise ValueError("inventory_date must be an ISO date, not in the future")
    article = data.get("article")
    if not isinstance(article, dict) or article.get("access") not in {"reconstructed", "full-text-reviewed"}:
        raise ValueError("article access status is missing or unsupported")
    _url(article.get("url"))
    _text(article.get("title"), "article.title")
    _text(article.get("limitation"), "article.limitation")
    _text(data.get("reuse"), "reuse")
    known = {item["id"] for item in catalog(root)["skills"]}
    records = data.get("resources")
    if not isinstance(records, list) or not records:
        raise ValueError("resources must be a nonempty array")
    seen: set[str] = set()
    for row in records:
        if not isinstance(row, dict):
            raise ValueError("each resource must be an object")
        sid = _text(row.get("id"), "resource.id")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", sid) or sid in seen:
            raise ValueError("invalid or duplicate upstream id: " + sid)
        seen.add(sid)
        _url(row.get("url"))
        _text(row.get("scope"), sid + ".scope")
        if row.get("status") not in STATUSES or row.get("relation") not in RELATIONS:
            raise ValueError(sid + ": unsupported review status or relation")
        reviewed = row.get("reviewed")
        if row["status"] in NOT_REVIEWED:
            if reviewed is not None:
                raise ValueError(sid + ": discovery/unavailable must not claim content review")
        elif not valid_review_date(reviewed) or reviewed > date:
            raise ValueError(sid + ": content review date is invalid or later than inventory")
        mapping = row.get("maps_to")
        if not isinstance(mapping, list) or not mapping or not all(isinstance(x, str) for x in mapping):
            raise ValueError(sid + ": maps_to must be a nonempty string array")
        if len(mapping) != len(set(mapping)) or not set(mapping).issubset(known):
            raise ValueError(sid + ": duplicate or unknown local skill mapping")
        for target in mapping:
            if not safe_path(root, f"skills/{target}/SKILL.md").is_file():
                raise ValueError(sid + ": missing mapped skill")
        sha, path = row.get("blob_sha"), row.get("path")
        if (sha is None) != (path is None):
            raise ValueError(sid + ": blob_sha and path must occur together")
        if sha is not None:
            if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{40}", sha):
                raise ValueError(sid + ": invalid Git blob SHA")
            # Validate syntax without interpreting the remote path as a local file.
            _text(path, sid + ".path")
            if "\\" in path or any(p in {"", ".", ".."} for p in path.split("/")):
                raise ValueError(sid + ": unsafe remote relative path")
            if urlsplit(row["url"]).hostname != "github.com":
                raise ValueError(sid + ": Git blob receipt requires a GitHub repository URL")
            if len(urlsplit(row["url"]).path.strip("/").split("/")) != 2:
                raise ValueError(sid + ": blob receipt URL must identify owner/repository")


def render(data: dict) -> str:
    def cell(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")
    lines = ["# Ecosystem provenance map", "", "Generated from `upstreams.json`; run `python3 scripts/upstream_audit.py --write`.", "",
             f'Inventory date: {data["inventory_date"]}.', "",
             f'Source article: [{data["article"]["title"]}]({data["article"]["url"]}).', "",
             "**Access boundary:** " + data["article"]["limitation"], "", data["reuse"], "",
             "Mappings indicate relevant local guidance, not feature parity or an audit of upstream implementation. `directory-discovery` is one level beyond the recovered article list. A reviewed entry point does not mean every supporting file was read.", "",
             "| Resource | Relationship / review | Local guidance | Review scope |", "| --- | --- | --- | --- |"]
    for row in data["resources"]:
        mapping = ", ".join(f'[{sid}](../skills/{sid}/SKILL.md)' for sid in row["maps_to"])
        scope = row["scope"]
        if row.get("blob_sha"):
            scope += f' Receipt: `{row["path"]}` at Git blob `{row["blob_sha"]}`.'
        lines.append("| " + " | ".join([f'[{row["id"]}]({row["url"]})', row["relation"] + " / " + row["status"], mapping, cell(scope)]) + " |")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.repo.resolve(strict=True)
        data = read_json(safe_path(root, "upstreams.json"))
        validate(root, data)
        output = safe_path(root, "docs/ecosystem.md")
        expected = render(data)
        if args.write:
            output.write_text(expected, encoding="utf-8")
        elif not output.is_file() or output.read_text(encoding="utf-8") != expected:
            raise ValueError("docs/ecosystem.md is missing or stale")
        print(f'ok: {len(data["resources"])} provenance records; no network, installation, or source-review claims inferred')
        return 0
    except (ValueError, OSError, TypeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
