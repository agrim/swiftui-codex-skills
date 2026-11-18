---
name: swiftui-state-architecture
description: "Fix SwiftUI state ownership, Observation, bindings, environment injection, row identity and scene lifetime."
---

# SwiftUI state and identity

## Inputs

Trace creators, readers, writers, lifetimes and supported OS versions.

## Rules

- **STATE-001 — Ownership.** Place each mutable value at the narrowest scope that survives its required transitions. Give write access only to callers that need it.
- **STATE-002 — Wrappers.** Choose the wrapper for the actual owner and supported targets. A child receiving a replaceable model must follow its parent’s replacement.
- **STATE-003 — Identity.** Carry the same record ID from row selection through save completion.
- **STATE-004 — Rendering.** Tie service starts, writes and expensive setup to their owner so rendering cannot repeat them.
- **STATE-005 — Drafts.** Keep discardable drafts separate from saved records. Choose actor isolation independently of observation.

## Workflow

1. Trace an edit to its owner across dismissal, navigation or relaunch.
2. Use an enum when flags permit impossible combinations.
3. After suspension, resolve the row by ID and check the edit is current.

## Verify

- STATE-001: Select in one window. The other keeps its scene-owned selection.
- STATE-002, STATE-004: Recompute the parent. An owned model keeps its draft without repeated I/O or setup. An injected model follows deliberate replacement.
- STATE-003: Reorder, delete or re-edit during save. A late reply preserves deletion, newer edits and pending state.
- STATE-005: Cancel preserves storage. Save survives reopening.

## Output

Give owner, wrapper, compatibility constraints and lifecycle results.

## References

- [Owners, wrappers and scenes](references/state-patterns.md)
- [Observation, bindings and async edits](references/observation-and-bindings.md)
