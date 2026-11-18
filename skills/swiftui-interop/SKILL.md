---
name: swiftui-interop
description: "Bridge UIKit or AppKit with SwiftUI representables, hosting, coordinators, and delegates."
---

# UIKit and AppKit bridges

## Inputs

Identify the missing capability, OS, and owner.

## Rules

- **BRIDGE-001 — Limit scope.** Wrap the smallest supported public API that fills the gap.
- **BRIDGE-002 — Update in place.** Create once per identity. Apply only changed inputs.
- **BRIDGE-003 — Rebind callbacks.** Refresh coordinator bindings and handlers. Suppress programmatic delegate echoes.
- **BRIDGE-004 — Dismantle.** Detach observers and delegates, cancel owned tasks, and reject late callbacks.
- **BRIDGE-005 — Preserve interaction.** Respect UI isolation, proposed size, focus, accessibility, responder chains, and controller containment.

## Workflow

1. Trace each lifecycle owner. Exercise resizing and reparenting in the host.

## Verify

- BRIDGE-001: Exercise the missing capability on the minimum OS. It works through the adapter, and unrelated controls work without it.
- BRIDGE-002, BRIDGE-005: Reapply unchanged text. Marked text, focus, and selection survive.
- BRIDGE-003: One edit changes the model once. Programmatic writes produce no echo.
- BRIDGE-004: Remount. Old resources are released and stale callbacks cannot change the model.

## Output

Report owners, interaction results, and cleanup evidence.

## References

- [Hosting, sizing, and focus](references/interop-patterns.md)
- [Representable lifecycle](references/representable-lifecycle.md)
