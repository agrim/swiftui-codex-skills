---
name: swiftui-navigation
description: "Fix SwiftUI Back behavior, deep links, sheets, scene selection, and restoration in NavigationStack or NavigationSplitView."
---

# Navigation and presentation

## Inputs

Target, minimum OS, journey, scene or tab, IDs and restoration needs.

## Rules

- **NAV-001 — Identity.** Resolve route IDs against current records and permissions.
- **NAV-002 — Container.** Use stacks for hierarchy, split views for selection/detail, tabs for peers, sheets for focused tasks.
- **NAV-003 — Ownership.** Use one selection for exclusive sheets. Scope paths and selection per scene unless intentionally shared.
- **NAV-004 — Exits.** Preserve Back and keyboard dismissal. Save commits. Define draft handling on other exits.
- **NAV-005 — Incoming links.** Validate URL, authentication and record access. Provide a fallback.

## Workflow

1. Use route values for restorable steps and screens Back must revisit after a value push.
2. Register destinations outside lazy rows. Synchronize selection and path at their owner. Check availability.

## Verify

- NAV-002, NAV-003, NAV-004: Push guide then detail. Back reveals the guide at both widths. Collapsing a split view preserves selection. A second window retains its path.
- NAV-001, NAV-005: Open a link twice for one destination. Relaunch after deletion or revoked access. Restoration shows the fallback.
- NAV-003, NAV-004: Switch sheets, edit, cancel. Verify editor identity and unchanged stored data.

## Output

Owner, fallback, path and screen at failure.

## References

- [Containers, sheets, and scenes](references/navigation-patterns.md)
- [Skipped history, failed dismissal, and restoration](references/routing-and-restoration.md)
