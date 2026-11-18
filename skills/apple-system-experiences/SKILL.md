---
name: apple-system-experiences
description: "Choose and verify a WidgetKit glance, Live Activity or App Intent that reflects the app’s real state, account and actions."
---

# Extend an app task beyond the open app

A widget can answer “when is the next departure?” A Live Activity can follow a trip already underway. A shortcut can file a known note. If the person needs to compare alternatives, open the app at that choice.

## Design choices

1. **Choose the surface by how the value changes.** Give a WidgetKit entry a source timestamp and a useful expired state. For a Live Activity, decide what ends the session. Publish the smallest useful snapshot from the app’s owner and account for what a bystander can see. <!-- SURFACE-001 -->
2. **Resolve saved choices at invocation.** A shortcut or widget link can outlive the record or account that created it. Resolve identity and access before opening private content, including on cold launch. Offer a neutral way to choose again when access changes. <!-- SURFACE-002 -->
3. **Give App Intents the app’s existing operation.** Resolve missing parameters, then call the same validated move or save as the UI. If the action is missing, check the built target’s metadata and discovery in Shortcuts before debugging persistence. <!-- SURFACE-003 -->

## Try it

Run the task from the actual system surface.

- Cross a widget entry’s freshness deadline or end a Live Activity. Compare its displayed time, state and destination with the app. <!-- SURFACE-001 -->
- Run a saved action cold, cancel its required prompt, then complete it. Switch accounts and invoke it again. Only the authorized completed invocation changes the record. <!-- SURFACE-002 SURFACE-003 -->

- [Should “Move note” run in Shortcuts or open the app?](references/a-saved-action.md)
- [A widget still shows a departed train](references/widget-timeline.md)
