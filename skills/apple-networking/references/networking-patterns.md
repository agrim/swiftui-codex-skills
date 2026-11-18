# Response, retry, and offline decisions

For each endpoint, decide what the UI may publish. A 204 can complete a delete while the same empty body fails a fetch that promises a record. Feed both through the injected transport and check each caller's recovery.

| Outcome | Next action |
| --- | --- |
| Caller cancels | Release its wait without presenting a network failure. |
| Credentials expire during concurrent requests | Coordinate one refresh per account where supported. Discard its result if the session was replaced. |
| Request is forbidden | Surface the access failure even when an older cached response exists. |
| A read is interrupted or throttled | Attempt recovery within latency and retry budgets. Respect the server's retry delay. |
| The response to a write is lost | Reconcile the operation or reuse its server-supported idempotency key before retry. |

An offline cache may serve yesterday's data if the feature permits it. Decide whether to hide or mark it stale, when to evict private entries, and what happens if refresh fails after a cache hit. Use actual request outcomes to choose recovery.

For a credential refresh incident, capture status, sanitized error, and request identity. Exercise simultaneous expiry and logout. A failing fixture should leave usable diagnostics without exposing credentials, private URLs, or response bodies. Verify transport trust and cache behavior on the real platform where those properties matter.
