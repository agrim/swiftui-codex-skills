# Contributing

Improve a demonstrated decision or failure mode, not the adjective count. Read [AGENTS.md](AGENTS.md) and the relevant current skill first.

## A useful change

State the triggering task, failure scenario, scoped correction, primary-source basis, compatibility implications, and verification. Include a counterexample to an overly broad rule. For example, “prefer Button for an action” should not become “ban every tap gesture,” and “keep expensive work off a UI update path” should not become “use detached tasks everywhere.”

An entry point should tell a human or agent what to inspect, decide, do, and prove. Put decision tables and examples in the playbook. Avoid copying the same paragraphs into every skill. Add a new skill only when it has a distinct trigger and owner; expand a reference when the work belongs to an existing owner.

## Rule taxonomy

| Kind | Evidence and wording |
| --- | --- |
| API contract | Link the exact symbol/article and state applicable platform/compiler constraints |
| Apple HIG guidance | Link the relevant HIG topic; preserve its context rather than claiming legal obligation |
| Engineering recommendation | Explain the failure it prevents and when an alternative is appropriate |
| Repository convention | Label it as local; do not universalize a folder layout or architecture preference |
| Unverified hypothesis | Name the experiment needed; do not write it as a proven fix |

Stable IDs identify the decision contract. Preserve IDs for clarified rules; document materially changed meaning. Examples should include real error, cancellation, identity, and lifecycle behavior where relevant, not only the happy path.

## Source review

Add precise Apple or Swift primary sources to `sources.json` and the skill's catalog record. Link them in the local playbook. Use `content-reviewed` only after inspecting relevant page content; use `reference-only` for discovery routes. A framework landing page is not evidence for every detailed API claim. Never auto-refresh review dates from HTTP status.

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

Add regression tests for tooling changes, including malformed input and false-positive cases. Update the behavioral scenarios for a new important failure mode. The [evaluation protocol](docs/evaluation.md) requires real model outputs to claim behavioral results; passing phrase-routing fixtures is not an agent benchmark.

Keep changes reviewable. No live service calls, account writes, private credentials, or external dependencies are required for ordinary library checks. Do not add unsafe automation that gives untrusted pull-request code write tokens or publishing credentials.

## Review rubric

A reviewer should be able to answer: Does it solve a real task? Is its scope clear? Is the advice technically defensible? Is the source specific? Is the failure testable? Is the common path short? Does it work without a particular host? Are unavailable proof and coverage limits explicit?

Reject invented API names, arbitrary “always/never” rules, fake benchmarks, source links that do not support the claim, and duplicated vendor-specific versions of the same content. The owner must resolve licensing before accepting contributions under a new distribution license; do not assume one from the repository being public.
