---
name: apple-data-persistence
description: "Choose SwiftUI draft ownership and SwiftData or Core Data save boundaries so Cancel, retries and reopening preserve the right edits."
---

# Save the changes someone meant to keep

An immediate favorite and an editor with Save and Cancel make different promises. Choose where the write occurs before binding controls to a persistent model.

## Design choices

1. **Keep a cancellable draft outside the stored record.** For a new SwiftData item, a small value held in the sheet can own the input until Create. For an existing record, apply the edited fields to its current identity. Discarding a draft should leave a second editor’s changes intact. <!-- EDIT-001 -->
2. **Close the editor after the promised write succeeds.** Give failures a recoverable draft. For Core Data, check whether a child-context save still needs a parent save to reach the store. If the product syncs, distinguish a local commit from cloud delivery. <!-- EDIT-002 -->
3. **Tie pending work to its record and account.** Reconcile an uncertain write before repeating it. If two editors change the same field, keep the draft available while resolving which value to use. <!-- EDIT-003 -->

## Try it

Reopen the store and inspect the record a person would see.

- Open Create, type, dismiss and relaunch. No placeholder appears. Rename an existing record while another window favorites it, then force a save failure. The favorite survives and the draft can be retried. <!-- EDIT-001 EDIT-002 -->
- For synced edits, lose the reply after an accepted write, switch accounts, then reconnect. Confirm one change in the intended account. <!-- EDIT-003 -->

- [A rename meets a newer edit](references/two-editors.md)
