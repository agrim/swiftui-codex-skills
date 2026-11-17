# Observation, bindings, and dependency seams

Choose lifetime before property wrapper. A view-local value belongs to its owner; a reference model requires a stable lifetime at the intended app, scene, feature, or row boundary. Do not create a new observable service during every `body` evaluation or let unrelated windows accidentally share editor state.

With Observation, a child can read an injected observable reference without acquiring ownership. Use `@Bindable` where bindings to that reference are needed; `@State` at a stable owner is a different responsibility. Keep the legacy observation wrappers where supported targets or existing architecture require them. Do not mix wrappers mechanically to silence update problems.

A custom `Binding(get:set:)` is valid for a real projection or invariant. Its setter should implement the intended change contract, not hide network requests, repeated saves, or inconsistent derived state. Replacing it with `onChange` can change ordering and duplicate side effects; compare both paths before migrating.

## Identity probes

Insert, delete, reorder, filter, and replace a collection while editing one row. Check that focus, selection, task work, animations, and drafts still belong to the same domain item. Avoid generating fresh IDs in computed properties or using indices as persistent identity for a mutable collection. A stable-looking label is not a unique key.

Separate stored truth from derived presentation. Cache expensive derivations only with a correct invalidation key; do not duplicate a mutable source of truth to reduce recomputation. Small pure projections or explicit immutable inputs often clarify updates without adding another coordinator layer.

Use dependency injection at the feature composition boundary for clients, clocks, stores, and ID creation. Keep defaults production-safe and previews/tests isolated. A project may use closures, protocols, or a deliberate architecture library; this skill does not require one. Verify deallocation and task cancellation when an injected owner leaves its intended lifetime.

## A late save updates the wrong row

A user renames a document while the list sorts by name. The save completes, and a different document changes. Stable IDs in the view solve only half the problem. Trace the save completion back to its write. An array offset captured when editing started can now select a different record or fall outside the collection. Even on the main actor, another task can change the collection while the save is suspended. [Identifiable](https://developer.apple.com/documentation/swift/identifiable) · [Swift concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html)

1. At submission, capture the record's identity and the proposed edit. Include account identity when record keys are unique only within an account.
2. On completion, resolve that identity in the current owner. If the record was deleted or the user switched accounts, leave the current list alone. An ordinary array lookup is sufficient for a small list.
3. A second edit to the **same** record still passes an ID check. For last-edit-wins UI, track the current edit token per record and apply success, failure, or pending-state cleanup only to the matching edit. If the server supplies authoritative revisions, reconcile according to its version contract. Suppressing a stale UI update alone cannot order writes at the server.

Use a controllable save client. Pause the first rename, reorder the list, then complete it and assert by document ID that only the renamed document changed. Repeat after deleting the document and assert it stays absent. Finally submit a second rename to the same document, finish it first, and deliver the older success or error. Check the displayed name and pending/error state. An offset used synchronously against an unchanged snapshot is safe within that operation.

## Official sources

- [Migrating to Observation](https://developer.apple.com/documentation/SwiftUI/Migrating-from-the-observable-object-protocol-to-the-observable-macro).
- [Managing model data](https://developer.apple.com/documentation/SwiftUI/Managing-model-data-in-your-app).
- [Swift API design guidelines](https://www.swift.org/documentation/api-design-guidelines/).
