#!/usr/bin/env python3
"""Validate Codex skill folders without third-party dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SKILL_NAME = re.compile(r"^[a-z0-9-]{1,63}$")
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
MAC_USER_PATH = re.compile("/" + "Users" + r"/[A-Za-z0-9._-]+")
MAC_TEMP_PATH = re.compile(r"/(?:private/)?" + "var" + r"/folders/")
CODEX_CLIPBOARD_PATH = re.compile("codex-" + r"clipboard-[A-Za-z0-9-]+")
PUBLIC_SCRUB_PATTERNS = [
    ("absolute macOS user path", MAC_USER_PATH),
    ("temporary macOS folder", MAC_TEMP_PATH),
    ("Codex private state path", re.compile(r"\.codex/(sessions|memories|state)")),
    ("clipboard artifact", CODEX_CLIPBOARD_PATH),
    ("GitHub token", re.compile(r"gh[oprsu]_[A-Za-z0-9_]+")),
    ("GitHub fine-grained token", re.compile(r"github_pat_[A-Za-z0-9_]+")),
    ("OpenAI API key", re.compile(r"sk-[A-Za-z0-9_-]{20,}")),
    ("private key", re.compile(r"BEGIN [A-Z ]*PRIVATE KEY")),
    ("email address", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")),
]


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        raise ValueError("missing YAML frontmatter")

    data: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {raw_line}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate_agent_metadata(skill_dir: Path, skill_name: str, errors: list[str]) -> None:
    metadata_path = skill_dir / "agents" / "openai.yaml"
    if not metadata_path.exists():
        errors.append(f"{skill_dir}: missing agents/openai.yaml")
        return

    text = metadata_path.read_text(encoding="utf-8")
    for key in ("display_name", "short_description", "default_prompt"):
        if re.search(rf"^\s*{key}\s*:", text, re.MULTILINE) is None:
            errors.append(f"{metadata_path}: missing interface.{key}")

    short_match = re.search(r"short_description:\s*['\"]?(.*?)['\"]?\s*$", text, re.MULTILINE)
    if short_match:
        short_description = short_match.group(1)
        if not 25 <= len(short_description) <= 64:
            errors.append(
                f"{metadata_path}: short_description must be 25-64 characters"
            )

    prompt_match = re.search(r"default_prompt:\s*['\"]?(.*?)['\"]?\s*$", text, re.MULTILINE)
    if prompt_match and f"${skill_name}" not in prompt_match.group(1):
        errors.append(f"{metadata_path}: default_prompt must mention ${skill_name}")


def iter_public_files(root: Path) -> list[Path]:
    ignored_parts = {".git", "__pycache__"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_parts for part in path.parts):
            continue
        files.append(path)
    return files


def validate_public_scrub(root: Path, errors: list[str]) -> None:
    for path in iter_public_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in PUBLIC_SCRUB_PATTERNS:
            for match in pattern.finditer(text):
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{path}:{line}: possible {label}")


def validate_skill(skill_dir: Path, errors: list[str]) -> None:
    skill_name = skill_dir.name
    if not SKILL_NAME.match(skill_name):
        errors.append(f"{skill_dir}: invalid skill folder name")

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill_dir}: missing SKILL.md")
        return

    try:
        frontmatter = parse_frontmatter(skill_md)
    except ValueError as exc:
        errors.append(f"{skill_md}: {exc}")
        return

    if frontmatter.get("name") != skill_name:
        errors.append(f"{skill_md}: frontmatter name must equal folder name")
    if not frontmatter.get("description"):
        errors.append(f"{skill_md}: missing frontmatter description")
    validate_agent_metadata(skill_dir, skill_name, errors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".", type=Path)
    args = parser.parse_args()

    root = args.repo.resolve()
    skills_root = root / "skills"
    errors: list[str] = []

    if not skills_root.exists():
        errors.append(f"{skills_root}: missing skills directory")
    else:
        for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
            validate_skill(skill_dir, errors)

    validate_public_scrub(root, errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"ok: validated skills in {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
