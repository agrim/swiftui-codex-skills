# Representable updates and teardown

A bridge should supply a missing platform capability, not replace a working semantic SwiftUI control by habit. Define ownership across make, update, coordinator callbacks, and dismantle. Keep the bridge small enough that the platform view's lifecycle is reviewable.

Construct the native view once for its identity and update only properties that changed. Unconditional assignments during every SwiftUI update can reset selection, text composition, scroll position, or delegates. Compare effective state before writing and distinguish user-originated callbacks from programmatic updates.

Avoid synchronous feedback loops that mutate SwiftUI state during an update. Route changes through an explicit callback contract and correct actor context. A deferred callback is not automatically safe: it must still belong to the current view/model generation after reuse or teardown.

## Lifecycle checklist

| Phase | Check |
| --- | --- |
| Make | Initial state, delegate ownership, no duplicate registrations |
| Update | Minimal mutations; preserve focused editing and identity |
| Callback | Validate current owner; avoid echoing programmatic changes |
| Dismantle | Remove observers, cancel work, release resources/delegates |
| Recreate | No inherited stale callback or duplicate subscription |

Use the coordinator for actual bridging responsibility, not as a parallel app model. Capture values carefully when the representable struct is recreated; ensure the coordinator receives current callbacks or dependencies.

Test repeated mount/update/unmount, navigation replacement, IME composition, focus changes, size changes, and delayed callbacks. Verify accessibility and keyboard semantics in the bridged control. A compiled representable and one screenshot do not establish correct teardown, resource release, or input behavior.

## Official sources

- [UIViewControllerRepresentable](https://developer.apple.com/documentation/SwiftUI/uiviewcontrollerrepresentable).
- [NSViewRepresentable](https://developer.apple.com/documentation/SwiftUI/NSViewRepresentable/).
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
- [HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).
