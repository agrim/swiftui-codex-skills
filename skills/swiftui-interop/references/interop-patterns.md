# UIKit and AppKit interoperability: playbook

## When interop is appropriate

A required text-system feature, specialized camera/media surface, platform panel, responder-chain behavior, or window capability may justify UIKit/AppKit. The existence of an import is not a defect. Prefer supported public APIs and a small adapter rather than private view-hierarchy introspection. Revisit the adapter when a newer SwiftUI API genuinely meets its contract, not just because it is newer.

## Lifecycle ownership

| Phase | Responsibility |
| --- | --- |
| Creation | Construct the platform view/controller, install delegate/coordinator, configure durable resources |
| Update | Apply current SwiftUI inputs idempotently without restarting unchanged work |
| Callback | Translate actual platform user events into the current binding or command |
| Teardown | Detach observers/delegates and stop resources owned by the adapter |

Do not start a new capture session, observer, or request on every update. Compare meaningful configuration before expensive reconfiguration. Make resource shutdown idempotent, and account for asynchronous callbacks that may arrive after removal.

## Coordinator correctness

A coordinator can outlive a particular value of the representable struct. Keep its inputs and callbacks current during updates instead of storing an initializer snapshot forever. Avoid retaining obsolete bindings or model instances. If assigning a platform value triggers its delegate, distinguish a model-driven update from a genuine user edit so the adapter does not feed back indefinitely.

Deferring every callback with arbitrary asynchronous dispatch can hide reentrancy without fixing ownership. Determine when the framework permits mutation, capture the intended value, and use a deliberate boundary. Do not mutate observed state during view update merely to synchronize two redundant sources of truth.

## Sizing and focus

Honor the proposed size and intrinsic sizing behavior. Use supported sizing hooks where available; do not compute every platform view from the global screen. Test empty content, large text, constrained width, and repeated resize. A hosting controller needs correct containment and lifecycle forwarding when embedded in another controller.

Text bridges must preserve selection, marked/composing text, undo, focus, and accessibility. Replacing all text on every update can break input methods and move the cursor. Window bridges should target the intended window, not whichever happens to be globally key at a particular instant.

## Concurrency and teardown

Keep UIKit/AppKit UI operations on their documented actor/thread boundary. A background callback must cross into the UI owner safely, with generation checks if the adapter may have been replaced. Stop platform resources independently of hiding their SwiftUI wrapper. Remove tokens and notifications from the same owner that created them; avoid cycles through delegates and closures.

## Regression probes

Create the view, update one property, trigger a user event, remove it, recreate it, and deliver a delayed callback from the prior lifecycle. Assert that only the current model changes and that resource counts return to baseline. Exercise keyboard/assistive focus and resize. A single successful render proves neither lifecycle cleanup nor responder correctness.

## Sources

- [uikit](https://developer.apple.com/documentation/swiftui/uikit-integration) — SwiftUI UIKit integration.
- [appkit](https://developer.apple.com/documentation/swiftui/appkit-integration) — SwiftUI AppKit integration.
- [concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) — The Swift Programming Language: Concurrency.
- [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) — HIG: Accessibility.
- [view-controller-bridge](https://developer.apple.com/documentation/SwiftUI/uiviewcontrollerrepresentable) — UIViewControllerRepresentable.
- [appkit-view-bridge](https://developer.apple.com/documentation/SwiftUI/NSViewRepresentable/) — NSViewRepresentable.
