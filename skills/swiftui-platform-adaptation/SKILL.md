---
name: swiftui-platform-adaptation
description: "Adapt SwiftUI scenes, windows, focus, and input for iOS, iPadOS, macOS, watchOS, tvOS, or visionOS."
---

# Platform-native scenes and interaction

## Inputs

Targets, minimum OS, task, scenes, inputs and capabilities.

## Rules

- **PLAT-001 — Shared behavior.** Share commands when equivalent input should produce equivalent outcomes.
- **PLAT-002 — Ownership.** Decide which draft, path and selection a second window may share.
- **PLAT-003 — Native input.** Find the first unreachable action. Give it a route using the target’s input.
- **PLAT-004 — Availability.** Define the outcome when a target lacks a required capability.
- **PLAT-005 — Destinations.** Record build, input and lifecycle results per destination.

## Workflow

1. Trace a platform-specific control to its domain command.
2. On external reopen, identify the receiving scene and focus target.

## Verify

- PLAT-001, PLAT-004: Run a shared command on two targets with identical input. Compare outcomes. Exercise the fallback where its API is unavailable.
- PLAT-002: Switch or resize windows. Editing the selection by keyboard changes only its draft.
- PLAT-003: Read and activate the watchOS control. On tvOS reach it by remote and regain focus after dismissal.
- PLAT-003, PLAT-005: Use spatial input on visionOS. Verify task completion, exit scene and comfort on hardware.

## Output

Per target, report scene, input, command, fallback, build and runtime results.

## References

- [Tasks and native inputs](references/platform-patterns.md)
- [Reopening windows and restoring focus](references/scenes-and-focus.md)
