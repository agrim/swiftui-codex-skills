# Persistence, drafts, and synchronization: playbook

## Separate the storage contracts

| Data | Suitable starting point | Not a substitute for |
| --- | --- | --- |
| Temporary editor values | Value draft | Durable commit |
| Small preference | `AppStorage`/UserDefaults | Credentials or large relational data |
| Structured local records | SwiftData or existing Core Data stack | Guaranteed cross-device acknowledgement |
| Documents/binary assets | Appropriate file/document APIs | Permission-free arbitrary filesystem access |
| Credentials | Keychain with an explicit access policy | General user-default storage |
| Remote replica/projection | CloudKit or service adapter | Canonical business semantics by itself |

SwiftData's context tracks changes in memory and writes through explicit or implicit saves. Do not infer that a model mutation is already durable, or that merely dismissing an editor rolls it back. The main context has main-actor ownership; inspect the isolation of other persistence work rather than moving live models into detached tasks.

## Draft and save semantics

For a new record, create a value draft outside the persistent context. Validate, then insert and explicitly save when the workflow promises a durable commit. Preserve the draft on failure. For an edit, choose either explicit value-to-model commit or an isolated edit context whose rollback semantics are understood. Rolling back a shared context can undo unrelated work.

Autosave can be convenient for continuous editing. It is not automatically compatible with a Cancel button promising no changes. Name the product contract: autosaved document editing, staged form submission, or explicit transactional operation. Test interruption at the actual persistence boundary.

## Context-local rollback

For staged local creation, a dedicated writer context with autosave explicitly disabled can isolate a failed commit from unrelated pending edits in the shared main context. Validate the value first; create and insert the model only on Save; propagate any save failure and retain the user's draft. Roll back only that writer's pending changes. This is an engineering choice, not a requirement to create a context per operation in every app.

`rollback()` affects pending inserts, deletes, edits, and the undo stack for its context. It is not a selective undo command and cannot reverse an already committed save or remote operation. Autosave defaults differ between a newly created context and the container's main context; inspect and set the policy intentionally rather than relying on a presumed universal default.

The repository's `DraftNoteStoreTests` exercise this boundary with real SwiftData in-memory storage on Apple SDKs. An injected pre-save failure proves recovery from that failure point only. It does not simulate a disk-full error, partial disk write, migration, cold launch, or CloudKit conflict. Do not turn its retry test into an exactly-once claim: repeated successful Create calls intentionally create different records.

## Queries and observation

Scope queries by the feature's data need. Avoid adding broad live queries to every sheet and row. Pass the necessary data or identifiers from a stable owner where that reduces redundant observation. Use fetch limits, sorting, paging, or indexes when supported and measured. Do not promise performance from changing wrappers alone.

An in-memory store is useful for unit tests and previews, but does not prove disk persistence, migration, protection, contention, or app-group access. Include temporary disk-backed round trips and reopen the store before asserting durability.

## Schema evolution

Keep versioned schemas and a supported upgrade matrix. Test realistic old fixtures, relationships, uniqueness, deleted records, and failed migration. Back up or provide a documented recovery/export path where the risk warrants it. Never ship a catch block that silently switches to an empty in-memory store and reports success. A destructive reset must be deliberate and user-authorized, not an automatic exception handler.

Cloud-compatible schemas have additional constraints; verify them in the current framework documentation. A successful local migration is not evidence that cloud synchronization or older clients remain compatible.

## Sync, retries, and deletion

Give repeatable external writes an operation identity where duplication matters. Persist enough intent to reconcile after termination when an acknowledged local promise outlives the process. Define conflict resolution and what the user sees while uncertain. Exactly-once delivery cannot be manufactured by a client-side boolean.

Keep local delete, tombstone propagation, export deletion, search-index removal, and retention distinct. Reconcile account changes without mixing data between people. Define whether a remote failure blocks local success or leaves a pending projection; do not let supplementary cloud service failure erase locally valid work.

## Failure probes

Inject a save failure after validation; assert the editor remains recoverable. Relaunch after successful save and after interrupted save. Retry an operation with the same ID. Upgrade each supported schema fixture. Exercise quota, offline, account replacement, and inaccessible storage. Verify a delete reaches every representation that the product promises to remove.

## Value meaning before storage

For products with plans and measured outcomes, represent a target, an observation or estimate, a user-confirmed result, and an external projection as different states. Preserve unit, provenance, and correction ownership. Unknown is not zero; a planned value is not evidence of a completed result. Confirming an estimate creates a new authoritative value without rewriting where the estimate came from.

For example, a count-based inspection may target 12 items, observe an estimated 10, and confirm 9 after correction. History and export use the confirmed 9 with its unit; the plan remains 12. Repeating that inspection creates a fresh draft with no result or export acknowledgement. Whether it copies the plan or the previous result into a new target is a product choice that must be explicit.

Validate quantities at their semantic boundary: whole-item counts reject fractional or negative values; other measurements may legitimately allow them. Keep this policy in domain code, independent of the keyboard. Test unknown versus zero, correction, repeat/cancel, unit mismatch, and failed export. These are engineering patterns, not a prescribed Apple data model.

## Sources

- [model-context](https://developer.apple.com/documentation/swiftdata/modelcontext) — SwiftData ModelContext.
- [model-container](https://developer.apple.com/documentation/swiftdata/modelcontainer) — SwiftData ModelContainer.
- [cloudkit](https://developer.apple.com/documentation/cloudkit) — CloudKit.
- [keychain](https://developer.apple.com/documentation/security/keychain-services) — Keychain services.
- [swiftdata-autosave](https://developer.apple.com/documentation/swiftdata/modelcontext/autosaveenabled) — SwiftData autosave policy.
- [swiftdata-rollback](https://developer.apple.com/documentation/swiftdata/modelcontext/rollback%28%29) — Context-wide rollback scope.
