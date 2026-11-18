# Observation, bindings, and dependency seams

## Two writes from one control

Follow a single edit through its binding setter and change handler. If both save, decide which boundary owns the commit. Retain a custom projection when it enforces a real invariant. If replacing it, compare call order, commit count and unaffected fields after one edit and cancellation.

## Identity and dependency probes

- Filter or reorder a list during typing. Track the draft, focus and ongoing save by domain ID. An index is enough for a synchronous operation on an unchanged snapshot.
- Swap a feature’s store or client while a task is in flight. Finish the old request. It must neither publish into the new feature nor keep the old owner alive.
- Change an input to a cached projection. Verify the resulting presentation and the unchanged source of truth before adding a second stored copy.

## A late save updates the wrong row

A user renames a document while the list sorts by name. The save completes, and a different document changes. Inspect the eventual write as well as the view’s row key. Sorting during suspension can leave a captured offset pointing at another record.

1. At submission, capture the record's identity and the proposed edit. Include account identity when record keys are unique only within an account.
2. On completion, resolve that identity in the current owner. If the record was deleted or the user switched accounts, leave the current list alone. An ordinary array lookup is sufficient for a small list.
3. A second edit to the **same** record still passes an ID check. For last-edit-wins UI, track the current edit token per record and apply success, failure, or pending-state cleanup only to the matching edit. If the server supplies authoritative revisions, reconcile according to its version contract. Suppressing a stale UI update alone cannot order writes at the server.

Use a controllable save client. Pause the first rename, reorder the list, then complete it and assert by document ID that only the renamed document changed. Repeat after deleting the document and assert it stays absent. Finally submit a second rename to the same document, finish it first, and deliver the older success or error. Check the displayed name and pending/error state.
