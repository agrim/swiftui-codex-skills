---
name: swiftui-navigation
description: "Fix SwiftUI Back behavior, deep links, sheets, scene selection, and restoration in NavigationStack or NavigationSplitView."
---

# Make Back, Cancel and deep links land on the right screen

Use this when Back skips a screen, Cancel closes the wrong window or a saved link opens a record the user can no longer access.

## Start here

Write the expected journey, such as “Folder → Guide → Document, then Back to Guide.” Reproduce it in the affected window and width.

## How to proceed

1. **Identify the record behind each destination.** Store the record’s stable ID in the route. Restore only records the current account can still open. <!-- NAV-001 -->
2. **Choose the container by the return journey.** Should Back revisit a screen, Cancel dismiss an editor, or a wider window reveal a selection? Track the history or selection that container needs. If a restored destination appears only after scrolling, move its registration outside the lazy row. <!-- NAV-002 -->
3. **Give each editor a clear owner.** Use one selection to choose between sheets that must never appear together. Keep history per window unless the product deliberately shares it. <!-- NAV-003 -->
4. **Decide what each exit does to a draft.** Follow Back, Cancel and keyboard dismissal to the editor that owns the draft. Keep unsaved work available after a failed Save. <!-- NAV-004 -->
5. **Recheck delayed links.** If login interrupts a link, validate its target and account again before presenting the destination once. <!-- NAV-005 -->

## Check the result

- Back reaches Guide at both widths. Collapsing a split view keeps its selection. A second window keeps its history. Repeat on the oldest supported target. <!-- NAV-002 NAV-003 NAV-004 -->
- Open the same link twice and count one destination. Relaunch after deletion or revoked access. Expect an unavailable message or a safe return screen. <!-- NAV-001 NAV-005 -->
- Switch sheets, edit the second record and cancel. Reopen both records and confirm neither stored value changed. <!-- NAV-003 NAV-004 -->

## What to report

Show the expected and observed path at the first wrong screen and name the code that owns it.

- [Choose who owns a scene’s history or a sheet’s draft](references/navigation-patterns.md)
- [Diagnose skipped screens, failed dismissal and stale links](references/routing-and-restoration.md)
