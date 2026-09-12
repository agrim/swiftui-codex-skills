# Repository maintenance contract

Maintain a provider-neutral, source-linked skill library. Read the current files before changing them. Preserve user edits and the requested action boundary.

## Authoring

- Keep each skill self-contained in `skills/<id>/` with `SKILL.md` and local `references/`. Preserve published identifiers unless a documented migration is intended.
- Use the documented scalar frontmatter profile: unquoted `name`, JSON-quoted single-line `description`. Both are valid YAML; advanced YAML is deliberately outside this repository profile.
- Keep entry points within 650 words and playbooks within 1,800 words. Use Inputs, Rules, Workflow, Verify, Output, References. Give rules stable IDs.
- Make rules scoped, actionable, and testable. Distinguish Apple requirements, documented API behavior, repository conventions, and engineering recommendations. Avoid universal bans derived from one app.
- Link precise primary sources. Record reviewed content honestly; do not upgrade discovery links or review dates after an HTTP-only check. Verify availability in the current SDK before adding version-specific examples.
- Keep core content free of vendor invocation syntax or mandatory plugins. Optional host adapters may live under `agents/`; they do not own engineering rules.
- Update `catalog.json` and `sources.json` with the content, then regenerate docs. Do not hand-edit generated coverage/source tables.
- Keep community/plugin review provenance in `upstreams.json`, not the Apple authority registry. Preserve explicit access limits and source receipts; do not infer reuse permission. Run `python3 scripts/upstream_audit.py --check` after changes.
- Keep secrets, private device identifiers, machine paths, screenshots, and session artifacts out of published files. Do not choose or change the owner's license silently.

## Verification

Run `python3 scripts/validate_skills.py .`, `python3 scripts/skillctl.py docs --check`, and `python3 -m unittest discover -s tests -v`. Run `swift test --package-path examples/SkillExamples` for example changes. Apple-only compilation requires an Apple SDK; Linux success does not prove SwiftUI compilation.

Review the diff and run whitespace checks. Report exact commands, failures, and blocked Apple/device gates. Never fabricate screenshots, benchmarks, cross-model evaluation, or CI results. Keep external upload, submission, publication, destructive changes, and account administration within explicit authority.
