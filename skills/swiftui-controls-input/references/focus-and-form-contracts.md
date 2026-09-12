# Focus, forms, and editable control contracts

Make the control express its role: action, navigation, boolean, mutually exclusive selection, continuous value, or text editing. A native control supplies semantics, but a custom style still needs contrast, focus, disabled, pressed, and accessibility verification. A decorative tap gesture is legitimate; a gesture-only primary action needs an equivalent discoverable control path.

Use a typed focus value for forms with multiple fields. Declare submit intent and route it through validation and commit once. Keyboard dismissal, field validation, and saving are different operations. Do not clear focused input while simultaneously destroying its owner without testing system-input teardown.

Test composition input, paste, AutoFill, selection replacement, and formatting while editing. A numeric formatter that rewrites every keystroke can destroy intermediate valid input or cursor position. Keep raw draft text when the edit grammar differs from the committed value grammar. Do not attach personal-data content types merely to obtain a keyboard appearance.

## Commit table

| Event | Expected contract |
| --- | --- |
| Open editor | No unintended persistence or permission request |
| Change field | Update draft; show proportionate validation |
| Submit/Save | Validate and invoke one canonical command |
| Cancel/swipe dismiss | Discard only this edit session's changes |
| Save failure | Preserve editable work and show recovery |
| Duplicate trigger | Do not create duplicate effects |

Keep menu selections type-compatible with their binding and unique tags. Do not add custom checkmarks that conflict with native selection. Drag/drop and keyboard shortcuts must invoke the same domain command and revalidate external payloads; alternate input routes cannot bypass permissions or save boundaries.

For compact or watch surfaces, remove low-value copy before sacrificing hit targets. For desktop, preserve keyboard equivalents and focus visibility. Test the entire component, not just its resting screenshot.

## Official sources

- [SwiftUI Button](https://developer.apple.com/documentation/SwiftUI/Button).
- [SwiftUI FocusState](https://developer.apple.com/documentation/swiftui/focusstate).
- [SwiftUI accessible controls](https://developer.apple.com/documentation/swiftui/accessible-controls).
