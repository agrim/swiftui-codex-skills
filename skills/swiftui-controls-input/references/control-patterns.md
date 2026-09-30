# Controls, forms, and input: playbook

## Choose the interaction contract

| User intent | Control | Common mistake |
| --- | --- | --- |
| Perform an action | `Button` | Tap gesture on a stack |
| Open hierarchical content | `NavigationLink` | Button with an opaque navigation side effect |
| Choose one value | `Picker` | Independent checkmark toggles |
| Enable a preference | `Toggle` | Ambiguous action label |
| Adjust a continuous value | `Slider` | Tiny drag-only handle without accessible adjustment |
| Reveal secondary actions | `Menu` or contextual menu | Primary action hidden in an undiscoverable gesture |
| Commit a task | Explicit Save/Create action | Persistence on every draft keystroke |

Use a `Label` or equivalent semantic text plus symbol. `.labelStyle(.iconOnly)` can retain the text's accessibility meaning; an image-only label needs its own meaningful description. Avoid redundant “button” suffixes in labels when the control already announces its role.

## System style versus custom style

First inspect role, style, tint, inherited foreground, material, and enabled state. Remove conflicting label coloring before changing a system control. Do not assume `.tint` is a universal foreground color across all styles and platforms.

A genuinely custom component can own its foreground/background pair, with tested contrast and all interaction states. Use `ButtonStyle` to preserve standard activation; use `PrimitiveButtonStyle` only when intentionally owning activation semantics. An arbitrary custom fill plus a plain button does not guarantee the system will select a contrasting foreground. Avoid broad ancestor styling that accidentally changes menu, toolbar, or disabled labels.

## Forms and editing

Keep draft values separate from durable models when Cancel promises to discard changes. Show validation after relevant interaction or attempted submission, not as a wall of first-frame errors. Save failure leaves the draft recoverable. Treat an in-progress save as a command with a duplication policy, not simply a spinner.

For pickers, ensure tag values match the selection's type, including optional selections where relevant. Handle a selected value that disappears from the available choices. Use a native picker in a menu for exclusive choices instead of synthesizing state from independent row actions.

## Input and focus

Use an optional field enum with `@FocusState` for multi-field forms. Choose `submitLabel` and `onSubmit` consistently, respecting multiline input where Return inserts a newline. Autofocus can help a dedicated entry task; it is not universally right or wrong. Avoid surprising keyboard presentation on an informational modal.

Set content type, capitalization, autocorrection, keyboard type, and secure entry from the field's real semantics. Do not request personal AutoFill candidates for unrelated fields. Preserve composed text and non-Latin input; formatting and validation must not disrupt an input method's in-progress composition.

Before replacing a focused hierarchy, release focus and coordinate with actual lifecycle completion when necessary. `Task.yield()` is not a guaranteed render or keyboard-teardown barrier. Avoid arbitrary delayed dispatch as a universal fix.

## Gestures, drag, and drop

Gestures are appropriate for direct manipulation, drawing, or supplementary shortcuts. Provide an equivalent control or accessibility action for essential operations. Resolve gesture competition with scrolling and system navigation; do not capture the entire screen unnecessarily. Validate dropped types and sizes, handle cancellation, and commit the domain operation only after accepting a valid drop. Test pointer and keyboard paths independently of touch.

## Sources

- [button](https://developer.apple.com/documentation/SwiftUI/Button) — SwiftUI Button.
- [focus](https://developer.apple.com/documentation/swiftui/focusstate) — SwiftUI FocusState.
- [accessible-controls](https://developer.apple.com/documentation/swiftui/accessible-controls) — SwiftUI accessible controls.
- [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) — HIG: Accessibility.
