---
name: core-data
description: "Diagnose Core Data context handoffs, batch changes, persistent history, merge conflicts, SQLite migrations, and CloudKit mirroring."
---

# Core Data contexts, history, and migration

## Inputs

Identify stores, model versions, context queues and parents, merge policy, history consumers, and mirroring settings.

## Rules

- **CD-001 — Confine managed objects.** Schedule access on the owning context. Cross context boundaries with object IDs or immutable values.
- **CD-002 — Resolve IDs at use.** Pass permanent IDs across contexts. Handle a lookup failing because the record is unsaved or deleted.
- **CD-003 — Merge batch changes.** Update observing contexts using affected object IDs or persistent history.
- **CD-004 — Protect history consumers.** Advance each cursor after successful processing. Retain transactions any required consumer still needs.
- **CD-005 — Preserve failed stores.** Upgrade a disk fixture from each supported model version. Retain the original store and diagnostics after open or migration failures.

## Workflow

1. Trace a background edit through any parent contexts to disk and the UI.
2. Bound fetches and imports. Choose which edit survives a local/background conflict.

## Verify

- CD-003: Batch-delete a SQLite row. The observing context and a fresh fetch both reflect the deletion.
- CD-004: Replay a transaction. Its effects occur once and a slower consumer can resume from its own cursor.
- CD-005: Reopen the upgraded disk fixture. Business IDs, values, and relationships match the fixture.

## Output

Report the save chain, merge policy, and recovery gaps. Give separate account evidence for mirroring claims.

## References

- [Context handoffs, batch changes, and history](references/contexts-and-history.md)
- [Fetches, conflicts, and migrations](references/migration-and-fetches.md)
