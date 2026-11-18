---
name: swiftdata
description: "Design or repair SwiftData models, relationships, predicates, indexes, contexts, history, disk migrations, and CloudKit schemas."
---

# Preserve SwiftData records across queries, edits, and upgrades

Use this when a SwiftData query returns the wrong records, a deletion removes too much, or an upgrade loses saved values.

## Start here

Identify the affected models, saving context, shipped schemas, OS and sync settings. For a query, write down the expected records, such as the five highest-priority overdue invoices.

## How to proceed

1. **Choose what survives deletion.** Decide whether deleting a record should delete its children, especially children shared by two parents. <!-- SD-001 -->
2. **Run the actual query.** Exercise the app’s predicate, sorting, and limit on the supported store. Filtering only after fetching five candidates can omit every overdue invoice. <!-- SD-002 -->
3. **Keep draft and saved values distinct.** Decide when an editor writes its draft. For a fixed export, copy values on the model’s actor. For a current read elsewhere, pass the saved ID and refetch. <!-- SD-003 -->
4. **Protect shipped schemas.** Keep each shipped schema intact and put changes in a new version. For a rename, preserve the old stored value. Before enforcing uniqueness, choose which duplicate and relationships survive. Keep the store and diagnostic if an upgrade fails. <!-- SD-004 -->
5. **Check changes on the receiving device.** With CloudKit enabled, try the schema change with a supported older client and inspect the resulting records. <!-- SD-005 -->

## Check the result

- Delete a parent and refetch its children. Shared children should survive if another parent still needs them. Save an edit in one context and read it by ID in another. <!-- SD-001 SD-003 -->
- Compare ordered IDs from the production query with expected matches, including missing relationships, ties and the fetch limit. <!-- SD-002 -->
- Upgrade each supported disk fixture. Edit, save, reopen, and compare values by ID. <!-- SD-004 -->
- Confirm the synced edit at its destination. Switch accounts and verify private and shared records follow their access rules. <!-- SD-005 -->

## What to report

Give the schema versions, store and runtime used, and which query, upgrade, or sync outcomes you verified.

- [Relationship ownership and limited queries](references/models-and-queries.md)
- [Disk-backed upgrades and changes across devices](references/migration-and-sync.md)
