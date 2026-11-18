# Store choice and recovery

For a new feature, compare files and managed stores against the minimum OS, query and relationship needs, interoperability and recovery cost. For an existing store, identify the unmet requirement before migrating. Identify the authoritative copy, its readers, and what each can recover after process death. A widget may rebuild a snapshot. A recorded inspection needs its original units, identity, and correction history.

| Promised outcome | Failure to exercise |
| --- | --- |
| A safe upgrade from a shipped schema | Force an upgrade failure on a copy of a shipped store. Verify the original records and diagnostics survive, and the app offers recovery without reporting an empty replacement as a successful upgrade. |
| A local edit survives an offline export | Terminate after local commit, then again after remote acceptance but before acknowledgement. Resume with the same account and operation identity. |
| A deletion reaches all promised locations | Leave one replica offline. Keep deletion evidence until the replica catches up. Check indexes and exports separately. |
| Credentials remain accessible for intended background work | Exercise the intended device-lock and account-switch states under the selected Keychain access policy. |

## Independent edits in a parent context

A parent's next save can commit pending changes from two editors together. For independent commits, use a writer attached to the store coordinator or isolate everything the parent will save.

Stage edits in both editors, save the first, and reopen through a separate stack. Only the first edit should be on disk. Repeat from a clean fixture and force the durable writer's save to fail. Both stored values should remain unchanged and the failed editor should retain its draft.
