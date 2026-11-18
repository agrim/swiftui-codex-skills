---
name: swiftdata
description: "Design or repair SwiftData models, relationships, predicates, indexes, contexts, history, disk migrations, and CloudKit schemas."
---

# SwiftData

## Inputs

Identify models, store, context actors, shipped schemas, OS, and sync settings.

## Rules

- **SD-001 — Specify ownership.** Decide which shared children survive each endpoint’s deletion.
- **SD-002 — Execute predicates.** Exercise the production query on supported store runtimes.
- **SD-003 — Choose the handoff.** Export snapshots. Pass saved IDs for fresh reads.
- **SD-004 — Freeze shipped schemas.** Preserve failed stores and diagnostics. Offer recovery.
- **SD-005 — Confirm delivery.** Check shipped clients’ schema compatibility and destination state.

## Workflow

1. Define when drafts become persistent.
2. For renames or uniqueness changes, identify the values and relationships to preserve.

## Verify

- SD-001: Delete an endpoint. Refetch both sides and check survivors.
- SD-002: Compare ordered IDs for the production predicate, including relevant nil relationships and limits.
- SD-003: Save in one context. Refetch by ID in another and compare values.
- SD-004: Upgrade each supported disk fixture. Edit, save, reopen, and compare ID–value pairs.
- SD-005: Confirm a synced edit at its destination. Switch accounts and check private or shared visibility against policy.

## Output

Report store, versions, observations, and untested upgrade or sync paths.

## References

- [Models and queries](references/models-and-queries.md)
- [Migration and sync](references/migration-and-sync.md)
