---
name: swiftui-platform-adaptation
description: "Adapt SwiftUI scenes, windows, focus, and input for iOS, iPadOS, macOS, watchOS, tvOS, or visionOS."
---

# Platform-native scenes and interaction

## Inputs

Targets, minimum OS, task, scenes, inputs and capabilities.

## Rules

- **PLAT-001 — Shared behavior.** Share models and commands for equivalent tasks. Adapt presentation.
- **PLAT-002 — Ownership.** Match scene to task. Scope drafts, paths and selection per window.
- **PLAT-003 — Native input.** Expose essential actions to each supported input.
- **PLAT-004 — Availability.** Check APIs and entitlements per target. Define fallbacks.
- **PLAT-005 — Destinations.** Build each affected target and exercise its task. Identify untested hardware.

## Workflow

1. Map inputs to scenes. Isolate platform presentation in views.
2. Choose which scene handles external requests, regains focus and restores state.

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
