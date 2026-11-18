# Debugger, simulator, and evidence integrity

Discover the current runtime, device, pairing state, tool defaults, and app identity. A prior session's destination or screenshot is not current-candidate evidence. Record build, install, launch, render, interaction, and hardware as separate steps with explicit status.

Automation should query semantic elements and accessibility identifiers when available. Coordinates are a fallback tied to a known screenshot, size, orientation, and app state; do not reuse them after layout changes. A screenshot tool returning a file does not prove the intended app or screen was captured—inspect it.

Test negative states deliberately: denied permissions, empty stores, offline data, larger text, reduced motion, interrupted lifecycle, and multiple windows where relevant. Keep fixtures synthetic and restore the harness rather than resetting user data. Installing an app is not permission to uninstall its existing copy.

## Artifact identity

Attach source/build, destination/runtime, timestamp, fixture, action sequence, and resulting state to evidence. If an artifact lacks those fields, mark the uncertainty instead of inferring it from a filename. A cropped screenshot can conceal a wrong navigation state; retain enough context for review.

Debuggers and hot reload can alter timing or preserve stale state. Repeat material lifecycle/performance checks from a clean launch without injected development helpers. Capture raw crash or install failure output before trying broad cleanup.

Differentiate tooling failure from app failure: missing SDK, unavailable simulator, pairing, provisioning, install service, launch crash, and post-launch store readiness require different next actions. Do not rewrite UI because screenshot capture timed out. Reconcile later successful receipts with earlier blockers and retain both histories without presenting superseded evidence as current.

## A visible control receives no tap

Query the control in the running app by its accessibility identifier. A matching element can exist in the hierarchy while it is offscreen or covered. For a row below the fold, scroll it into view and check `isHittable`. For a sheet covering the row, exercise the expected dismissal first, then query again. A timeout while the sheet is present is a different failure from a missing row.

Once the control is hittable, perform the action and assert its specific outcome, such as the saved value appearing in the detail view. If the automation session points to another simulator or bundle, correct the destination and repeat the check before changing hit targets in source. Save a frame for a layout question and the observed transition for a tap question.

## Official sources

- [Xcode documentation](https://developer.apple.com/documentation/xcode).
- [Swift Testing](https://developer.apple.com/xcode/swift-testing/).
- [XCUI accessibility audits](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityauditissue).
- [Distributing your app](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).
- [XCUIElement.isHittable](https://developer.apple.com/documentation/xcuiautomation/xcuielement/ishittable).
