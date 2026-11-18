# Save disappears over the photo

Reproduce the editor with the photo, toolbar and sheet in place. A Button previewed alone can look fine. Trace the label outward through the button style, placement, tint and ancestor foreground. If the photo’s caption color reaches the toolbar, scope it to the caption. Let the system choose the button foreground for its role and appearance.

```swift
ToolbarItem(placement: .confirmationAction) {
    Button("Save", action: saveDraft)
        .disabled(isSaving || !draft.isValid)
}
```

Use a stable label for a brief save. If the wait becomes noticeable, show progress without moving the action. Try enabled, disabled and saving states over both light and dark photos. If the button is difficult to hit, inspect the native label size, control size and actual hit region before drawing a larger capsule.

**When glass is involved.** Start in the system toolbar and scroll content beneath it. Remove a second material or opaque background that hides the native effect. If a custom treatment still serves the task, try it with Reduce Transparency, Reduce Motion and the oldest supported runtime. A first-party screenshot alone cannot establish which public API supplies the effect.

**When color implies the wrong choice.** Give peer start options equal emphasis. For mutually exclusive values, bind one Picker inside the Menu to the selected value. Reopen the menu after changing it. Exactly one value should be selected.
