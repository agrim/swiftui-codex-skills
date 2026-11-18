---
name: swiftui-accessibility
description: "Audit SwiftUI tasks with VoiceOver, Voice Control, keyboards, Dynamic Type, Reduce Motion, contrast, and localized layouts."
---

# Find what blocks a SwiftUI task with assistive input

Use this when a task works by touch but someone using voice, a keyboard or an accessibility setting cannot finish it.

## Start here

Try the affected task, such as editing a reminder, in the reported language, text size and input method. Stop at the first blocked action.

## How to proceed

1. **Inspect the element receiving focus.** Compare the announced name, role, value and unit with what activation does. A dial that announces a level should let its user adjust it. <!-- AX-001 -->
2. **Follow the action when the layout changes.** If Save moves into a menu at large text sizes, follow its localized title to the record it actually changes. <!-- AX-002 -->
3. **Try the task without its strongest cue.** Remove the color cue or skip the swipe gesture. Can the person still tell whether Save succeeded and reach the next action? <!-- AX-003 -->
4. **Preserve independent row actions.** Group related text only when Edit and Delete remain reachable in order. <!-- AX-004 -->
5. **Follow a failed submission through recovery.** Using the affected input, find the error, correct the invalid field and finish the task. <!-- AX-005 -->

## Check the result

- With VoiceOver or Full Keyboard Access, reach each row action in order and recover from invalid input. <!-- AX-004 AX-005 -->
- Use long, mixed-direction text at maximum supported size. Speak the visible Save label with Voice Control. Only the intended reminder changes. <!-- AX-001 AX-002 -->
- Force success and failure under the affected Reduce Motion, Reduce Transparency or contrast setting. Each outcome remains distinguishable. <!-- AX-002 AX-003 -->

## What to report

Rank barriers by the tasks they block and name the input, setting, fix and outstanding hands-on checks.

- [Find the first inaccessible step](references/accessibility-patterns.md)
- [Test spoken Save, a custom dial or a translated action](references/assistive-and-localized-flows.md)
