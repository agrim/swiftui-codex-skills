---
name: apple-system-experiences
description: "Integrate widgets, Live Activities, notifications, Spotlight, WatchConnectivity, HealthKit, and StoreKit."
---

# System surfaces

## Inputs

Identify host, OS, device, permissions, and source.

## Rules

- **SYS-001 — Project records.** Derive content from canonical records. Mark stale or unavailable data.
- **SYS-002 — Share commands.** Check inputs, authorization, and required confirmation. Reconcile retries.
- **SYS-003 — Track delivery.** Separate refresh requests, queued transfers, receipt, and application.
- **SYS-004 — Preserve meaning.** Match exported types and units. Report only observable permission states.
- **SYS-005 — Verify the host.** Check embedding, registration, access, payload handoff, execution, and rendering.

## Workflow

1. Configure host capabilities and declarations. Define payload identity, expiry, and deletion.

## Verify

- SYS-001, SYS-003: Delay delivery across restart. The host marks stale data or shows its fallback.
- SYS-002: Deliver a command twice. Its effect appears once.
- SYS-004, SYS-005: Revoke access or switch accounts on-device. Inaccessible records disappear without a fabricated permission status.

## Output

Report source, host, configuration, outcome, and gaps.

## References

- [Surface integration](references/system-patterns.md)
- [Delivery and recovery checks](references/system-surface-contracts.md)
