# Behavior tests, previews, and evidence: playbook

## Evidence ladder

| Claim | Minimum relevant evidence |
| --- | --- |
| Parser or reducer behavior | Executed deterministic unit test |
| SwiftUI API compiles | Build for the affected Apple target/minimum |
| State survives a save/relaunch | Disk-backed integration test or installed runtime journey |
| Button performs the action | UI interaction or equivalent behavioral integration |
| Layout does not truncate | Rendered inspection at risky sizes and states |
| VoiceOver journey works | Assistive-technology interaction plus audits where supported |
| Sensor or paired-device behavior | Relevant physical-device evidence |

Evidence levels are complementary, not a single substitute-for-everything score.

## Framework choice

Swift Testing provides expressive expectations, parameterized tests, and concurrency integration. Existing XCTest tests can remain and migrate incrementally. Keep UI automation in the supported XCTest/XCUI toolchain rather than assuming every testing framework provides the same UI capabilities. Inspect the installed Xcode version and current API availability before adopting a new test API.

Swift Testing normally runs tests in parallel. A serialized suite does not serialize unrelated peers globally. Prefer independent clients, temporary directories, isolated in-memory stores, and per-test data. Serial execution is a deliberate escape hatch for a real shared resource, not a cure for hidden fixture ownership.

## Deterministic asynchronous tests

Use a controlled fake that acknowledges registration before the test completes a request. Test A-start, B-start, B-complete, A-complete; repeat for failures and cancellation. Inject a clock for debounce/backoff and advance it explicitly. Avoid assuming a fixed sleep means the UI rendered, a network request began, or cancellation finished.

Use timeouts as safety limits, not synchronization. Teardown must cancel tasks, finish streams, restore injected dependencies, and remove temporary storage even after an assertion fails.

## Previews and snapshots

Build a fixture matrix: loading, empty, content, error, denied, stale, very long text, large text, and relevant platform widths. A preview should not request permissions, access live credentials, mutate the user's database, or start sensors. Preview-friendly dependency injection often exposes architectural problems early.

Snapshot baselines must record appearance, locale, text size, OS/runtime, content, and rendering size. An updated snapshot requires a meaningful visual review; do not bless every difference just to restore green CI. Pixel differences can be infrastructure noise, but classification needs evidence.

## UI automation

Use stable accessibility identifiers for test selection without replacing human-facing labels. Wait for observable UI state rather than sleeping. Exercise actual controls, errors, cancellation, and relaunch. Inject deterministic launch fixtures through an explicit test configuration, and keep those controls unavailable in production builds.

Automated accessibility audits find useful classes of issues. Pair them with screen-reader and keyboard journeys; audit success does not demonstrate that a custom workflow is comprehensible or operable.

## Regression value

A test should fail if the intended bug returns. For a save/cancel defect, assert the store contents, not that the source contains `Button("Cancel")`. Source-contract tests are appropriate for narrow architectural prohibitions or generated artifacts, but do not prove application behavior. Preserve unique scenarios during cleanup rather than reducing test count for cosmetic metrics.

## Handoff

Report which exact source state was tested and which result belongs to source inspection, unit/integration, UI, visual, or hardware validation. Keep raw failing output until it is classified. If Apple tooling is unavailable, run portable checks and clearly list Apple build/runtime gates as unverified.

## Regression probes from visual review

Turn an observed UI defect into the smallest relevant executable probe. For a bottom-field editor, enter text, reveal the actual keyboard, reach the commit action, and recover from invalid input at a risky size. A source assertion that a safe-area modifier exists does not exercise this contract. For repeated surfaces, compare the same entity and state across both contexts, including the shared component's affected appearances.

Keep screenshot fixtures labeled as staged or real. A forced sensor count or injected save error demonstrates that presentation state, not a successful sensor or storage operation. When an interaction test passes but a unit runner stalls, report both outcomes; do not silently substitute the former for the latter. Stop and classify a bounded stalled run before adding more retries.

## Sources

- [testing](https://developer.apple.com/xcode/swift-testing/) — Swift Testing.
- [test-parallel](https://developer.apple.com/documentation/Testing/Parallelization) — Swift Testing parallelization.
- [ui-audit](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityauditissue) — XCUI accessibility audits.
- [xcode](https://developer.apple.com/documentation/xcode) — Xcode documentation.
