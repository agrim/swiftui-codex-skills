# Model ownership and query correctness

| Choice | Evidence that changes it |
| --- | --- |
| Cascade or retain a related record | Delete each endpoint of a shared relationship. Check whether a child used elsewhere survives. |
| Live model or snapshot | For an editor with Cancel, stage values or use an isolated writer. Try cancelling with another editor's change pending. |
| Index or bounded fetch | Measure the production query and the import that maintains its index. Check both on a supported store. |
| Workaround for an untranslated predicate | Record the failing OS, store, and expression. Keep a query fixture that can retire the workaround when translation succeeds. |

## A derived filter with a fetch limit

A list shows the first five overdue invoices in priority order. Filter by stored due date and payment status at a captured cutoff. If filtering must happen in memory, scan stable, ordered batches until five matches or exhaustion. Applying a limit to five unfiltered candidates can hide every match.

Seed five high-priority paid invoices, a future unpaid invoice and six overdue unpaid invoices. Tie two priorities at the limit. At a fixed cutoff, compare the exact five IDs in order on disk. Mark one returned invoice paid and confirm the sixth replaces it according to the tie-breaker. Give previews and fixtures their own store and cloud configuration.
