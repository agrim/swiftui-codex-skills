---
name: core-data
description: "Diagnose Core Data context handoffs, batch merges, persistent history, conflicts, SQLite migrations, and CloudKit mirroring."
---

# Core Data

## Inputs

Identify stores, model versions, context queues and parents, readers, and mirroring settings.

## Rules

- **CD-001 — Choose the handoff.** Send snapshots for historical values, IDs for current values.
- **CD-002 — Resolve IDs.** Publish IDs after save. Handle deletion before lookup.
- **CD-003 — Merge batches.** Merge affected IDs for live readers. Refetch missed state or replay required history.
- **CD-004 — Protect readers.** Advance cursors after successful processing. Preserve history slower readers need.
- **CD-005 — Preserve stores.** Keep originals and diagnostics after open or upgrade failure.

## Workflow

1. Trace a background edit to disk and UI.
2. Bound fetches and imports. Choose which edits survive conflicts.

## Verify

- CD-001, CD-002, CD-003: Batch-delete a SQLite row. After merge, check disappearance and failed lookup on a fresh reader’s queue.
- CD-004: Replay history. Effects occur once and slower readers resume.
- CD-005: Reopen each supported disk upgrade. Compare IDs, values and relationships. Fail migration on a copy. Check the original, sidecars, and diagnostic.

## Output

Report save chain, merge policy, recovery, and account evidence for mirroring.

## References

- [Contexts and history](references/contexts-and-history.md)
- [Fetches and migrations](references/migration-and-fetches.md)
