---
name: apple-system-experiences
description: "Choose a widget, Live Activity or shortcut for an app task and verify its freshness, permissions and result from the system surface."
---

# Extend an app task beyond the open app

A widget shows the next train. A Live Activity follows the trip underway. A shortcut can file a known note. If filing requires comparing notes, open the collection.

## Design choices

1. **Define when the display becomes misleading.** Give the widget a source time and its next known state. Decide when a Live Activity grows stale and what ends it. Limit lock-screen details. <!-- SURFACE-001 -->
2. **Resolve saved choices again.** On invocation, look up the record ID in the active account, even on cold launch. If the record is gone or inaccessible, offer a fresh choice without naming private content. <!-- SURFACE-002 -->
3. **Call the app’s existing operation.** Resolve missing inputs, then use the UI’s validated move or save. When an App Intent is missing from Shortcuts, check build-time metadata extraction and installed discovery first. <!-- SURFACE-003 -->

## Try it

Compare the system’s answer with the app’s record.

- Expire the feed offline. The widget shows dated or unavailable data. End a Live Activity and verify its final state and dismissal policy. <!-- SURFACE-001 -->
- Run a saved shortcut cold. Cancel its prompt, complete a second attempt, then switch to an account with a same-named folder. Only the authorized move takes effect. <!-- SURFACE-002 SURFACE-003 -->

- [Should “Move note” run in Shortcuts or open the app?](references/a-saved-action.md)
- [A widget still shows a departed train](references/widget-timeline.md)
