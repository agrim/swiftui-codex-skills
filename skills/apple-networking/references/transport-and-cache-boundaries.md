# Transport, pagination, images, and cache identity

Validate HTTP status, expected content type, decoding, and domain invariants separately. A transport success can still carry an application failure. Preserve cancellation without presenting it as a network error, and sanitize user-facing errors instead of exposing full response bodies.

Retry only when both the error and operation permit it. Distinguish safe reads, idempotent writes, and potentially duplicated side effects. Respect server retry guidance and bound attempts/backoff. A connectivity observation is not proof that a request will succeed; attempt the operation and handle its result.

Cache keys must include relevant account, authorization, query, locale, and representation parameters. Invalidate or partition on account changes. Never let a stale cached success suppress an important authorization error. Label stale data and refresh failure separately so offline functionality does not masquerade as current server state.

For pagination, tie responses to both request generation and query identity. Deduplicate by domain IDs, preserve sort contracts, and guard against repeated/invalid cursors. A stale failure or cleanup path must not clear the current request's loading state.

Image loading needs bounds for network data, decoded pixel dimensions, in-flight work, and memory/disk caches. Downsample for the displayed size where appropriate; compressed byte size alone does not describe decoded memory. Cancel obsolete work and avoid repeatedly decoding during view updates. An `AsyncImage` usage is not a comprehensive cache policy.

Test invalid payloads, unauthorized responses, cancellation, out-of-order pages, repeated cursors, server throttling, oversized images, and account switches. Use isolated transport fakes for ordering, then exercise real platform networking where the claim concerns trust, background delivery, or cache implementation.

## Official sources

- [URLSession](https://developer.apple.com/documentation/foundation/urlsession).
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
- [Keychain services](https://developer.apple.com/documentation/security/keychain-services).
- [Preventing insecure network connections](https://developer.apple.com/documentation/security/preventing-insecure-network-connections).
