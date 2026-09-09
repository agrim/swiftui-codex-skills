# Task-to-skill examples

## A search screen shows an older result

Read `swift-concurrency`, then `apple-networking` if transport is involved. Trace request identity through success, failure, cancellation, and loading cleanup. Keep old completion from mutating a newer request's state. Use a controlled completion-order test, not a sleep that happens to pass.

## A sheet creates a record even after Cancel

Read `swiftui-state-architecture` and `apple-data-persistence`. Identify whether the editor mutates a live persistence object or owns a value draft. Save only at the promised commit boundary; verify cancellation, failed save, duplicate submission, and relaunch.

## A screen feels custom-built rather than native

Start with `apple-swiftui-native-apps`, then `swiftui-controls-input`, `swiftui-design-system`, and `swiftui-accessibility` as needed. Fix action semantics and hierarchy before recoloring. Custom styles are allowed; they still need a full appearance, disabled, focus, and accessibility contract. Prove visual claims with rendered output.

## A phone layout is awkward on Mac or iPad

Read `swiftui-platform-adaptation`, `swiftui-layout`, and `swiftui-navigation`. Separate shared domain state from per-window selection and presentation. Use platform scenes, commands, keyboard behavior, and adaptive navigation rather than scaling phone geometry.

## A widget compiles but does not stay current

Read `apple-system-experiences`, `apple-project-governance`, and `apple-device-validation`. Verify embedding, registration, shared projection, timeline generation, host rendering, delayed updates, and stale state. Do not promise an exact refresh cadence that the system does not guarantee.

## A HealthKit permission label says “denied” when no samples appear

Read `apple-privacy-system-integrations` and `apple-system-experiences`. Check the exact authorization contract: absence of query results is not a read-permission signal. Preserve empty/unknown/unavailable distinctions and test truthful UI rather than inferring protected state.

## A refactor reduces lines but slows scrolling

Read `apple-performance-cleanup` and `swiftui-testing`. Compare the same workload and configuration, inspect invalidation and allocation behavior, and preserve unique regression tests. Fewer lines are not a performance measurement.

## A macOS app runs locally but fails after download

Read `macos-productization`. Inspect the exact packaged artifact, nested code, signing identity, entitlements, notarization, stapling, Gatekeeper, and installed launch. Do not “fix” it by disabling system security or blanket re-signing.

## “Make the app ready for the App Store”

Start with `apple-app-store-readiness`. Separate auditing and preparation from authorized upload, submission, and release. Bind the real product promise, privacy disclosures, screenshots, reviewer access, and device evidence to one exact candidate.

All skill identifiers above are indexed in the [coverage map](coverage.md). They are names, not model-specific commands.
