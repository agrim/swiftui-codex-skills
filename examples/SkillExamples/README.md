# Executable examples

Swift 6 package with no third-party dependencies. `SkillExamplesCore` uses Foundation and Observation. `SkillExamplesUI` requires SwiftUI; `SkillExamplesPersistence` requires SwiftData. The Apple examples target macOS 14 / iOS 17 or newer. These are example requirements, not universal minimums for using the skills.

## Contracts and limits

| Example | Executed contract | What it does not establish |
| --- | --- | --- |
| `LatestRequestState` | Request tokens reject stale and duplicate terminal paths | Resource cancellation or durable side effects |
| `SearchModel` | Main-actor state ownership and guarded async service completion | Actual network, debounce, account authentication, or pagination |
| `SearchExample` | Uses the tested model from a view-bound task; invalidates on disappearance | Rendered UI, focus, VoiceOver, or SwiftUI scheduler tests |
| `NoteDraft` / `NoteRoute` | Value draft validation and stable route identity | On-disk persistence or navigation restoration |
| `DraftNoteStore` | Explicit local creation; isolated writer rollback on failure | CloudKit, migrations, crash recovery, general idempotency, or an asynchronous storage architecture |

`SearchIntegrationTests` start real tasks and use a controlled actor service with registration handshakes. They finish requests out of order and deliberately ignore cancellation in the fake service. No sleep establishes test ordering. The suite's time limit is only a deadlock watchdog. The UI and tests use the same model implementation, not duplicated algorithms. Keep the injected service stable for a view's identity; account replacement must invalidate the existing model and update the service/context ownership deliberately.

`DraftNoteStoreTests` run against real SwiftData with a fresh in-memory container per test. They cover untouched/canceled value drafts, explicit save through a fresh context, validation failure, injected pre-save failure, preservation of unrelated main-context work, and retry after a proven pre-save failure. They do not claim a disk-full or partial-write simulation. Repeating a successful `create` intentionally creates another record; external operations need their own durable identity and reconciliation.

The synchronous store is deliberately tiny. Do not put expensive storage work into a SwiftUI button callback merely because this example has a synchronous `create` method. Choose actor ownership and an asynchronous commit state for larger workloads. `titles()` is an unbounded teaching query, not a pagination strategy. A creation context isolated from the main context may also require deliberate UI query refresh/reconciliation in a real app.

`DraftEditor` and `DraftNavigationExample` remain in-memory UI examples. Their cancel/save callbacks are separate from the SwiftData store tests; connecting them is not evidence of tested disk durability.

## Run

```bash
swift test --package-path examples/SkillExamples
swift test --package-path examples/SkillExamples --filter SearchIntegrationTests
swift build --package-path examples/SkillExamples --target SkillExamplesUI
swift build --package-path examples/SkillExamples --target SkillExamplesPersistence
```

On Linux, the SwiftUI and SwiftData sections are excluded. A working Linux Swift/Observation runtime can exercise the core/model tests but cannot establish Apple framework compilation or persistence behavior. Report toolchain/linker failures separately from failed assertions; do not bypass runtime validation to get a green test command.

The Apple CI lane runs all suites on macOS, repeats async interleavings five times, and compiles both UI and persistence targets against the installed iOS SDK. It does not run iOS tests, render screens, inspect VoiceOver, or use physical devices. Inspect the exact candidate's CI logs before claiming any check passed.
