---
name: swiftui-platform-adaptation
description: "Adapt SwiftUI navigation, focus and controls across Apple devices while keeping the selected item and unfinished task intact."
---

# Keep a task usable as the interface changes

Let the destination fit the device. A phone can push the selected note, an iPad or Mac can show it beside a sidebar, and a watch may offer only capture. Decide what someone must be able to finish in each place.

## Design choices

1. **Keep selection with the scene that owns it.** Bind compact and split presentations to the same record identity and editing session. Independent windows can share the saved records and still work on different items. <!-- ADAPT-001 -->
2. **Preserve the route when the layout changes.** Trace the selection through NavigationStack or NavigationSplitView and back to its collection. On watch, lead with the current metric and action. Move infrequent controls to another surface before shortening the primary label. <!-- ADAPT-002 -->
3. **Give each input a deliberate result.** Route keyboard commands and VoiceOver actions through the same operation as touch. When replacing a focused form, end editing in its owning view and return focus to a useful destination. In an editor with explicit Save, label Return according to what it actually does. <!-- ADAPT-003 -->

## Try it

Change the presentation while the task is in progress.

- Type into one of two note windows. Narrow it, open the same selection in compact detail, and go Back. The draft survives and the second window keeps its own note. <!-- ADAPT-001 ADAPT-002 -->
- Try Save at an accessibility text size with VoiceOver or a keyboard. On a companion watch, read and activate the current action at the smallest supported size. <!-- ADAPT-002 ADAPT-003 -->

- [An iPad editor becomes a compact detail](references/editing-across-layouts.md)
- [Pause on the watch and resume on the phone](references/watch-session.md)
