---
name: apple-networking
description: "Build or review URLSession authentication, retries, cancellation, shared downloads, pagination, caching, and offline behavior."
---

# Networking and caching

## Inputs

Identify endpoint, credential owner, sensitive fields, cache policy, and consumers.

## Rules

- **NET-001 — Validate success.** Check HTTP status, representation, decoding, and domain invariants.
- **NET-002 — Bound work.** Limit payloads, concurrency, attempts, pages, and caches. Assign cancellation ownership.
- **NET-003 — Retry eligible operations.** Retry only recoverable failures and honor server delays. Reconcile uncertain writes or reuse a server-supported idempotency key.
- **NET-004 — Protect credentials.** Validate certificates, protect stored credentials, and redact private payloads and tokens.
- **NET-005 — Expose freshness.** Label stale data. Surface refresh and authorization errors even on cache hits.

## Workflow

1. Inject transport. Distinguish cancellation, expiry, malformed data, and empty success.
2. Partition caches by account and representation. Track transfer IDs and subscribers. Scope pages to queries, deduplicate IDs, and stop repeated cursors.

## Verify

- NET-002: Cancel one subscriber. Its peer still receives the image. Late callbacks leave the replacement transfer intact.
- NET-005: Offline, hide or label expired data per policy. Switching accounts hides prior entries.
- NET-001, NET-003, NET-004: Reject malformed private data without logging it. Repeated transient errors stop at the retry limit.

## Output

Report retry and cache policies, fixture results, and live checks.

## References

- [HTTP and offline behavior](references/networking-patterns.md)
- [Pagination and shared downloads](references/transport-and-cache-boundaries.md)
