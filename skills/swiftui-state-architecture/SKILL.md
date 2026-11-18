---
name: swiftui-state-architecture
description: "Fix SwiftUI state ownership, Observation, bindings, environment injection, row identity and scene lifetime."
---

# SwiftUI state and identity

## Inputs

Trace creators, readers, writers, lifetimes and supported OS versions.

## Rules

- **STATE-001 — Ownership.** Choose the shortest sufficient lifetime. Pass values to readers, bindings to editors and services to callers.
- **STATE-002 — Wrappers.** Own an `@Observable` model with `@State` where supported. For `ObservableObject`, use `@StateObject` for ownership or `@ObservedObject` for an injected model.
- **STATE-003 — Identity.** Key editable rows by stable domain ID.
- **STATE-004 — Rendering.** Keep service starts, writes and expensive work outside `body` and repeated initialization.
- **STATE-005 — Drafts.** Keep discardable drafts separate from saved records. Choose actor isolation independently of observation.

## Workflow

1. Trace an edit to its owner across dismissal, navigation or relaunch.
2. Use an enum when flags permit impossible combinations.
3. After suspension, resolve the row by ID and check the edit is current.

## Verify

- STATE-001: Select in one window. The other keeps its scene-owned selection.
- STATE-002, STATE-004: Recompute the parent. Its model and draft survive without repeated I/O or expensive initialization.
- STATE-003: Reorder, delete or re-edit during save. A late reply preserves deletion, newer edits and pending state.
- STATE-005: Cancel preserves storage. Save survives reopening.

## Output

Give owner, wrapper, compatibility constraints and lifecycle results.

## References

- [Owners, wrappers and scenes](references/state-patterns.md)
- [Observation, bindings and async edits](references/observation-and-bindings.md)
