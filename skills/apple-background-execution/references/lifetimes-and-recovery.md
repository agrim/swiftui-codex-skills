# Expiration, transfer, and recovery contracts

Keep a small state machine: requested, eligible/submitted, running, checkpointed, completed, retryable failure, and terminal failure as applicable. Persist what must survive process death. Do not project an in-memory task handle as durable state.

Select the framework that fits the workload. Short refresh and opportunistic processing are not exact alarms; background URLSession transfers have their own lifecycle. Long-running audio, location, workout, or similar modes require genuine product use and applicable capabilities. Do not add unrelated modes merely to avoid suspension.

Install expiration behavior before starting work. Completion and expiration may race; establish one owner for terminal state. Cancel cooperative work, stop acquiring resources, and preserve a checkpoint consistent with committed side effects. Calling task completion must not falsely claim a partial operation succeeded. Do not call completion twice after a delayed callback.

Use stable operation identity to reconcile repeated launches and retries. A process may die after an external service accepted work but before a local acknowledgement was saved. Check the service's idempotency or reconciliation contract before retrying; a local boolean cannot establish exactly-once delivery.

Schedule subsequent work according to the framework's model and user settings, not a tight retry loop. Account changes and permission revocation can turn retries into terminal or user-action-required states. Surface last successful completion and pending status separately.

Test durable reopen and interrupted operations using controlled dependencies. Debugging hooks can exercise the handler, but only production-like device tests can supply evidence about real scheduling constraints. Record which mechanism and platform were actually exercised.

## Official sources

- [Background Tasks](https://developer.apple.com/documentation/backgroundtasks).
- [URLSession](https://developer.apple.com/documentation/foundation/urlsession).
- [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests).
- [Swift Task cancellation semantics](https://developer.apple.com/documentation/swift/task/cancel%28%29).
