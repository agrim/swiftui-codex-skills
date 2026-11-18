---
name: core-data
description: "Diagnose Core Data context handoffs, batch merges, persistent history, conflicts, SQLite migrations, and CloudKit mirroring."
---

# Core Data

## Inputs

Identify stores, model versions, context queues and parents, readers, and mirroring settings.

## Rules

- **CD-001 — Confine objects.** Use the owning queue. Transfer IDs or immutable snapshots.
- **CD-002 — Resolve IDs.** Publish permanent IDs after save. Handle missing rows.
- **CD-003 — Merge batches.** Merge changed IDs or history into observing contexts.
- **CD-004 — Protect readers.** Advance cursors after successful processing. Preserve history slower readers need.
- **CD-005 — Preserve stores.** Keep originals and diagnostics after open or upgrade failure.

## Workflow

1. Trace parent saves to disk and the observing UI.
2. Bound fetches and imports. Choose which edits survive conflicts.

## Verify

- CD-001, CD-002, CD-003: Batch-delete a SQLite row. Verify disappearance after merge and failed lookup by ID on a fresh reader’s queue.
- CD-004: Replay history. Effects occur once and slower readers resume.
- CD-005: Reopen each supported disk upgrade. Compare IDs, values and relationships. Force a migration failure on a copy. Verify the original store and sidecars survive and the error is recorded.

## Output

Report save chain, merge policy, recovery, and account evidence for mirroring.

## References

- [Contexts and history](references/contexts-and-history.md)
- [Fetches and migrations](references/migration-and-fetches.md)
