---
name: swiftui-navigation
description: "Fix SwiftUI Back behavior, deep links, sheets, scene selection, and restoration in NavigationStack or NavigationSplitView."
---

# Navigation and presentation

## Inputs

Record target, deployment minimum, journey, owning scene or tab, record IDs, and restoration requirements.

## Rules

- **NAV-001 — Route by identity.** Store lightweight route values or IDs. At the destination, load the current record and check authorization.
- **NAV-002 — Match container to task.** Use stacks for hierarchy, split views for persistent selection/detail, tabs for peers, and sheets for focused tasks.
- **NAV-003 — Give presentation one owner.** Represent mutually exclusive sheets with one selection. Keep paths and selection per scene unless sharing is intentional.
- **NAV-004 — Define each exit.** Preserve Back and keyboard dismissal. Commit on Save. Handle unsaved drafts explicitly on Cancel or dismissal.
- **NAV-005 — Validate incoming routes.** Parse supported URLs, resolve authentication, and handle malformed, deleted, or inaccessible destinations.

## Workflow

1. Use route values for restorable steps and intermediate screens Back must reach after a value push.
2. Register destinations outside lazy rows. Synchronize selection and path through their owner. Check availability on the oldest target.

## Verify

- NAV-003, NAV-004: Push from a guide to a detail, then go Back. If the guide belongs in history, confirm it reappears in compact and expanded layouts. For scene-local paths, navigation leaves the second window unchanged.
- NAV-005: Deliver a link twice and confirm one intended destination. Restore a deleted record on cold launch and check the unavailable state or root fallback.
- NAV-003, NAV-004: Switch sheets, edit, then cancel. Confirm the intended editor opened and stored data stayed intact.

## Output

Report owners, fallback, and observed path and screen at the failing transition.

## References

- [Containers, modal tasks, and scene ownership](references/navigation-patterns.md)
- [Back history, deep links, and restoration](references/routing-and-restoration.md)
