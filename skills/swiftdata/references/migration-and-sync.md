# Schema evolution and synchronization

Keep the oldest supported released model definitions immutable. Record the ordered versions, migration stages, affected relationships, transform rules, and validation invariants. Choose lightweight migration only when the change is supported; use an explicit plan for transformations that need it.

For a stored property rename, give the destination property its previous persisted name using `@Attribute(originalName:)`. Apple illustrates this with a lightweight migration stage. If old rows collide under a proposed uniqueness constraint, define which row survives and what happens to its relationships, then exercise those duplicates through a custom stage before the constraint takes effect. An implicit choice of survivor can discard user data. [Apple’s schema migration examples](https://developer.apple.com/videos/play/wwdc2023/10195/)

### Exercise an upgrade on disk

1. Create a disposable directory with an explicit store URL and disable managed CloudKit sync for the local fixture. Use the frozen source `VersionedSchema` to write two records with distinguishable business IDs and values. Include the relationships or collisions affected by the change. Save and release the old contexts, models, and container.
2. Open that exact URL with `Schema(versionedSchema:)` for the destination, the app's ordered migration plan, and a disk configuration. Fetch from a new context. Compare the expected business ID–value pairs, new defaults, and relationship destinations. Counting rows alone misses fields that were reset or swapped.
3. Make and save a small destination-only edit. Release the container, reopen the same store with the current plan, and assert that the edit and migrated rows survived together. Record the fixture's source and destination versions and the SDK/runtime that actually ran it.

A store generated from historical model definitions under today's SDK covers that model transition. To investigate a failure specific to an older release or toolchain, also run the upgrade on a sanitized, store-consistent fixture produced by that release. Exercise unavailable or damaged storage separately when the incident calls for it.

Back up using a store-aware, consistent strategy rather than copying a live SQLite file without its associated state. On migration failure, preserve the original and present recovery or export options. Do not automatically delete data or claim downgrade support without testing it.

For CloudKit-backed schemas, inspect current framework constraints on uniqueness, defaults, optionality, inverses, and delete rules. Production schema evolution is constrained, but not every additive change is forbidden. Reconcile remote deletions, account changes, unavailable iCloud, conflicts, and interrupted synchronization. A local record count cannot prove every device converged.

History consumers need a per-consumer durable cursor and a retention policy that does not erase changes before other consumers process them. Match APIs and store capabilities to the deployed OS. Use domain operation IDs for retried cross-process work; do not infer exactly-once execution from an attribute declaration.

## Official sources

- [SwiftData ModelContext](https://developer.apple.com/documentation/swiftdata/modelcontext).
- [SwiftData ModelContainer](https://developer.apple.com/documentation/swiftdata/modelcontainer).
- [SwiftData SchemaMigrationPlan](https://developer.apple.com/documentation/swiftdata/schemamigrationplan).
- [Syncing SwiftData across devices](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices).
- [SwiftData ModelContext autosaveEnabled](https://developer.apple.com/documentation/swiftdata/modelcontext/autosaveenabled).
- [SwiftData ModelContext rollback()](https://developer.apple.com/documentation/swiftdata/modelcontext/rollback%28%29).
