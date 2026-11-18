---
name: apple-app-intents
description: "Implement App Intents, AppEntity queries, and App Shortcuts. Verify authorization and cold invocation."
---

# App Intents, entities, and system actions

## Inputs

Identify the action, entity, host, actor, account, and access policy.

## Rules

- **INT-001 — Share the command.** Resolve parameters and call the UI’s validated operation. For retried writes, reconcile the previous outcome.
- **INT-002 — Check each stage.** Distinguish extracted metadata, host discovery, entity resolution, and the effect of `perform()`.
- **INT-003 — Resolve current identity.** Look up stable entity IDs within the active account. Handle deleted or inaccessible entities without recreating them.
- **INT-004 — Limit disclosure.** Expose only necessary fields in suggestions, labels, results, and logs. Apply the action’s authentication and confirmation policies.
- **INT-005 — Support cold invocation.** Initialize services in the executing process. Use the actor and time budget for this execution mode.

## Workflow

1. Build the hosting target. Inspect embedded metadata and find the action in its system surface.
2. Resolve the selected entity and invoke the action from that surface.

## Verify

- INT-002, INT-005: With the app closed, invoke the discovered action. Its reported result matches the domain outcome.
- INT-003, INT-004: After an account switch, a stale ID yields no private details or unauthorized mutation.
- INT-004: When the policy requires authentication, a signed-out invocation leaves data unchanged.
- INT-001: Retry a committed write using the same durable operation ID. The effect occurs once.

## Output

Report the command, host, resolved entity, observed effect, and untested paths.

## References

- [Entity queries, shared commands, and invocation checks](references/entities-and-actions.md)
