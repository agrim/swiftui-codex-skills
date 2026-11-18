---
name: swiftdata
description: "Design or repair SwiftData models, relationships, predicates, indexes, contexts, history, disk migrations, and CloudKit schemas."
---

# SwiftData

## Inputs

Identify models, store, context actors, shipped schemas, OS, and sync settings.

## Rules

- **SD-001 — Specify ownership.** Set inverses and delete rules for the intended survivors.
- **SD-002 — Execute predicates.** Check translation on the target store.
- **SD-003 — Confine models.** Keep models on their actor. Transfer IDs or snapshots.
- **SD-004 — Freeze shipped schemas.** Preserve failed stores and diagnostics. Offer recovery.
- **SD-005 — Confirm delivery.** Check CloudKit constraints, account changes, and destination records.

## Workflow

1. Define when drafts become persistent.
2. Map renames to stored names. Reconcile duplicate rows and relationships before enforcing uniqueness.

## Verify

- SD-001: Delete an endpoint. Refetch both sides and check survivors.
- SD-002: Compare ordered IDs for the production predicate, including relevant nil relationships and limits.
- SD-003: Save in one context. Refetch by ID in another and compare values.
- SD-004: Upgrade each supported disk fixture. Edit, save, reopen, and compare ID–value pairs.
- SD-005: With sync enabled, confirm destination delivery. Switch accounts and check visibility against the private or shared store’s access rules.

## Output

Report store, versions, observations, and untested upgrade or sync paths.

## References

- [Models and queries](references/models-and-queries.md)
- [Migration and sync](references/migration-and-sync.md)
