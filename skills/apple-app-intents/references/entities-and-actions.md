# Entity resolution and invocation failures

## A saved selection belongs to another account

Save a shortcut under account A. Switch to B and invoke it with the app closed. Resolve the stored ID against B’s accessible records. If unavailable, keep A’s display name out of suggestions and errors. Substituting B’s first suggestion would target the wrong record.

When an invocation fails, record the last stage that succeeded in the shipping host. Missing metadata, an undiscoverable action, a stale entity, and a command that never committed need different fixes. Cold invocation should work before any scene initializes the store.

## A missing parameter restarts a move

A move-note shortcut archives the original before asking for its destination. Throwing `needsValueError(_:)` here can repeat that archive when the person answers. Resolve the destination and obtain required confirmation before calling the app’s move command. For an interrupted write, reconcile its durable operation ID before retrying.

Cancel the missing-destination prompt and inspect the original note. Invoke again, answer the prompt, and count one committed move across both passes through the intent.
