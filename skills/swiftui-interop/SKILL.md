---
name: swiftui-interop
description: "Bridge SwiftUI to UIKit or AppKit with representables, hosting, coordinators, and delegates."
---

# UIKit and AppKit interoperability

## Inputs

Identify the missing capability, supported OS, platform object, inputs, callbacks, and lifetime.

## Rules

- **BRIDGE-001 — Bound the adapter.** For capabilities SwiftUI lacks on supported targets, wrap the smallest suitable public platform API.
- **BRIDGE-002 — Separate creation from updates.** Create the platform object once per identity. Update changed inputs in place.
- **BRIDGE-003 — Refresh callbacks.** Give the coordinator current bindings and handlers. Suppress delegate echoes from programmatic writes.
- **BRIDGE-004 — Release owned resources.** On dismantle, detach observers and delegates, cancel owned tasks, and discard late callbacks.
- **BRIDGE-005 — Preserve native interaction.** Honor UI actor isolation, proposed size, focus, accessibility, responder chains, and controller containment.

## Workflow

1. Assign ownership for creation, updates, callbacks, and teardown.
2. Rebind the coordinator when ownership changes. Exercise resizing and reparenting in the host.

## Verify

- BRIDGE-002, BRIDGE-005: During text editing, reapply unchanged input. Focus, selection, and marked text survive.
- BRIDGE-003: One user edit produces one model change. A programmatic update produces no duplicate edit.
- BRIDGE-004: Recreate the view and deliver an old callback. The current model stays unchanged and old resources are released.

## Output

Report the capability gap, adapter interface, owners, and observed interaction and cleanup results.

## References

- [Hosting, sizing, focus, and platform behavior](references/interop-patterns.md)
- [Representable updates, callbacks, and teardown](references/representable-lifecycle.md)
