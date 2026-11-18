# Rename a walk while its favorite changes

Window A opens a walk called Ridge. Window B favorites it while A is typing. If A writes back its entire opening snapshot, Save can silently remove B’s favorite. Hold the record ID, original name and edited name in A’s draft. Fetch the current record when saving and change only the name. Resolve a same-field conflict if the current name differs from the one A opened.

Cancel drops A’s draft. Calling `rollback()` on a shared SwiftData context would also discard other pending inserts, updates and deletes. If the design needs context-level rollback, isolate the writer. After a failed write, retain the input and prevent an abandoned pending mutation from leaking into a later autosave. Reopen the store after an unrelated successful save to check that boundary.

**If sync is promised.** A timeout after the server accepts a creation leaves the outcome unknown. Reuse its original operation ID when supported, or look up the accepted result before retrying. If the service offers neither, keep the outcome unresolved and offer recovery.

Reorder the list before delivering a delayed reply. A completion for Ridge must never rename the row now in Ridge’s former position.
