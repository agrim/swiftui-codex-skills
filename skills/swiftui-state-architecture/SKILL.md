---
name: swiftui-state-architecture
description: "Fix SwiftUI state ownership, Observation, bindings, environment injection, row identity and scene lifetime."
---

# State, identity, and architecture

## Inputs

Identify each value’s creator, readers, writers, required lifetime and supported OS versions.

## Rules

- **STATE-001 — Choose one owner.** Own mutable state for the shortest sufficient lifetime. Pass values to readers, bindings to editors and services to callers.
- **STATE-002 — Match the wrapper to ownership.** For a view-owned `@Observable` model, use `@State` on supported targets. For `ObservableObject`, use `@StateObject` to own or `@ObservedObject` to observe a passed-in model.
- **STATE-003 — Keep record identity stable.** Key editable rows by domain IDs that survive reordering.
- **STATE-004 — Keep rendering pure.** Move service starts, persistence writes and expensive work out of `body` and repeatedly evaluated initializers.
- **STATE-005 — Isolate edits.** Keep discardable drafts separate from durable records until Save. Choose actor isolation independently of observation.

## Workflow

1. Trace one edit from control to owner. Choose which state should survive navigation, dismissal or relaunch.
2. Replace independent flags with an enum when they permit impossible combinations.
3. After an asynchronous row save, resolve the current record by ID. Apply the reply only if the edit is still current.

## Verify

- STATE-001: For scene-owned selection, open a second window. Its selection changes independently.
- STATE-002: Recompute the parent of an owned model. Its identity and in-progress draft survive.
- STATE-003: Reorder, delete or re-edit a row before its save completes. The reply preserves newer edits, their pending state and any deletion.
- STATE-005: Cancel an editor and check that storage is unchanged. Save and reopen to verify the committed value.

## Output

Identify the owner, wrapper, compatibility constraints, and results of the affected lifecycle checks.

## References

- [Choose owners, wrappers and scene scope](references/state-patterns.md)
- [Observation, bindings and asynchronous row edits](references/observation-and-bindings.md)
