# State, identity, and architecture: playbook

## Ownership decision table

| Need | Observation-era choice | Legacy or alternative |
| --- | --- | --- |
| View-owned simple value | `@State` | Same |
| Child edits a parent value | `@Binding` | Same |
| View owns an observable reference | `@State` with `@Observable` | `@StateObject` with `ObservableObject` |
| Child reads an observable reference | Ordinary stored property | `@ObservedObject` |
| Child needs projected bindings | `@Bindable` | `@ObservedObject` projections |
| Deliberately shared dependency | Explicit injection; typed environment where appropriate | `@EnvironmentObject` with provider |
| Small preference | `@AppStorage` | Not a database or credential store |
| Restorable per-scene UI value | `@SceneStorage` where supported | Scene-owned state and explicit restoration |

Observation integration begins at iOS/iPadOS/tvOS 17, macOS 14, and watchOS 10; inspect the exact target for visionOS and newer additions. Its tracking follows properties read by a view. It does not make a reference thread-safe, turn nested plain reference mutations into observation, or make a copied value a live binding. [observation] and [model-data] are the authoritative migration starting points.

## Work from identities and lifetimes

A SwiftUI view value can be recreated while its state storage persists. `@State` initialization seeds storage for that identity; changing an initializer argument does not necessarily reset an existing state value. Decide whether new input updates the same feature or represents a different feature identity. Do not use `.id(...)` as a universal refresh mechanism: intentionally changing identity also resets local state, focus, and associated tasks.

For mutable rows, persist the ID when creating the record. Indices are reasonable for genuinely static position-based content, not a safe default for editable, reordered records. Test deleting the selected item and inserting before an editing row. Preserve semantic row identity during loading by changing status/accessories when that avoids losing focus; do not freeze the entire hierarchy if content genuinely changes.

## Avoid accidental global state

Share authentication and deliberate app services at app scope; keep selections and edit drafts at scene or feature scope. Opening a second window must not silently replace the first window's route or draft. A type-based environment dependency needs a provider in previews, tests, sheets, and new scenes. Prefer explicit parameters when they make required dependencies clearer.

Do not persist every UI flag. Durable data, scene restoration, cached data, and transient presentation are separate contracts. Restoring a route must revalidate identifiers against current data and authorization.

## Model behavior before naming an architecture

Use a value type for a draft, a small enum for loading or workflow phases, and a service boundary for I/O. Add an observable coordinator only when a feature needs it. MVVM, reducers, or another established repository pattern can all work; a view model per view is not a platform requirement. A single giant model can be as harmful as needless layers.

A creation editor receives a value draft and a commit action. Opening, typing, and cancelling must not insert a placeholder in the store. Keep failed saves visible with the draft intact. For existing-record edits, specify the conflict policy if the source changes while the editor is open. A child binding should mutate only the intended property, not reconstruct unrelated state.

## Regression probes

Recompute the parent without changing record identity; assert the draft survives. Reorder rows; assert editing follows the same record. Open two scenes; assert independent selection. Replace an injected dependency deliberately; assert no stale callbacks from the prior instance. Cancel an editor; assert no durable mutation. Confirm a save twice; assert the domain command's duplication policy. These tests evaluate observable behavior rather than source spelling.

## Sources

- [observation](https://developer.apple.com/documentation/SwiftUI/Migrating-from-the-observable-object-protocol-to-the-observable-macro) — Migrating to Observation.
- [model-data](https://developer.apple.com/documentation/SwiftUI/Managing-model-data-in-your-app) — Managing model data.
- [navigation](https://developer.apple.com/documentation/swiftui/understanding-the-navigation-stack) — Understanding the navigation stack.
