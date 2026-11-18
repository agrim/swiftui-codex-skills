# Verification claims and remaining work

Use this matrix to plan evidence, not as a record that checks have run. Individual commits and CI runs supply the results.

| Layer | Mechanism | What it does not establish |
| --- | --- | --- |
| Skill contracts | Metadata, budget, rule ID, source, local-link, and portability validator | That all guidance is correct or followed by a model |
| Source provenance | Offline ledger validation and generated map consistency | That a human review assertion independently proves source content |
| Task routing | App-task phrases and documentation-only no-match cases | Semantic retrieval quality or comparative model effectiveness |
| Build helper | Injected runner tests, malformed input, preserved failures, descriptive statistics | A real app's build speed, Xcode behavior, or complete process sandboxing |
| Swift domain examples | Actual Swift Testing execution | Apple-only framework behavior when executed on a non-Apple host |
| SwiftUI and persistence | Apple SDK compilation, in-memory persistence tests, and a synthetic V1 → V2 disk rename with a second reopen | Rendered layout, assistive interaction, stores produced by released binaries, or live cloud services |
| New deep-link parser | Canonical origin/path and negative-input tests | Authorization, associated-domain deployment, or navigation presentation |
| Installation | Existing preflight and receipt/status regression suites | Atomic filesystem transactions or updates to a user's installation |

See the [evaluation protocol](evaluation.md) for the offline workflow and scrolling-trace pilots. Each records the inputs, scope, and outcomes of the performed runs. The scenarios below specify additional evidence to collect.

## Current app scenarios

The [six scenario contracts](../evals/scenarios.json) cover a first feature, a window transition, independent edits, a saved shortcut, a scroll hitch and an in-place upgrade. They specify the evidence to collect. Earlier pilot results apply to the revisions used in those runs.
