# Context handoffs, batch changes, and history

## Which version does the reader need?

For a point-in-time export, copy the needed values on the owning context. For a screen that needs current values, pass the ID and resolve it on the reader's queue. An importer's permanent ID can reach a reader before the first save. A detail screen can receive the same ID after deletion. Use a throwing lookup when either outcome changes the UI.

Hold the import after ID allocation. A fresh reader should fail to resolve it. Save and check its business ID from a second reader. Delete and save, then open the detail screen in a third reader. A reader with an already registered object also needs the deletion merged.

## Who consumes a batch?

For a local batch with known observers, merge affected IDs into those contexts. A returning reader can refetch current state. If it must process intervening transactions, keep a durable history cursor. Use notifications to trigger a fetch and filter by store and author where appropriate. Pick one path for each side effect.

Pause one consumer. Have a second process a transaction and crash before saving its cursor. Restart both. The replay should preserve one user-visible effect and the slower reader must still find its transactions. Only then is that history eligible for pruning.
