---
name: swiftdata
description: "Design or repair SwiftData models, predicates, relationships, indexes, context ownership, history, disk migrations, and CloudKit-compatible schemas."
---

# SwiftData schemas, queries, and migrations

## Inputs

Identify registered models, store configuration, context isolation, shipped schemas, target OS, and sync settings.

## Rules

- **SD-001 — Define relationship ownership.** Choose inverses and delete rules by deciding which records survive deletion of each endpoint.
- **SD-002 — Execute translated queries.** Run predicates on the supported store. Check returned IDs, ordering, limits, and optional relationships.
- **SD-003 — Confine mutable models.** Keep live models on their context’s actor. Transfer identifiers or snapshots.
- **SD-004 — Preserve schema history.** Freeze shipped schemas. On open or migration failure, retain the original store and diagnostics. Offer recovery.
- **SD-005 — Verify cloud behavior separately.** Check CloudKit schema constraints and account changes. Verify delivery at the destination.

## Workflow

1. Specify when a draft enters its model’s store.
2. On rename, map the new property to its previous persisted name. Before enforcing uniqueness, choose surviving records and reconcile their relationships.

## Verify

- SD-002: Run the production predicate on the supported store. Compare ordered IDs with the fixture, including nil relationships and limits where used.
- SD-003: Save in one context and refetch by ID in another. The reader sees committed values.
- SD-004: For each supported disk upgrade, migrate distinct ID–value pairs. Save an edit and reopen. The edit and the other migrated values survive.
- SD-001: Delete a relationship endpoint and refetch both sides. Only the records covered by the delete rule disappear.

## Output

Report store type, schema versions, observed values, and untested migration or sync paths.

## References

- [Models, context ownership, and queries](references/models-and-queries.md)
- [Disk migrations, reopen tests, and sync](references/migration-and-sync.md)
