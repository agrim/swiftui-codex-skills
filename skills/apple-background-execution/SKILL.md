---
name: apple-background-execution
description: "Handle BGTaskScheduler, background transfers, expiration, and relaunch recovery."
---

# Background execution and resumable work

## Inputs

Identify the user benefit, target capabilities, resource limits, and state to preserve.

## Rules

- **BG-001 — Track actual progress.** Distinguish submission, eligibility, launch, and completion. An earliest start date promises no launch time.
- **BG-002 — Save resumable state.** Persist the operation ID and a checkpoint consistent with committed effects before suspension.
- **BG-003 — Handle expiration.** Install a background task’s expiration handler before starting work. Coordinate cancellation and completion to report one terminal result per task.
- **BG-004 — Match the mechanism.** Select refresh, processing, transfer, or an active-session mode documented for the workload.
- **BG-005 — Label the evidence.** Label forced launches. Use unforced, production-like device runs for scheduling or energy claims.

## Workflow

1. Register the handler and capabilities on the executing target. Bound each work unit.
2. On relaunch, recheck account access and reconcile unacknowledged effects before retrying.

## Verify

- BG-002, BG-003: Expire during I/O or commit. A late callback leaves the checkpoint intact and completion fires once.
- BG-002: Relaunch with the same operation ID after network loss. Committed effects survive without duplication.
- BG-001, BG-002: Revoke access before resuming. Protected work stays pending or fails without advancing its checkpoint.

## Output

Report the mechanism, checkpoint, retry policy, and observed outcomes.

## References

- [Expiration, transfer, and recovery](references/lifetimes-and-recovery.md)
