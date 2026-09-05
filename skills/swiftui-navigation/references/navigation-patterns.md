# Navigation and presentation: playbook

## Container decisions

A `NavigationStack` represents a hierarchy. `NavigationSplitView` keeps selection and detail visible where space permits and adapts when it does not. A detail stack inside a split view can be valid; “never nest navigation containers” is too broad. A tab is a peer destination, not an action button. A sheet is a task boundary, not a replacement for every navigation destination.

Simple `NavigationLink` destination closures are appropriate when explicit programmatic state is unnecessary. Use value-based routing when deep linking, restoration, or coordinated navigation requires it. A homogeneous route enum array often gives clearer validation than an unrestricted heterogeneous `NavigationPath`; use the latter when its flexibility is actually needed.

## Route shape

A route such as `case detail(id: UUID)` holds identity rather than a live model, entire JSON payload, or destination view. Make routes `Hashable`; add `Codable` only when you need persistence. Restore through a versioned decoder and a validation step. The ability to decode yesterday's route does not prove the record still exists or that the current account can access it.

Place `navigationDestination` within the intended navigation container but outside a lazy row's transient creation scope. Avoid duplicate registrations for the same route type at accidental nested levels. Keep the path, selection, and presented editor at a stable owner rather than recreating them when loading completes.

## Modal task contract

Prefer `.sheet(item:)` when the existence of a specific item defines presentation. A single enum can represent mutually exclusive editor/inspector tasks. The editor owns a value draft; Save commits, Cancel discards, and interactive dismissal follows an explicit unsaved-changes policy. Do not disable dismissal globally to hide a persistence bug. A save failure must preserve the draft and present a recoverable error.

When one modal hands off to another, express the transition at a single owner and respect dismissal completion. Avoid arbitrary sleeps as presentation synchronization. Do not assume dismissing a SwiftUI view immediately completes every platform input teardown callback.

## External input and scene restoration

Parse URLs with structured URL APIs; reject unknown hosts/schemes, unsupported paths, malformed IDs, and unintended commands. Authentication may defer a destination, but must not silently execute a destructive action from a URL. Make repeated delivery idempotent where the same route could arrive through launch and running-app paths.

Store route state per scene when multiple windows can show different work. Decide how a request chooses an existing scene or creates a new one. Do not restore sensitive or unauthorized content just because the prior session had access. Provide a useful root or unavailable-detail state for deleted records.

## Test the transitions

Test list selection after reorder and deletion, detail visibility after collapsing a split view, navigation back after a deep link, reopening a cancelled editor, and independent histories in two windows. Verify tab-specific history when the product expects it. Keyboard shortcuts, focus restoration, and large-text layouts are part of navigation usability, not optional decoration.

Backport changes incrementally. On older supported targets, retain an appropriate legacy path or isolate the newer implementation behind availability checks. A new navigation API is useful only when it improves the actual journey without breaking the compatibility contract.

## Sources

- [navigation](https://developer.apple.com/documentation/swiftui/understanding-the-navigation-stack) — Understanding the navigation stack.
- [navigation-migration](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types) — Migrating to new navigation types.
- [windows](https://developer.apple.com/design/human-interface-guidelines/windows) — HIG: Windows.
