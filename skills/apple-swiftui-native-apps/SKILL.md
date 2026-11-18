---
name: apple-swiftui-native-apps
description: "Build or simplify a SwiftUI feature around one everyday task, from the first action to the result someone comes back for."
---

# Build a complete native SwiftUI feature

What should someone be able to do when this feature is finished? With Saved Places, they hear about a café today and find it on Saturday. Build enough of the app to make that whole trip work.

## Design choices

1. **Let the main verb shape the screen.** Sketch what a person sees before and after acting. For “save a place,” a list with Add and an editor may be the whole feature. When the task is drawing a route, a map or canvas belongs at the center and the list can wait. <!-- FEATURE-001 -->
2. **Give familiar controls the real work.** For Saved Places, a SwiftUI List can show the collection and a toolbar Button can open the editor. Style the label if needed. Keeping the button gives touch, keyboard and assistive input the same action. <!-- FEATURE-002 -->
3. **Put each value where it needs to live.** The editor can own unfinished text. The collection owns saved places. Connect the two at Save using the app’s existing model. Introduce a shared owner when a second consumer actually needs the same value. <!-- FEATURE-003 -->

## Try it

Walk through your chosen task from first use to its payoff. For Saved Places, try these two paths.

- Start empty, add a place, save, relaunch, and open it. Then abandon a second entry. The first place is still there and the abandoned one never appears. <!-- FEATURE-001 FEATURE-003 -->
- Complete the same task with a supported alternate input, such as a hardware keyboard. Add, Save and the saved row must all be reachable. <!-- FEATURE-002 -->

- [Choosing the first screen for Saved Places](references/saved-places.md)
