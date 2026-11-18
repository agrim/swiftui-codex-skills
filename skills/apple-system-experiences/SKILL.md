---
name: apple-system-experiences
description: "Choose what a widget, shortcut or notification should let someone see or do, including when its saved context has gone stale."
---

# Extend an app task beyond the open app

Ask what someone gains by staying outside the app. A widget can show the next departure at a glance. A shortcut can mark a known item complete. If the person needs to compare several records before deciding, open the app at that choice.

## Design choices

1. **Choose how much of the task belongs outside.** Show enough context for a confident decision. If yesterday’s cached time could look like a live departure, show when it was updated or offer to open the schedule. Hand off to the relevant item when the surface runs out of context. <!-- SURFACE-001 -->
2. **Treat a saved selection as a request.** Resolve the item against the account and permissions available at invocation, including before any window opens. If access changed, give a neutral way to choose again without exposing the old item’s details. <!-- SURFACE-002 -->
3. **Use the operation the app already trusts.** Let the surface supply inputs and the existing app operation decide whether the change can succeed. Collect missing choices before committing. Report completion only when the promised effect took place. <!-- SURFACE-003 -->

## Try it

For a saved action, compare its response with the record you find on returning to the app.

- Run the saved action with the app closed. Cancel a required choice, then run it to completion. Only the completed attempt changes the intended record. <!-- SURFACE-001 SURFACE-003 -->
- Save the action in one account and invoke it in another that lacks access. Both accounts keep their data and the old record’s private details stay hidden. <!-- SURFACE-002 -->

- [Should “Move note” run in Shortcuts or open the app?](references/a-saved-action.md)
