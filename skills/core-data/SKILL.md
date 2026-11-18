---
name: core-data
description: "Diagnose Core Data context handoffs, batch merges, persistent history, conflicts, SQLite migrations, and CloudKit mirroring."
---

# Make Core Data changes visible to every reader

Use this when a saved or deleted record looks different to two Core Data readers, or an upgrade changes what they see.

## Start here

For a deleted row that still appears onscreen, identify the writer, its parent contexts, the disk store, and the context feeding the list. Note model versions and whether CloudKit mirrors the store.

## How to proceed

1. **Choose what the reader needs.** For a historical export, copy the values on the writer’s queue. For a live detail screen, pass an object ID and fetch current values on the reader’s queue. <!-- CD-001 -->
2. **Save new records before sharing their IDs.** Follow saves through parent contexts to the shared store. Handle a record deleted between save and lookup. <!-- CD-002 -->
3. **Update readers after a batch change.** Merge changed IDs into live contexts. Limit fetches and imports to the affected records and choose which pending edits survive a conflict. <!-- CD-003 -->
4. **Let offline readers catch up.** Refetch if only current state matters. For readers that process each transaction, advance their saved position after processing succeeds and retain history until every required reader has caught up. <!-- CD-004 -->
5. **Preserve a failed store.** Try opening or migrating a copy first. Retain the original store files and migration error for recovery. <!-- CD-005 -->

## Check the result

- Batch-delete a SQLite row. It disappears from the merged list and a fresh reader cannot find it by ID. <!-- CD-001 CD-002 CD-003 -->
- Pause a reader and replay a transaction on another. Each effect happens once and the paused reader can resume. <!-- CD-004 -->
- Upgrade and reopen each supported disk fixture. Compare IDs, values and relationships. Force an upgrade failure and verify the original database and its companion files survive and the error is recorded. <!-- CD-005 -->

## What to report

Identify the save or merge that changed the outcome, and distinguish local recovery from any mirroring verified in the destination account.

- [Sharing object IDs and replaying history](references/contexts-and-history.md)
- [Fetches, conflicting edits, and migration recovery](references/migration-and-fetches.md)
