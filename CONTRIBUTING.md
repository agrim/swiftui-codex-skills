# Contributing

Improve a demonstrated decision or failure mode, not the adjective count. Read [AGENTS.md](AGENTS.md) and the relevant current skill first.

## A useful change

Start with a real SwiftUI, Xcode or Apple service task. Identify the source to inspect, the choice that affects the app, and how a developer can see the result. An unreadable button calls for tracing its role, tint and parent environment. An empty widget store calls for comparing the app and extension’s signed entitlements before changing the view.

Keep the entry short. Put specialized cases and tool invocations in local references. Look up framework mechanics as needed and keep official source links in the maintenance catalog. The [original skills and their migration](docs/skill-migration.md) show where existing guidance belongs.

## Write a checkable entry point

Title the guide with the job it helps a person finish. Open with the situation and the result they care about. Use two headings.

- **Design choices** contains numbered decisions with a short bold action and enough context to choose. Tie advice to the conditions that warrant it.
- **Try it** opens with the acceptance goal, then gives observable checks as bullets. End with a separate group of links to local cases.

Keep the machine-readable IDs in trailing HTML comments. Cite each decision from a check. Use a worked case only when it adds a choice, consequence or counterexample that the entry point could not show as clearly.

```markdown
1. **Give each window its own selection.** Share saved notes across windows. Let each window choose which note to read. <!-- ADAPT-001 -->

- Open different notes in two windows. Change the first window’s selection and check that the second keeps its note. <!-- ADAPT-001 -->
```

Keep each decision, check and case link on one line. Preview the JSON with `python3 scripts/skillctl.py contract <skill-id>`.

## Rule taxonomy

| Kind | Evidence and wording |
| --- | --- |
| API contract | Name the symbol or target constraint that changes the decision |
| Apple HIG guidance | Tie the design choice to the affected task, input or setting |
| Engineering recommendation | Explain the failure it prevents and when an alternative is appropriate |
| Repository convention | Label it as local; do not universalize a folder layout or architecture preference |
| Unverified hypothesis | Name the experiment needed; do not write it as a proven fix |

Stable IDs identify the decision contract. Preserve IDs for clarified rules; document materially changed meaning. Examples should include real error, cancellation, identity, and lifecycle behavior where relevant, not only the happy path.

## Source review

Record reviewed Apple or Swift pages in `sources.json` and their IDs in the skill’s `catalog.json` entry. An original workflow can have an empty `sources` list. Use `content-reviewed` for content actually inspected and `reference-only` for discovery. Record the review date when the content is read.

For new or beta APIs, distinguish SDK version, language mode, deployment minimum, runtime availability, and fallback behavior. Preserve older supported targets unless changing them is explicitly part of the work. Recheck legal/store/privacy-sensitive requirements at use time rather than freezing an unconditional rule.

## Upstream integration

Record community and plugin provenance separately in `upstreams.json`; keep platform authority in `sources.json`. State the exact read file, blob receipt, scope, and local mapping. Directory discovery, landing-page access, and entry-point review are different statuses. Do not turn a review into permission to copy third-party code. Inspect license terms and preserve notices before any future vendoring. Regenerate `docs/ecosystem.md` with `python3 scripts/upstream_audit.py --write`.

## Checks and evaluation

```bash
python3 scripts/skillctl.py docs
python3 scripts/validate_skills.py .
python3 scripts/upstream_audit.py --check
python3 -m unittest discover -s tests -v
swift test --package-path examples/SkillExamples
```

For tooling changes, exercise the failure through the command or API people use. Extend an existing test when it already covers that workflow. The validator checks every skill’s metadata, budgets, links, and catalog entry. Update the behavioral scenarios for a new important failure mode. The [evaluation protocol](docs/evaluation.md) requires real model outputs to claim behavioral results; passing phrase-routing fixtures is not an agent benchmark.

Keep changes reviewable. No live service calls, account writes, private credentials, or external dependencies are required for ordinary library checks. Do not add unsafe automation that gives untrusted pull-request code write tokens or publishing credentials.

## Review rubric

A reviewer should be able to answer: Does it solve a real task? Is its scope clear? Is the advice technically defensible? Is the source specific? Is the failure testable? Is the common path short? Does it work without a particular host? Are unavailable proof and coverage limits explicit?

Reject invented API names, arbitrary “always/never” rules, fake benchmarks, source links that do not support the claim, and duplicated vendor-specific versions of the same content. The owner must resolve licensing before accepting contributions under a new distribution license; do not assume one from the repository being public.
