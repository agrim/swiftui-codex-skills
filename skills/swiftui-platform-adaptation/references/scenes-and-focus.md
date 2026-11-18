# Window identity, commands and reopening

## Opening the same record creates a second editor

Decide whether the request means “another workspace” or “return to this record.” For the latter, address a data-presenting window group with the stable record ID. Include the group ID when several groups accept the same value type. Inspect the value sent by the caller before adding a private window registry.

On a multiwindow destination, open A twice and B once. Expect one editor per record and A's unsaved draft when A comes forward again. Restore after B was deleted. B should offer recovery without recreating its record or altering A.

## A menu shortcut edits the previous window

Open two different selections. Switch windows without clicking a row, invoke the shortcut, then undo. If the previous selection changes, trace the command's focused receiver before changing the shared data model. Repeat with an empty selection and verify the command is disabled.

For a menu-bar utility, close the last content window and try opening Settings from its intended entry point. Document whether reopening should present the last document, a fresh window or just the menu. Reproduce that specific launch failure before changing app activation policy or adding AppKit interop.
