---
name: apple-swiftui-native-apps
description: "Build or refine SwiftUI screens using native controls, clear action hierarchy, system styling and one owner for each interaction."
---

# Build a feature that feels at home in SwiftUI

During a workout, the current interval and Pause belong together. Session settings can wait. Build the feature around one task someone can finish and recognize afterward.

## Design choices

1. **Choose what belongs on screen.** Give the next action priority and keep an exit reachable. Put screen commands in the toolbar and item choices beside the item. <!-- FEATURE-001 -->
2. **Start with the native control.** Use a Button for an action or a Picker for a choice. For a disappearing toolbar label, trace role, style, tint and inherited foreground. Remove the conflict and render again before choosing a custom fill or foreground. <!-- FEATURE-002 -->
3. **Change state once.** Let Pause and Resume act on the same session. Derive the label, clock and automatic advance from its phase. For a Save form, keep typing in a draft until the person commits. <!-- FEATURE-003 -->

## Try it

Exercise the actual control in its container.

- Pause just before an interval boundary and return afterward. The same interval is paused and Resume is available. In a creation flow, only a committed item survives relaunch. <!-- FEATURE-001 FEATURE-003 -->
- At large text size in both appearances, the primary label stays legible. VoiceOver names the action and activates it once. <!-- FEATURE-002 -->

- [Choosing the first screen for Saved Places](references/saved-places.md)
- [An unreadable button, a glass toolbar, or a jumping Save action](references/native-controls.md)
