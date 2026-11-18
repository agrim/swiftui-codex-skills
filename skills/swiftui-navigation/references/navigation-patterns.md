# Choosing navigation ownership

## What should a width change preserve?

Start with the user's expected return point. An account editor opened from a sidebar should still edit the selected account after the sidebar collapses. If the user must go Back through several records within that detail, model only those steps in its history. For peer tabs, switch away while deep in one tab, return, and compare the path with the product's intended history. Check the same journey on the oldest supported target before sharing a navigation implementation.

## Two windows or two sheets

Open different records in two windows. Change the selection in A while B is loading. If B's editor changes, move ownership of the selection to the scene that presents it. Share durable records independently of the open editor.

When an editor hands off to another sheet, switch rapidly from A to B. Give the transition one owner that knows which draft is pending. Start the replacement from observed dismissal completion if sequencing matters. Fixed delays make the wrong editor harder to reproduce.

For a dirty editor, specify the promised outcome of Cancel, swipe, Escape and Save failure. After each, reopen the record from a different entry point. Only a successful commit may change stored data when the user was promised explicit Save.
