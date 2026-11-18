---
name: apple-background-execution
description: "Handle BGTaskScheduler, background transfers, expiration, and relaunch recovery."
---

# Background execution

## Inputs

Identify workload, capabilities, and resource limits.

## Rules

- **BG-001 — Track progress.** Separate submission and eligibility from observed launch and completion.
- **BG-002 — Checkpoint effects.** Persist the operation ID and last committed step.
- **BG-003 — Own completion.** Give expiration, cancellation, and late callbacks one owner for terminal state.
- **BG-004 — Match workloads.** Match the workload’s duration and delivery needs to an eligible mechanism.
- **BG-005 — Qualify evidence.** Measure scheduling and energy on unforced device runs. Label forced launches.

## Workflow

1. Follow one bounded work unit from the configured target to its checkpoint.
2. On relaunch, reauthorize and reconcile unacknowledged effects.

## Verify

- BG-002, BG-003: Expire during commit. Completion fires once and the checkpoint matches stored effects.
- BG-002: Lose the acknowledgement and relaunch. Reconcile before retrying. Without a reliable outcome, keep it pending. Revoked access prevents new effects.
- BG-001, BG-004, BG-005: For short refreshes, trace a BGAppRefreshTaskRequest to its handler on-device. Record submission and launch separately. Exclude forced runs from timing estimates.

## Output

Report mechanism, checkpoint, retry policy, and outcomes.

## References

- [Expiration, transfer, and recovery](references/lifetimes-and-recovery.md)
