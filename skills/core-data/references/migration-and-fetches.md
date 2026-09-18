# Fetch performance and schema evolution

Start from a measured query or import. Restrict predicates, fetched properties, fetch limits, batching, and relationship prefetching according to the UI's actual needs. Avoid firing faults in a rendering hot path. Resetting a context releases registered state but also invalidates references; do not reset a shared editing context as a memory workaround.

Choose a conflict policy by deciding whose changes may be discarded. Store-trump, object-trump, and manual reconciliation are product semantics. Test an unsaved local edit against a background update rather than treating a merge-policy switch as a harmless crash fix.

Migration fixtures should contain representative historical relationships, optional values, large collections, and malformed legacy records. Match old and new model versions explicitly. Use lightweight, staged, or manual migration according to supported changes and toolchain availability. An accidental model checksum or identifier change can be material even when a Swift class rename looks cosmetic.

Check the final store through a fresh container and a second reopen. Keep a failing original store intact, document the recovery path, and do not treat a fallback in-memory container as successful production launch. For mirroring, validate both schema compatibility and runtime account/cloud behavior; local fetch success is not synchronization proof.

## Official sources

- [Core Data concurrency programming guide (archived)](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/Concurrency.html).
- [Core Data batch delete guide (archived)](https://developer.apple.com/library/archive/featuredarticles/CoreData_Batch_Guide/BatchDeletes/BatchDeletes.html).
- [Consuming relevant store changes](https://developer.apple.com/documentation/coredata/consuming-relevant-store-changes).
- [CloudKit](https://developer.apple.com/documentation/cloudkit).
