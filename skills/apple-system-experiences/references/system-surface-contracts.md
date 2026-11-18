# System surfaces and framework-specific contracts

Use one domain command and explicit projections, but do not flatten framework semantics into a generic success boolean.

| Surface | Key distinction | Probe |
| --- | --- | --- |
| Widget | Timeline entry, reload request, and displayed freshness | Old data, privacy redaction, delayed refresh |
| Live Activity | Requested activity, system acceptance, update, and end | Stale content, restart, interrupted end |
| Intent/Shortcut | Metadata discovery, entity resolution, and performed action | Cold process, stale ID, denied account |
| Notification | Authorization, subscription, delivery, and routing | Duplicate payload, no-change fetch, disabled alerts |
| Watch transfer | Reachability, queued transfer, received state, and applied command | Reordering, duplication, disconnected devices |
| Health data | Write access, opaque read access, actual samples, and absence | Denial, no data, duplicate export |
| Purchase | Verified transaction, current entitlement, and UI unlock | Pending purchase, refund/revocation, restore |
| Search index | Indexed snapshot, current access, and deep-link resolution | Deleted or cross-account result |

Persist the canonical state before projecting where that is the contract. Keep revision/identity information sufficient to reject stale companion updates. A successful request to a system service is not necessarily visible delivery.

For purchases, use current platform transaction verification and entitlement behavior; do not unlock solely because a local boolean was set or a purchase sheet closed. For HealthKit, lack of readable data cannot identify the user's read-permission decision. For notifications, authorization alone does not prove active subscriptions or successful delivery.

Every surface needs explicit deletion, account change, denial, and stale-data behavior. Minimize exposed fields. Compile target wiring and test the actual host surface/process; app UI tests do not establish widget timelines, shortcut discovery, or companion transport guarantees.

## A widget shows an expired pass as valid

A pass expires at a known time. Supply a timeline entry for its current status and a future entry for expiry. Keep the expiry time visible so a delayed update still gives the person enough information. If the issuer renews the pass early, persist the new expiry first and request a reload for the affected widget kind.

Inspect the provider’s dated entries across expiry with the app closed. Then renew the pass and inspect the replacement timeline and the installed widget separately. Record when the host actually displays the new status.

## Official sources

- [WidgetKit](https://developer.apple.com/documentation/widgetkit).
- [Keeping a widget up to date](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date/).
- [AppIntent protocol](https://developer.apple.com/documentation/appintents/appintent).
- [ActivityKit](https://developer.apple.com/documentation/activitykit).
- [WatchConnectivity](https://developer.apple.com/documentation/watchconnectivity).
- [Protecting user privacy with HealthKit](https://developer.apple.com/documentation/healthkit/protecting-user-privacy).
- [StoreKit](https://developer.apple.com/documentation/storekit).
- [User Notifications](https://developer.apple.com/documentation/usernotifications).
