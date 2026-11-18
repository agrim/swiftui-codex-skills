---
name: apple-data-persistence
description: "Choose a store and define save, cancel, migration, and sync behavior across SwiftData, Core Data, files, or CloudKit."
---

# Persistence, drafts, and synchronization

## Inputs

Identify the authoritative store, supported schemas, context owners, and local and remote save guarantees.

## Rules

- **DATA-001 — Define commit.** Separate drafts, tracked edits, saved records, and remote acknowledgements. Keep targets and observations distinct from confirmed values when storing or exporting them.
- **DATA-002 — Isolate edits.** Access managed objects within their context’s isolation domain. Pass IDs or immutable snapshots across actors.
- **DATA-003 — Preserve shipped data.** Exercise migrations on historical disk fixtures. If opening or migration fails, retain the original store and diagnostics.
- **DATA-004 — Reconcile sync.** Track pending writes and deletions per account. Reconcile uncertain outcomes before retrying non-idempotent writes.
- **DATA-005 — Retain failed drafts.** Surface save errors, preserve editable input, and report success only after the promised commit.

## Workflow

1. Trace an edit through storage, sync, and export.
2. For explicit Save/Cancel, stage changes in a value or isolated edit context. Define validation, conflict resolution, and retry identity.
3. Bound queries to the feature’s data. Measure fetches before changing observation ownership.

## Verify

- DATA-001, DATA-005: Cancel a staged edit, then try saving another with a forced error. Both leave stored values intact. The failed draft remains editable.
- DATA-003: Reopen each supported disk upgrade. Migrated field values and relationships match the fixture’s expected mappings.
- DATA-004: Retry an interrupted sync. Each intended write or deletion takes effect once where deduplication is promised. Switching accounts hides the previous account’s records.

## Output

Report commit guarantees, upgrade paths tested, recovery behavior, and remote evidence.

## References

- [Drafts, rollback, and synchronization](references/persistence-patterns.md)
- [Store selection and recovery](references/store-selection-and-recovery.md)
