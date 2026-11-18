# Interrupted work and recovery

## An upload succeeded before the app saved its acknowledgement

After relaunch, recover the operation ID and ask the service whether it accepted the upload. If the outcome is unknowable and a repeat could create another record, leave the operation pending. Check account access again before resuming. Surface the last confirmed completion separately from pending work.

Exercise expiration immediately before and after commit, then deliver the original completion callback. Inspect both the service and the local checkpoint. The task reports one terminal result and the checkpoint advances only for confirmed work.

## The device locks before the checkpoint reopens

An export uses a checkpoint protected by `FileProtectionType.complete`. Preserve the checkpoint when a locked-device read fails. Starting another export at this point could repeat an accepted upload. Defer work until the file is accessible under its existing protection policy.

Interrupt after the service accepts the upload. Attempt recovery while locked, then unlock and resume. Check that the same operation ID reconciles to one upload.
