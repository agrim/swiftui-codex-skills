---
name: swiftui-platform-adaptation
description: "Adapt a SwiftUI task across window sizes, input methods and Apple devices while preserving selection, edits and navigation."
---

# Keep a task usable as the interface changes

When an iPad sidebar collapses, keep the same note, unfinished sentence and route back to the list.

## Design choices

1. **Own selection per window.** Share saved records. Keep the selected ID and draft with the scene that survives resizing. Sorting can change a row’s position. <!-- ADAPT-001 -->
2. **Decide what each destination can finish.** Use the same selection in a NavigationStack or NavigationSplitView. On watch, lead with the current action. Carry the item and progress into any handoff. <!-- ADAPT-002 -->
3. **Keep input attached to the task.** Send toolbar, keyboard and VoiceOver activation to the same Save operation. After dismissal, focus the edited item or another useful target. Let Return do what its label promises. <!-- ADAPT-003 -->

## Try it

Make the transition halfway through an edit.

- Open Monday and Tuesday in separate windows. Edit Monday, reorder the list and narrow its window. Monday keeps the draft, Back reaches the list and Tuesday stays selected in its window. <!-- ADAPT-001 ADAPT-002 -->
- At large text size, save by keyboard or VoiceOver and find the updated note. On watch, activate the primary action at the smallest supported size. <!-- ADAPT-002 ADAPT-003 -->

- [An iPad editor becomes a compact detail](references/editing-across-layouts.md)
- [Pause on the watch and resume on the phone](references/watch-session.md)
