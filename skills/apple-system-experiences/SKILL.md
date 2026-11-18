---
name: apple-system-experiences
description: "Connect app state and actions to widgets, Live Activities, notifications, Spotlight, WatchConnectivity, HealthKit, and StoreKit."
---

# System surfaces and framework integration

## Inputs

Identify the surface, OS, hosting target, device, permissions, and app command or data source.

## Rules

- **SYS-001 — Derive displayed state.** Build widgets, activities, indexes, and companion displays from canonical records. Represent stale and unavailable data explicitly.
- **SYS-002 — Reuse the app command.** Validate parameters and current authority, obtain required confirmation, and reconcile retries before repeating an effect.
- **SYS-003 — Track delivery stages.** Distinguish requesting refresh, queuing a transfer, receiving it, and applying it.
- **SYS-004 — Preserve framework meaning.** Export values only when the system type and units preserve their meaning. Report only permission states the framework discloses.
- **SYS-005 — Check the host.** Verify target embedding, registration, access, data handoff, execution, and host rendering.

## Workflow

1. Define the minimum payload, its identity, and expiration or deletion behavior.
2. Configure the hosting target’s capabilities and privacy declarations. Handle retries and device changes.

## Verify

- SYS-001, SYS-003: Delay delivery or restart the host. The surface shows the last known state or its fallback until fresh data arrives.
- SYS-002: Deliver the same side-effecting operation twice. Check that the store records the effect once.
- SYS-005: After revocation or account switch, the host hides data the viewer can no longer access. Test device-specific behavior on hardware.

## Output

Report the source, host, outcome, configuration changes, and unverified stages.

## References

- [Widget, activity, notification, and companion integration](references/system-patterns.md)
- [Framework-specific delivery and recovery checks](references/system-surface-contracts.md)
