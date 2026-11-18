---
name: apple-data-persistence
description: "Implement SwiftData or Core Data edits that respect Save and Cancel, survive relaunch and recover from failed or ambiguous writes."
---

# Save the changes someone meant to keep

A favorite can change on tap. A rename with Save and Cancel should take effect only at Save. Choose the write boundary before binding the controls.

## Design choices

1. **Isolate cancellable edits.** Hold new input in a value draft until Create. Apply edited fields to the record by ID. Rolling back a shared context can discard someone else’s pending work. <!-- EDIT-001 -->
2. **Make Save match its promise.** Dismiss after the promised write succeeds. A Core Data child save may still need a parent save to reach disk. Retain failed input and distinguish local success from pending sync. <!-- EDIT-002 -->
3. **Retry the original change.** Keep pending work tied to its record, account and operation. Reconcile a lost reply before resending. If the same field changed elsewhere, preserve the draft while resolving the conflict. <!-- EDIT-003 -->

## Try it

Read the result from a fresh context or launch.

- Cancel a rename while another window has starred the same record. Save the star and relaunch. The old name and new star survive. A failed rename stays editable for retry. <!-- EDIT-001 EDIT-002 -->
- For sync, interrupt an acknowledgement after the write commits. Switch accounts before retry. Only the original account should receive the change, once. <!-- EDIT-003 -->

- [A rename meets a newer edit](references/two-editors.md)
