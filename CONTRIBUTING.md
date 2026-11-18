# Contributing

Improve a demonstrated decision or failure mode, not the adjective count. Read [AGENTS.md](AGENTS.md) and the relevant current skill first.

## A useful change

State the triggering task, failure scenario, scoped correction, primary-source basis, compatibility implications, and verification. Include a counterexample to an overly broad rule. For example, “prefer Button for an action” should not become “ban every tap gesture,” and “keep expensive work off a UI update path” should not become “use detached tasks everywhere.”

Assume readers can look up framework mechanics. Write the decision they still face and a check that distinguishes a correct result from a plausible failure. Leave API tutorials, HIG summaries and official documentation links out of installed skill folders. Include a platform fact only when it changes a decision, such as which editor owns a draft after its record changes.

Keep the decision in the entry point and its worked case in one playbook. Introduce a new skill only for a distinct task and owner.

## Write a checkable entry point

Give the guide a title that names the job. Under it, explain when someone would use it and what should happen. A reader who skips the YAML should still understand the purpose. Use one recognizable example to carry a decision through to an observable result.

Use four level-two headings in order.

| Heading | What belongs here |
| --- | --- |
| Start here | One paragraph naming the first action or evidence to gather. |
| How to proceed | Numbered steps in the order a person would do them. Give each a short, bold action title and explain how to make the decision. |
| Check the result | Bullets describing an input or failure and the outcome the reader should observe. |
| What to report | One paragraph naming the result to communicate, followed by a blank line and links to the local playbooks. |

Put the stable rule ID at the end of its step in an HTML comment. End each check with the IDs it exercises. This keeps the guide readable on GitHub and lets the CLI export those relationships from the same Markdown. Here the input is valid HTTP data for the wrong record.

```markdown
1. **Check the record before replacing the cache.** If the server returns the wrong record, keep the usable cached copy. <!-- NET-001 -->

- Return another record's ID during refresh. The app reports a refresh error and still shows the cached record. <!-- NET-001 -->
```

Keep each step, check and playbook link on one line. Preview the structured version with `python3 scripts/skillctl.py contract <skill-id>`.

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
