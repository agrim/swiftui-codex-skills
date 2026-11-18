---
name: apple-data-persistence
description: "Choose persistence for drafts, saves, migrations, and sync across SwiftData, Core Data, files, or CloudKit."
---

# Make Save and Cancel keep their promises

Use this when choosing storage for an Apple app or fixing data that disappears, reappears, or syncs twice. Follow one edit from typing to the result the user expects after reopening the app.

## Start here

Pick a real action, such as saving an inspection. Identify where the original record lives, who can edit it, and whether “Saved” means written on this device or received elsewhere.

## How to proceed

1. **Choose a store for the data you have.** Compare file storage with a database against your query, relationship and recovery needs. Preserve the unit and source through export so estimates remain distinguishable from confirmed values. <!-- DATA-001 -->
2. **Give each editor its own draft.** Stage cancellable changes separately so cancelling one editor leaves another editor’s pending work intact. <!-- DATA-002 -->
3. **Make failure recoverable.** Validate before saving. Keep the draft editable on error and show success only when the promised write completes. <!-- DATA-005 -->
4. **Protect existing records during upgrades.** Try each supported schema on a copy. Keep the original store and the error if migration fails. <!-- DATA-003 -->
5. **Handle interrupted sync.** Track edits and deletions per account. Decide which conflicting change wins. Check whether an unacknowledged write already landed before retrying. <!-- DATA-004 -->

## Check the result

- Cancel one edit and force another to fail. Reopen both records by ID. Both original values survive and the failed draft can still be saved. <!-- DATA-001 DATA-002 DATA-005 -->
- Upgrade an old disk store and reopen it. Compare values and relationships. A failed upgrade offers recovery and preserves the original. <!-- DATA-003 -->
- Interrupt sync after remote acceptance. Resume without duplicating the change, then switch accounts and check which records are visible. <!-- DATA-004 -->

## What to report

Name the store, when Save succeeds, and what survived failure, upgrade, and interrupted sync.

- [Cancelling drafts and exporting confirmed values](references/persistence-patterns.md)
- [Choosing a store and recovering from a failed save](references/store-selection-and-recovery.md)
