---
name: apple-data-persistence
description: "Choose persistence for drafts, saves, migrations, and sync across SwiftData, Core Data, files, or CloudKit."
---

# Persistence and sync

## Inputs

Identify the authoritative store, schemas, context owners, and promised durability.

## Rules

- **DATA-001 — Define commit.** Distinguish drafts, tracked edits, saves, and remote acknowledgements. Separate targets, observations, and confirmed results.
- **DATA-002 — Confine edits.** Cross contexts with IDs or immutable snapshots.
- **DATA-003 — Protect upgrades.** Keep original stores and diagnostics on failure.
- **DATA-004 — Reconcile retries.** Track writes and deletions per account. Resolve uncertain non-idempotent writes before retry.
- **DATA-005 — Preserve drafts.** Surface save errors. Confirm success only at the promised commit.

## Workflow

1. Stage Save/Cancel edits in isolation. Trace commit through sync and export.
2. Define validation, conflict policy, and retry identity. Bound queries and measure fetches before moving observers.

## Verify

- DATA-001, DATA-002, DATA-005: Cancel one edit and fail another save. A separate context refetches original values by ID. The failed draft stays editable.
- DATA-003: Upgrade each supported disk fixture. Reopen and compare mapped values and relationships.
- DATA-004: Replay interrupted sync. Deduplicated changes apply once. Switching accounts hides prior records.

## Output

Report durability, recovery, tested upgrades, and sync evidence.

## References

- [Drafts and rollback](references/persistence-patterns.md)
- [Store choice and recovery](references/store-selection-and-recovery.md)
