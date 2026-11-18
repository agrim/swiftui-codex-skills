---
name: swiftui-navigation
description: "Fix SwiftUI Back behavior, deep links, sheets, scene selection, and restoration in NavigationStack or NavigationSplitView."
---

# Navigation and presentation

## Inputs

Target, minimum OS, journey, scene or tab, IDs and restoration needs.

## Rules

- **NAV-001 — Identity.** Resolve route IDs against current records and permissions.
- **NAV-002 — Container.** Choose the container by what Back, Cancel or a width change should reveal.
- **NAV-003 — Ownership.** Use one selection for exclusive sheets. Scope paths and selection per scene unless intentionally shared.
- **NAV-004 — Exits.** Specify what survives Back, Cancel, keyboard dismissal and a failed Save.
- **NAV-005 — Incoming links.** If login delays a link, recheck its target and account before presenting it once.

## Workflow

1. Write the expected history. Compare it with the path after each transition.
2. If a restored route works only after scrolling, inspect who registers its destination. Check the oldest target.

## Verify

- NAV-002, NAV-003, NAV-004: Push guide then detail. Back reveals the guide at both widths. Collapsing a split view preserves selection. A second window retains its path.
- NAV-001, NAV-005: Open a link twice for one destination. Relaunch after deletion or revoked access. Restoration shows the fallback.
- NAV-003, NAV-004: Switch sheets, edit, cancel. Verify editor identity and unchanged stored data.

## Output

Owner, fallback, path and screen at failure.

## References

- [Containers, sheets, and scenes](references/navigation-patterns.md)
- [Skipped history, failed dismissal, and restoration](references/routing-and-restoration.md)
