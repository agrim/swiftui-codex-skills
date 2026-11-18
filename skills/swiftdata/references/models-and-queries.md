# Models, contexts, and query correctness

Make `ModelContainer` failure visible and recoverable. Ensure every intended model and related type is part of the schema and the correct store configuration. A preview or test container must not accidentally select production CloudKit or a user's real store.

Choose relationship optionality, inverse, cardinality, ordering, and delete behavior from actual ownership. A cascade is suitable only when a child has no independent lifecycle that must survive. Test deleting either endpoint, reinserting, refetching, and cancellation of edits. Avoid assuming array insertion order is a durable sorting contract.

Keep broad queries close to a stable owner; use `FetchDescriptor` for repository operations, and view queries for view-owned reactive data. Add explicit sorting with a stable tie-breaker when order matters. Bound high-volume results and inspect faulting/relationship traversal rather than filtering entire stores in `body`.

Predicates need integration tests against the actual store: optional chains, to-many relationships, captures, dates, empty collections, and localized comparisons can have different translation constraints. Do not convert one reported SDK predicate bug into a timeless ban. Record the OS/SDK, minimal reproduction, fallback, and removal condition.

Consider indexing or uniqueness features only after checking availability, query patterns, existing duplicate data, and CloudKit support. An index has storage and write costs. New inheritance, history, or custom-store APIs require separate migration and deployment checks rather than a blanket target increase.

Draft edits should not mutate an existing stored object before Save unless immediate persistence is intentional. An isolated writer can limit rollback scope, but transferring a managed object into it breaks ownership. Validate values before inserting, retain a failed draft, and distinguish a proven pre-save failure from an ambiguous externally completed operation.

## A derived filter with a fetch limit

A list shows the first five overdue invoices in priority order. `isOverdue` derives from a due date, payment status, and today's date. Express the filter using stored fields and a captured cutoff when the backend supports it. A computed or transient display flag has no persisted column. If filtering must happen in memory, scan ordered, bounded batches until five matches or exhaustion. Limiting the fetch to five candidates first can hide every match.

Seed five high-priority paid invoices, a future unpaid invoice and six overdue unpaid invoices. Tie two priorities at the limit. At a fixed cutoff, compare the exact five IDs in order on disk. Mark one returned invoice paid and confirm the sixth replaces it according to the tie-breaker.

## Official sources

- [SwiftData ModelContext](https://developer.apple.com/documentation/swiftdata/modelcontext).
- [SwiftData ModelContainer](https://developer.apple.com/documentation/swiftdata/modelcontainer).
- [SwiftData SchemaMigrationPlan](https://developer.apple.com/documentation/swiftdata/schemamigrationplan).
- [Syncing SwiftData across devices](https://developer.apple.com/documentation/swiftdata/syncing-model-data-across-a-persons-devices).
- [SwiftData ModelContext autosaveEnabled](https://developer.apple.com/documentation/swiftdata/modelcontext/autosaveenabled).
- [SwiftData ModelContext rollback()](https://developer.apple.com/documentation/swiftdata/modelcontext/rollback%28%29).
- [SwiftData transient properties](https://developer.apple.com/documentation/swiftdata/transient%28%29)
- [SwiftData fetch limit](https://developer.apple.com/documentation/swiftdata/fetchdescriptor/fetchlimit)
