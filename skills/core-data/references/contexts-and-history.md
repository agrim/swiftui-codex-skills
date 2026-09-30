# Contexts, batch operations, and history

A context is an isolated unit of work, not a thread-safe object collection. Schedule private-queue work with `perform`; do not move a fetched object into a task on another executor. Copy a value snapshot or pass an object ID and resolve it in the receiving context. Check for temporary IDs and deletion before assuming resolution can succeed.

A child context save can push changes to its parent without writing the persistent store. Trace the entire save chain before promising durability. Avoid blocking the main queue on a private context that may call back to main. An actor wrapper does not automatically make arbitrary managed-object access safe.

Batch delete/update/insert works at the store layer and can leave registered objects stale. For suitable local batches, obtain affected object IDs and merge the changes into observing contexts. Persistent history is useful for durable multi-writer or cross-process consumption; it is not a mandatory prerequisite for every batch. Choose one coherent merge path and test duplicate processing.

Give each history consumer a persistent token, store identity, relevant transaction-author filtering, and failure retry. Process then advance the cursor, not the reverse. Pruning based only on the fastest consumer risks data loss for slower consumers. Notifications mean changes may exist; fetch actual transactions rather than trusting a single notification as an exact mutation record.

## Regression matrix

Verify a background save becomes visible through a fresh reader; a deleted object ID fails gracefully; a batch removes registered rows after merging; and a replay does not duplicate user-visible side effects. Use a temporary SQLite store for batch behavior. A passed in-memory test does not establish SQL translation, batch support, migration, or file protection behavior.

## Official sources

- [Core Data concurrency programming guide (archived)](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/Concurrency.html).
- [Core Data batch delete guide (archived)](https://developer.apple.com/library/archive/featuredarticles/CoreData_Batch_Guide/BatchDeletes/BatchDeletes.html).
- [Consuming relevant store changes](https://developer.apple.com/documentation/coredata/consuming-relevant-store-changes).
- [CloudKit](https://developer.apple.com/documentation/cloudkit).
