---
name: apple-swiftui-native-apps
description: "Design or repair a native SwiftUI feature, from the main action and state owner to toolbar controls, button contrast, and Liquid Glass."
---

# Build a feature that feels at home in SwiftUI

Start with one moment in the app. During a workout, the person needs the current interval, its next action, and a way out. For a place they saved yesterday, they need a recognizable list and a way to find it. Let that difference shape the screen.

## Design choices

1. **Give the current task priority.** Name the main action, safe exit, and what can wait. Use toolbar placements for app commands and content controls for choices about an item. A timer beside an exercise should measure that exercise. <!-- FEATURE-001 -->
2. **Trace the control before restyling it.** Follow the rendered label through its Button or Menu, role, style, tint and parent environment. For unreadable button text, remove competing foregrounds or custom backgrounds and try the system style in context. Use prominent styling for the action that deserves it. <!-- FEATURE-002 -->
3. **Give each transition one owner.** A draft belongs to its editor until Save. Pause and Resume are two states of one action. Have the timer, enabled actions and companion display read that same transition, including after relaunch. <!-- FEATURE-003 -->

## Try it

Pick a state that makes a wrong implementation visible.

- Pause during an interval, background the app, and return. The clock and automatic progression agree with the action shown. For a creation flow, cancel once and reopen a successfully saved item. <!-- FEATURE-001 FEATURE-003 -->
- Run the real toolbar or sheet in light and dark appearance at a large text size. Check the label, hit target, VoiceOver action and prominence in their surrounding chrome. <!-- FEATURE-002 -->

- [Choosing the first screen for Saved Places](references/saved-places.md)
- [An unreadable button, a glass toolbar, or a jumping Save action](references/native-controls.md)
