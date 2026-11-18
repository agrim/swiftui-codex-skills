# Drafts, commits, and exports

## Define what Cancel preserves

An autosaved document and a form with an explicit Save button promise different outcomes after interruption. For the form, validate a value draft before inserting it. If an editor needs tracked changes, isolate its writer and choose its autosave policy before editing. Roll back only that writer on failure. Stage another editor's unsaved work while cancelling or failing the first, then verify that the second can still save.

The example suite's `DraftNoteStoreTests` inject a pre-save failure in an in-memory SwiftData store. Retrying that failure checks draft recovery. Repeated *successful* Create operations intentionally produce distinct records.

## Decide which value leaves the app

An inspection targets 12 items, estimates 10, then confirms 9 after a correction. History and export use the confirmed 9 and its unit. Keep the plan, estimate, and correction provenance available. Represent an unknown count separately from a confirmed zero. Whole-item counts reject fractions even if the keyboard accepts them.

Repeating an inspection starts a draft without an observed result or export acknowledgement. Decide whether the new target comes from the plan or the prior result. Cancel the repeat and check that the prior inspection and its export remain intact.
