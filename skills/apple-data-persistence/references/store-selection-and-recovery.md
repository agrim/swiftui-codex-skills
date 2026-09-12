# Store selection and recovery boundaries

Choose the storage mechanism from constraints: data shape, query needs, schema history, interoperability, supported OS, sync model, and failure recovery. Do not migrate a working Core Data store simply because a new framework is preferred elsewhere. Route detailed SwiftData and Core Data behavior to their specialists.

Name the canonical truth and each projection. A widget snapshot, exported HealthKit record, intent entity, cloud replica, and on-screen draft may represent different subsets with different delivery guarantees. Keep identifiers, timestamps, origin, and confirmation authority where those distinctions change behavior.

## Recovery decisions

| Failure | Preserve | Avoid |
| --- | --- | --- |
| Validation fails | Editable draft and field context | Inserting a placeholder object |
| Local save fails | User work and actionable error | Reporting success after `try?` |
| Remote status unknown | Durable operation identity | Blind duplicate retry |
| Migration fails | Original store and diagnostics | Silent reset to empty data |
| Account switches | Account boundary and explicit policy | Showing another account's cache |

A local transaction does not make a cross-service operation atomic. Persist enough intent to reconcile after termination, then use the external service's documented identity/deduplication facilities. Mark ambiguous outcomes separately from proven pre-commit failure.

Define deletion across local stores, indexes, backups, cloud replicas, and exports. A tombstone may need retention until consumers converge; user-visible deletion and physical erasure can differ. Explain limits honestly and minimize retained data.

Tests should cover every supported historical schema and actual storage backend used by the feature. In-memory tests are useful for ownership and save semantics, not disk recovery, SQLite-specific operations, protected-data behavior, or cloud convergence. Exercise fresh-container reopens and interrupted operations before making stronger claims.

## Official sources

- [SwiftData ModelContext](https://developer.apple.com/documentation/swiftdata/modelcontext).
- [SwiftData ModelContainer](https://developer.apple.com/documentation/swiftdata/modelcontainer).
- [CloudKit](https://developer.apple.com/documentation/cloudkit).
- [Keychain services](https://developer.apple.com/documentation/security/keychain-services).
