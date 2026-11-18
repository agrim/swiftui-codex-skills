---
name: apple-data-persistence
description: "Design editing and persistence so people can tell what was saved, recover failed work, and keep their changes when sync is part of the feature."
---

# Save the changes someone meant to keep

A star toggled in a list can take effect immediately. A form with Save and Cancel makes a different promise. Decide which edits someone can abandon and when they can count on finding a change again.

## Design choices

1. **Match ownership to the editing promise.** For immediate edits, update the model directly. For Save and Cancel, edit a draft and commit it to the intended record on Save. Cancel discards only that draft, even when another editor has made changes. <!-- EDIT-001 -->
2. **Make success mean something durable.** Dismiss a Save form after its write succeeds. On failure, keep the input available for repair. If saving locally is enough, finish there. If the app promises delivery to another device, distinguish a local save from a pending or acknowledged upload. <!-- EDIT-002 -->
3. **Resolve competing writes when they can happen.** Tie pending work to its record and, in a multi-account app, its account. When a reply is lost, reconcile the original operation before sending it again. If another editor changed the same field, keep the draft available while resolving which value to keep. <!-- EDIT-003 -->

## Try it

Reopen the record to see which changes actually stuck. Exercise the boundaries this feature supports.

- Cancel a rename while another editor saves a different change. Then make a save fail. The other change survives, the cancelled name never appears, and the failed draft remains editable. <!-- EDIT-001 EDIT-002 -->
- For synced edits, lose the reply after a successful upload, switch accounts, then return and reconnect. The original account ends up with one change and the other account sees none. <!-- EDIT-003 -->

- [A rename meets a newer edit](references/two-editors.md)
