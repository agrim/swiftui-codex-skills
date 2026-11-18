# A toolbar button disappears over a photo

Reproduce the actual screen. A Button in a preview can look fine while the same label inherits a foreground override from the photo container. Follow the toolbar placement, Button role, style, tint and ancestor modifiers. Remove the smallest competing override and render again over both light and dark photos. For system-styled buttons, let the style resolve the foreground. If two colored start options are peers, give them equal hierarchy. A plain Button with a product-specific capsule can fit that case. Test its inherited label against the actual fill in both appearances before choosing the colors.

For an editor whose primary action commits a draft, keep the photo’s foreground styling on its caption and give Save a semantic toolbar placement:

```swift
ToolbarItem(placement: .confirmationAction) {
    Button("Save", action: saveDraft)
        .disabled(isSaving || !draft.isValid)
}
```

The same button stays in the hierarchy while the save finishes. Try it disabled, enabled and in flight over a bright photo.

**Chrome and Liquid Glass.** Put navigation and actions in the platform toolbar first. A custom capsule, an opaque toolbar background or a second material can obscure what the system already draws. Remove it and scroll real content underneath. Use a custom glass treatment only for a control the standard container does not supply. Check the deployment target and exercise the older appearance as well as Reduce Transparency and Reduce Motion. A first-party screenshot alone cannot tell you which public API produced it.

**Geometry and meaning.** Keep a brief Save in the same Button with a stable label and disable repeat submission. Show progress for a perceptible wait. If an action feels too small, inspect the label’s intrinsic font or symbol size as well as control size. Give a single-choice Menu a Picker bound to the selected value. Hand-drawn checkmarks can all become selected.

**A quiet list.** If an empty library draws a line through its placeholder, inspect row and section separators in the empty, one-item and two-item states. Keep separators between siblings where they clarify the collection. Preserve meaningful grouping in settings forms. Compare the smallest supported layout and the longest localized label before adjusting padding across the app.
