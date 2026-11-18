---
name: apple-data-persistence
description: "Choose persistence for drafts, saves, migrations, and sync across SwiftData, Core Data, files, or CloudKit."
---

# Persistence and sync

## Inputs

Identify the authoritative store, schemas, context owners, and promised durability.

## Rules

- **DATA-001 — Define commit.** Name the event that fulfills Save. Export the agreed value with its provenance.
- **DATA-002 — Isolate drafts.** Stage cancellable edits where discarding one cannot undo another.
- **DATA-003 — Protect upgrades.** Keep original stores and diagnostics on failure.
- **DATA-004 — Reconcile retries.** Track writes and deletions per account. Resolve uncertain non-idempotent writes before retry.
- **DATA-005 — Preserve drafts.** Surface save errors. Confirm success only at the promised commit.

## Workflow

1. Trace a confirmed value from editor through sync and export.
2. Choose validation, conflict policy, and retry identity. Bound queries to each reader’s needs.

## Verify

- DATA-001, DATA-002, DATA-005: Cancel one edit while another is pending. Fail the second save. Refetch original values by ID and check the second draft stays editable.
- DATA-003: Upgrade each supported disk fixture. Reopen and compare mapped values and relationships.
- DATA-004: Replay interrupted sync. Deduplicated changes apply once. Switching accounts hides prior records.

## Output

Report durability, recovery, tested upgrades, and sync evidence.

## References

- [Drafts and rollback](references/persistence-patterns.md)
- [Store choice and recovery](references/store-selection-and-recovery.md)
