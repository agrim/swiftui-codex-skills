# Host delivery and recovery checks

## A widget shows an expired pass as valid

The expiry is known when the pass is issued. Supply entries for the current state and the expiry transition. Keep the expiry time visible in case presentation is delayed. When the issuer renews early, persist the new expiry before requesting a reload of the affected widget kind.

With the app closed, inspect the entries spanning expiry. Renew the pass and inspect the replacement timeline and installed widget separately. Record when the host displays the new status.

## Check the affected host

| Failure to exercise | Observable result |
| --- | --- |
| Interrupt an activity’s end or dismissal. | Its last visible state and the reopened app agree about whether the underlying event is still active. |
| Deliver a notification twice, or deliver one with no new records. | A repeated command has one effect. A no-change fetch produces no new-data alert. |
| Open a search result after deletion or an account switch. | The deep link exposes no stale record. |
| Reconnect a watch after two revisions and a repeated command. | An old revision cannot replace the current one. The command commits once. |
| An export is interrupted and the next HealthKit read returns no samples. | The recorded workout survives and read permission stays unknown. Reconcile the earlier export before writing again. |
| Leave a purchase pending, then revoke an existing entitlement. | The pending transaction grants nothing. The next entitlement check reflects revocation. |
