# System surfaces and framework integration: playbook

## Integration matrix

| Surface | Own explicitly | Never infer |
| --- | --- | --- |
| WidgetKit | Timeline/snapshot data, freshness, family layout, shared storage | Reload request means immediate visible refresh |
| App Intents | Entity resolution, command authorization, execution mode, result | A resolved phrase authorizes any side effect |
| ActivityKit | Activity identity, content state, stale/end transitions | A Live Activity is an unrestricted background process |
| Notifications | Authorization, subscription, delivery/routing, minimal payload | Registration proves a notification was delivered |
| Core Spotlight | Indexed projection, identifier, deletion, deep-link recovery | Search metadata is a separate canonical store |
| WatchConnectivity | Versioned messages, identity, acknowledgement, deduplication | Reachability or send success proves durable remote commit |
| HealthKit | Supported types, units, scope, provenance, authorization semantics | Empty reads prove permission was denied |
| StoreKit | Verified transactions, entitlement state, pending/revoked changes | A tapped purchase button or unverified result proves access |

## Widgets and Live Activities

Use a small, stable projection of canonical state. Include enough identity/version/freshness information to distinguish stale content from current truth. App groups and target embedding must be verified in the built products. Separate preview snapshots from production timelines and actual host rendering.

A timeline or reload request is not a promise of an exact refresh interval. Design content that remains useful when refresh is delayed. Avoid app-style continuous loops inside widgets. For Live Activities, distinguish creation, update, stale state, ending, dismissal, and the related in-app process. Ending the app task and ending the system surface must not silently disagree.

## Intents and system commands

Expose specific typed actions and entities. Resolve parameters, check account/permission, obtain confirmation where the action requires it, and invoke a shared command service. Return a truthful result only after the promised operation reaches its completion boundary. Keep presentation routing on the correct actor and match execution mode to the current documented API.

A language model or natural-language parser may propose a typed command; deterministic code still owns authorization, validation, persistence, idempotency, and audit. Do not implement an unrestricted “do anything” intent that bypasses the app's normal safeguards.

## Notifications and search

Keep authorization, remote registration, requested subscription coverage, background fetch, and visible alerts separate. Minimize payloads and resolve sensitive content within the app when possible. Repeated delivery must not repeat a destructive command. A background fetch with no new data is not evidence for a “new data” alert.

Index only the promised discoverable projection. Delete or update indexed records when canonical data changes, and handle stale search results gracefully. A cold-launch deep link must revalidate access rather than trust the index blindly.

## Paired devices

Choose the transport method for latest-state replacement versus durable queued transfer; verify current framework guarantees. Version messages and include operation identity where duplicate application matters. Handle delayed, reordered, and duplicate delivery; reconcile after reconnect and process termination. Keep provisional observations distinct from authoritative committed records. Do not merge data from a prior account or generation into the current session.

## Health and protected records

Keep app-specific detail in the canonical store and export only a semantically supported system representation. Preserve units, timestamps, source/provenance, user corrections, and deletion rules. HealthKit deliberately limits what can be inferred about read authorization: no returned samples are not proof of denial. Verify the exact read/write status APIs before displaying permission claims. A workout duration alone does not encode arbitrary exercise, set, or repetition semantics.

## Purchases

Use verified transaction information for entitlements, handle pending/cancelled/revoked/expired states, and reconcile updates/restoration using the current StoreKit contract. Keep product display, local entitlement cache, server authority when present, and transaction acknowledgement distinct. Review current store rules for the shipped business model and region; do not hard-code remembered policy into a universal rule.

## Validation

Prove the affected chain in order: configuration → permission → data/command → host execution → rendering → delayed refresh/retry → restoration/deletion. Test the actual watch, system account, purchase sandbox, or hardware when those boundaries matter. A compiled extension and an app screenshot do not establish system integration correctness.

## Sources

- [widgets](https://developer.apple.com/documentation/widgetkit) — WidgetKit.
- [intents](https://developer.apple.com/documentation/appintents) — App Intents.
- [activities](https://developer.apple.com/documentation/activitykit) — ActivityKit.
- [notifications](https://developer.apple.com/documentation/usernotifications) — User Notifications.
- [spotlight](https://developer.apple.com/documentation/corespotlight) — Core Spotlight.
- [watch-connectivity](https://developer.apple.com/documentation/watchconnectivity) — WatchConnectivity.
- [healthkit](https://developer.apple.com/documentation/healthkit) — HealthKit.
- [storekit](https://developer.apple.com/documentation/storekit) — StoreKit.
- [widget-refresh](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date/) — Keeping a widget up to date.
- [health-authorization](https://developer.apple.com/documentation/healthkit/hkhealthstore/authorizationstatus(for:)) — HealthKit authorizationStatus(for:).
- [health-privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — Protecting user privacy with HealthKit.
- [app-intent](https://developer.apple.com/documentation/appintents/appintent) — AppIntent protocol.
