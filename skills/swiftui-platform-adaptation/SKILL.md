---
name: swiftui-platform-adaptation
description: "Adapt a SwiftUI task across phone, tablet or Mac while preserving the item, unfinished work and access to its actions."
---

# Keep a task usable as the interface changes

A phone may push a note onto a navigation stack while an iPad shows it beside the list. Both presentations should let someone finish the same edit. Start with the task that breaks when the window, text size or input method changes.

## Design choices

1. **Decide what belongs to this window.** Keep its selected item and unfinished edit alive across changes in layout. Use the record’s identity so a reordered list still opens the intended item. Give separate windows independent selections when people can work in both. <!-- ADAPT-001 -->
2. **Let the destination take its native shape.** A sidebar and detail can become a list and pushed detail in a narrow window. Preserve where Back should lead. If the selected item disappears, show a valid destination and explain what happened to any unsaved work. <!-- ADAPT-002 -->
3. **Keep the action within reach.** Let secondary controls move into a menu or onto another line as space shrinks. Give the primary action one meaning across touch, keyboard and assistive input. After dismissal, return focus to an item the person can act on. <!-- ADAPT-003 -->

## Try it

Exercise a transition while someone is halfway through the task.

- Edit a note, reorder the list, then narrow the window. The same draft is editable and Back returns to the list. A second window retains its own selection if the app supports it. <!-- ADAPT-001 ADAPT-002 -->
- At the largest supported text size, reach Save with VoiceOver or the keyboard. Invoke it once and find the saved note again. <!-- ADAPT-003 -->

- [An iPad note editor becomes a phone-sized detail](references/editing-across-layouts.md)
