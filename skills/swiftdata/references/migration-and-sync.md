# Migration and sync evidence

For a rename, preserve the old stored field's identity. For a new uniqueness constraint, choose the survivor of each collision and reattach its relationships before enforcing the constraint. Keep a fixture with conflicting rows even if current forms prevent users from creating them.

## Exercise an upgrade on disk

1. Write two distinguishable business ID–value pairs with the frozen source schema at an explicit disk URL, with CloudKit disabled. Include the relationships or collisions under test. Save and release the old container and its models.
2. Open that URL with the destination schema and the app's ordered migration plan. Fetch from a fresh context. Compare values, defaults, and relationship destinations by business ID.
3. Save a destination-only edit and reopen the same store again. Verify both the edit and the other migrated values. Record source, destination, SDK, and runtime.

A fixture generated today can miss a bug in an older shipping build. For such incidents, repeat the upgrade on a sanitized, store-consistent copy from that release. Preserve the original for recovery if opening fails.

## Existing cloud clients

Check the proposed schema against CloudKit's compatibility rules before shipping it. Run an older supported client through a remote edit and deletion while briefly offline. Confirm the promised state at its destination after reconnecting. If clients consume history, retain transactions until every required consumer has durably processed them.
