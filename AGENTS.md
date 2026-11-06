# Repository maintenance contract

Maintain a provider-neutral, source-linked skill library.

## Authoring

- Keep each skill self-contained in `skills/<id>/` with `SKILL.md` and local `references/`. Preserve published identifiers unless a documented migration is intended.
- Use the documented scalar frontmatter profile: unquoted `name`, JSON-quoted single-line `description`. Both are valid YAML; advanced YAML is deliberately outside this repository profile.
- Keep entry points within 650 words and playbooks within 1,800 words. Use Inputs, Rules, Workflow, Verify, Output, References. Give rules stable IDs.
- Distinguish Apple requirements, documented API behavior, repository conventions, and recommendations. Do not turn one app's rules into universal requirements.
- Link precise primary sources. Record reviewed content honestly; do not upgrade discovery links or review dates after an HTTP-only check. Verify availability in the current SDK before adding version-specific examples.
- Keep core content free of vendor invocation syntax or mandatory plugins. Optional host adapters may live under `agents/`; they do not own engineering rules.
- Update `catalog.json` and `sources.json` with the content, then regenerate docs. Do not hand-edit generated coverage/source tables.
- Keep secrets, private device identifiers, machine paths, screenshots, and session artifacts out of published files. Do not choose or change the owner's license silently.

## Verification

For skill, catalog, source, or tooling changes, run `python3 scripts/validate_skills.py .`, `python3 scripts/skillctl.py docs --check`, and `python3 -m unittest discover -s tests -v`. Run `swift test --package-path examples/SkillExamples` for example changes. Instruction-only edits need link/contract review and `git diff --check`. Apple-only compilation requires an Apple SDK; Linux success is not SwiftUI compilation.

## Cloud setup

See [.codex/cloud/README.md](.codex/cloud/README.md) for dependency-free Linux maintenance and the Apple compilation boundary.
