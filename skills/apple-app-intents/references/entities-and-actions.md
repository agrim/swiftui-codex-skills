# When a shortcut picks the wrong note or runs a move twice

## A saved shortcut belongs to another account

Save a “Move note” shortcut while signed into account A, then run it under B with the app closed. The shortcut still has the ID selected under A. Look it up among the records B can access. If it is unavailable, leave A’s note title out of suggestions and error messages. Choosing B’s first suggestion as a fallback could move an unrelated note.

To narrow a failure, find the first difference between the shortcut and the in-app move. If the action is missing, inspect the installed build. If the action appears but the note is missing, compare the ID that the entity query received with the records it returned for the active account. If the right note is found but never moves, follow the save and the result returned to Shortcuts.

## Asking for a folder causes a duplicate move

Suppose the intent archives the original note and then discovers it needs a destination. If it throws `needsValueError(_:)`, the system can run `perform()` again after the person answers. Ask for the folder before calling the shared move operation.

Run the shortcut twice with the folder omitted. Cancel the first prompt and check that the original note stays put. Answer the second prompt and confirm exactly one move to that folder. If delivery of the reply is interrupted, reconcile the saved outcome before retrying. Use a durable operation ID when the app can reliably identify a repeat.
