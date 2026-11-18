---
name: apple-networking
description: "Build or review URLSession clients for authentication, retries, cancellation, shared image downloads, pagination, caching, and offline use."
---

# Networking, caching, and remote state

## Inputs

Identify endpoint contract, credentials owner, sensitive data, retry guarantees, cache policy, and consumers.

## Rules

- **NET-001 — Validate responses.** Check HTTP status, expected content, decoding, and domain invariants before publishing success.
- **NET-002 — Bound resource use.** Limit payloads, concurrency, retries, pagination, and cache size. Assign cancellation to the transfer owner.
- **NET-003 — Retry by operation.** Retry only when the failure and operation allow it. Honor server delays. For uncertain writes, reconcile or reuse the server-supported idempotency key.
- **NET-004 — Protect credentials.** Validate certificates, use protected credential storage, and redact tokens and private payloads from diagnostics.
- **NET-005 — Describe offline results.** Label stale data and refresh failures. A cache hit must not hide an authorization failure.

## Workflow

1. Inject the transport. Map cancellation, expiry, invalid data, and empty success to distinct feature outcomes.
2. Scope cache keys by account and representation. Track each shared download’s subscribers and transfer identity.
3. Bind pages to their query, deduplicate by ID, and stop on repeated cursors.

## Verify

- NET-002: Cancel one subscriber to a shared download. The other receives its image. A retired transfer’s callback leaves its replacement intact.
- NET-005: Offline, expired data stays hidden or is labeled stale according to cache policy. Switching accounts hides the previous account’s data.
- NET-001, NET-003: Return malformed data and verify the request reports failure. For a retryable request, keep returning a temporary error and verify retries stop at the configured limit.

## Output

Report retry and cache decisions, fixture results, and real-service checks.

## References

- [HTTP validation, retries, and offline state](references/networking-patterns.md)
- [Pagination, cache identity, and shared downloads](references/transport-and-cache-boundaries.md)
