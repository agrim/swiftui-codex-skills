---
name: swiftui-platform-adaptation
description: "Adapt SwiftUI scenes, windows, focus, and input for iOS, iPadOS, macOS, watchOS, tvOS, or visionOS."
---

# Platform-native scenes and interaction

## Inputs

List affected targets, minimum OS versions, primary task, inputs, scenes, and capabilities.

## Rules

- **PLAT-001 — Share domain operations.** Reuse models and commands for equivalent outcomes. Adapt presentation to the platform.
- **PLAT-002 — Scope state per scene.** Choose the scene type for the task. Separate window drafts, navigation, and selection from shared services.
- **PLAT-003 — Support native input.** Make essential actions reachable by the intended touch, keyboard, pointer, remote, Crown, or spatial input.
- **PLAT-004 — Check availability.** Verify API support and entitlements per target. Define a fallback for unavailable features.
- **PLAT-005 — Verify per destination.** Build each affected target and exercise its primary task. Record untested destinations and hardware.

## Workflow

1. Map each task to its scene and input. Isolate platform-specific presentation at the view boundary.
2. Define the receiving scene for external requests, focus after dismissal, and state restored on reopen.

## Verify

- PLAT-002: Where windows can resize or switch, check that selection, draft, and keyboard commands still target the intended record.
- PLAT-003: On watchOS, read and activate the primary control. On tvOS, reach it by remote and regain focus after dismissal.
- PLAT-003, PLAT-005: On visionOS, complete the task using supported spatial input and exit to the expected scene. Assess physical comfort on hardware.

## Output

Report scene, input, shared command, fallback, build destination, and runtime result per target.

## References

- [Platform tasks, input, and availability](references/platform-patterns.md)
- [Scene ownership, desktop commands, and focus](references/scenes-and-focus.md)
