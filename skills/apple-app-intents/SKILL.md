---
name: apple-app-intents
description: "Build and verify App Intents, AppEntity queries, and App Shortcuts."
---

# App Intents and Shortcuts

## Inputs

Identify the action, host, account, and entity.

## Rules

- **INT-001 — Share commands.** Resolve parameters, then call the UI’s validated command. Reconcile retries.
- **INT-002 — Trace invocation.** Check metadata extraction, discovery, resolution, then execution.
- **INT-003 — Resolve IDs.** Look up stable IDs in the active account. Reject missing entities.
- **INT-004 — Limit disclosure.** Minimize exposed fields. Apply required authentication and confirmation.
- **INT-005 — Start cold.** Initialize dependencies in the executing process. Respect its actor and time budget.

## Workflow

1. Inspect the host’s built metadata. Find and run the action on its system surface.

## Verify

- INT-002, INT-005: Invoke cold. The result matches the stored effect.
- INT-003, INT-004: Switch accounts. A stale ID reveals nothing and changes nothing.
- INT-001, INT-004: Deny required authentication and observe zero writes. Replay a committed operation ID and count one effect.

## Output

Report host, command, entity, effect, and gaps.

## References

- [Entity resolution and invocation](references/entities-and-actions.md)
