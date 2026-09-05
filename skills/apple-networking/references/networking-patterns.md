# Networking, caching, and remote state: playbook

## Client contract

Use a typed client protocol or another established injection seam so views do not own HTTP details. Return domain values rather than exposing arbitrary response dictionaries throughout the UI. Keep transport errors, HTTP status, decoding errors, and domain validation distinguishable internally; provide concise actionable messages to users.

A successful `URLSession` transfer can contain an HTTP error response. Validate status and the expected representation before decoding or reporting success. Handle empty successful responses according to the endpoint contract. Bound downloads and decoded data where untrusted or large responses could exhaust memory.

## Authentication and trust

Keep credentials in an appropriate protected store and avoid embedding server secrets in the app. Prevent refresh storms with a single coordinated refresh operation where needed. Scope cached responses, pending requests, and publications to the current account; invalidate old generations on logout. Do not infer authorization solely from a UI flag.

Retain platform TLS validation and transport security. A development server problem is not justification for a global production bypass. Certificate pinning is not a universal requirement: it adds rotation and recovery obligations and needs a specific threat model. Redact tokens, authorization headers, personal URLs, and payload content from diagnostics.

## Retry decision table

| Failure | Default decision to evaluate |
| --- | --- |
| User cancellation | Stop; do not show it as an unexpected failure |
| Invalid request or forbidden operation | Repair input/authorization; do not blindly retry |
| Expired credentials | Coordinate refresh according to the service contract |
| Rate limit or temporary service error | Respect server guidance and use bounded backoff with jitter |
| Interrupted read | Retry only within the product's latency/resource budget |
| Uncertain non-idempotent write | Reconcile or use a supported idempotency key before retrying |

A timeout after a write does not prove the server did nothing. Retrying every POST can duplicate purchases, records, or external exports. Separate transport retry from a durable domain-operation retry.

## Caching and images

Honor HTTP caching semantics when appropriate, then define any product-specific freshness requirement explicitly. Cache keys must include relevant request variants and account scope. Bound memory and disk storage, remove protected data on the promised lifecycle, and show stale content honestly.

For images, constrain decoded dimensions, cancel abandoned loads, and avoid doing heavy decoding repeatedly on the main actor. Deduplicate simultaneous identical requests when beneficial. `AsyncImage` can be a useful display primitive; do not promise that it supplies an arbitrary persistent cache, authenticated image pipeline, or resource budget by itself.

## Pagination and ordering

Track cursors and in-flight state explicitly. Deduplicate by stable record IDs, preserve server ordering rules, and handle records changing between pages. A new filter/query invalidates the old pagination generation. Guard success, failure, and cleanup so an obsolete request cannot append data or clear the current spinner.

Do not treat a connectivity monitor as proof that the next request will succeed. Attempt the operation, classify the actual result, and offer the correct recovery.

## Test seams

Use an injected transport or controlled `URLProtocol` fixture for deterministic status, headers, body, and delay behavior. Keep fixture state isolated because tests may run in parallel. Test response sequences, not only one successful JSON sample. Integration tests against a real service have different prerequisites and must never be reported as run when only mocks passed.

## Sources

- [urlsession](https://developer.apple.com/documentation/foundation/urlsession) — URLSession.
- [keychain](https://developer.apple.com/documentation/security/keychain-services) — Keychain services.
- [concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) — The Swift Programming Language: Concurrency.
- [privacy](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests) — Describing data use in privacy manifests.
