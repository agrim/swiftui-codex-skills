---
name: apple-networking
description: "Build or review URLSession authentication, retries, cancellation, shared downloads, pagination, caching, and offline behavior."
---

# Handle failed requests without losing data or repeating a write

Use this when building a URLSession feature or fixing stale results, repeated writes, or downloads that stop when a view disappears.

## Start here

Pick a request and identify its account, expected response, cache lifetime, and callers. Use a fake transport to control when it completes.

## How to proceed

1. **Decide what counts as success.** Interpret the status and decoded body for that endpoint. Decide which failures leave an existing record usable. <!-- NET-001 -->
2. **Limit how much work a request can start.** Limit payloads, parallel requests, cache size, and pages. Stop repeated cursors and deduplicate records per query. Cancel a shared download when its last subscriber leaves. <!-- NET-002 -->
3. **Retry only when safe.** Cap transient retries and honor the server’s delay. If a write may have succeeded, confirm its outcome or reuse an operation key the server recognizes. <!-- NET-003 -->
4. **Protect the account during diagnosis.** Keep production certificate checks enabled. Capture sanitized status and request IDs while excluding private URLs, tokens and response bodies. <!-- NET-004 -->
5. **Decide when to show cached data.** Separate entries by account and representation. Mark or hide expired data and show refresh or access failures even when a cached record exists. <!-- NET-005 -->

## Check the result

- Return an empty 204 to a Delete that allows it and a Fetch that promises a record. Only Delete should succeed. Reject malformed private data without logging it, and stop repeated failures at the retry limit. <!-- NET-001 NET-003 NET-004 -->
- Cancel one of two subscribers. The other receives its image. After both leave, deliver an old callback to a same-key replacement. Only the new transfer may update the cache. <!-- NET-002 -->
- Go offline and switch accounts. Expired data follows the stated policy and private entries from the first account stay hidden. <!-- NET-005 -->

## What to report

Describe the request, how the caller recovers, and which outcomes you observed with the test transport or a live connection.

- [HTTP failures, retries, and offline data](references/networking-patterns.md)
- [Late pages, shared downloads, and thumbnail sizes](references/transport-and-cache-boundaries.md)
