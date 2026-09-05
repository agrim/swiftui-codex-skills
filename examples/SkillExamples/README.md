# Executable examples

This Swift 6 package has no external dependencies. `SkillExamplesCore` is portable; `SkillExamplesUI` compiles only where SwiftUI is available. The example UI targets macOS 14 / iOS 17 or newer. Those are example requirements, not universal minimums for using the skill library.

## What is demonstrated

`LatestRequestState` is a value-owned request state machine with unique request tokens. It rejects stale success, stale failure, stale cancellation, duplicate terminal completion, and completion after invalidation. Its owner must serialize mutation. Cancellation of the underlying work and durable side-effect delivery remain separate responsibilities.

`NoteDraft` demonstrates a true editable value and explicit validation before commit. `NoteRoute` carries stable identity. Tests verify copies, validation, and coding round trips, not disk persistence or automatic navigation restoration.

`SearchExample` uses view-bound `.task(id:)`, a caller-supplied async service, cancellation checks, and token-guarded terminal paths. It intentionally has no debounce, network client, account model, or pagination. Its demonstration results must have distinct strings; use stable entity IDs in a real domain.

`DraftEditor` and `DraftNavigationExample` show cancel-without-save, a narrow explicit save callback, typed routes, and missing-destination handling. Storage is deliberately in-memory. Do not substitute synchronous disk/network I/O into the save callback; introduce the appropriate async commit state for real persistence.

## Run

```bash
swift test --package-path examples/SkillExamples
swift build --package-path examples/SkillExamples --target SkillExamplesUI
```

On Linux the `canImport(SwiftUI)` sections are excluded. A successful Linux run proves only the portable core compilation/tests, not Apple UI compilation. The macOS CI lane builds the SwiftUI target with an Apple SDK and records the selected toolchain. Neither lane renders the views or establishes physical-device, VoiceOver, keyboard, layout, or store behavior.

Request-order tests drive the state machine directly and deterministically. They do not use sleeps, and they are not a claim that a transport service or SwiftUI scheduler was integration-tested. Add those tests in the actual app with a controlled service and the relevant runtime harness.
