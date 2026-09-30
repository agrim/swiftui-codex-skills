# Accessibility and localization: playbook

## Audit by task

Start with a real task: find a record, edit a value, recover from a failed save, or dismiss a modal. Inspect what is announced, in which order, and which actions can be performed without the default input method. A screen with labels can still have unusable focus order, invisible errors, or unreachable controls.

| Surface | Required reasoning | Proof |
| --- | --- | --- |
| Icon action | Meaningful label and native action semantics | Screen-reader activation |
| Adjustable value | Current value, unit, allowed range, adjustment action | Increment/decrement and boundary feedback |
| Collection row | Useful summary without swallowing child controls | Read row and invoke each independent action |
| Chart/custom drawing | Equivalent data summary and accessible exploration | Understand trend and exact relevant values |
| Form error | Field association and recovery path | Discover and fix error without sight |
| Live status | Meaningful change without excessive announcements | Announcements do not flood or steal focus |

Labels name the element; values communicate state; hints explain nonobvious outcomes. Do not repeat information already conveyed by the native role. Decorative images can be hidden, but meaningful images need text alternatives. Combining children is useful for one logical item, not an excuse to erase a row's separate buttons.

## Typography and target size

Use text styles and scalable custom metrics where appropriate. Let content wrap, grow vertically, or switch layout rather than globally capping text size. Check the highest supported accessibility sizes on actual containers, not only a normal-size preview.

Consult the current platform-specific HIG control-size table. Do not turn one familiar phone dimension into a universal minimum for macOS, tvOS, watchOS, and visionOS. Evaluate usable hit area, spacing, focus interaction, and accidental activation together. Compact visual glyphs can have larger interaction regions without misleading surrounding controls.

## Appearance and motion

Use semantic colors where possible, then verify actual contrast in supported appearances. Brand colors and custom materials need their own checks. Distinguish values with shape, text, pattern, or symbols in addition to color. Test increased contrast and reduced transparency against the implemented background, including content behind glass.

Respect Reduce Motion while preserving feedback. Replace distracting spatial motion with a restrained alternative when appropriate; do not remove the only indication that an action completed. Pause decorative or continuous motion when not needed. For audio/video, account for captions, transcripts, and applicable descriptions rather than relying on sound alone.

## Focus and alternative input

Keyboard focus and accessibility focus are related but different systems. Use `@FocusState` for input focus and `@AccessibilityFocusState` for supported assistive focus when necessary. Do not repeatedly steal focus during updates. Return focus sensibly after dismissal or deletion and preserve a way out of custom focus regions.

Provide alternatives to swipes, drags, timing-sensitive actions, and complex gestures. Verify keyboard commands against platform conventions. Avoid presenting status that disappears before assistive technologies can reach it.

## Localization is behavioral

Use localizable strings or String Catalogs and locale-aware dates, numbers, measurements, and plurals. Do not assemble sentences from independently translated fragments. Test long strings, mixed scripts, mirrored layouts, and accessibility labels in the selected language. Use leading/trailing alignment, but review whether each symbol or image should actually mirror.

## Reporting limits

Record the device/OS, assistive technology, settings, journey, and outcome. An accessibility audit API can find some defects, not prove comprehension or every supported input path. Evaluate App Store accessibility claims against Apple's current criteria and the shipped candidate; do not infer them from the presence of modifiers.

## Sources

- [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) — HIG: Accessibility.
- [accessible-controls](https://developer.apple.com/documentation/swiftui/accessible-controls) — SwiftUI accessible controls.
- [accessibility-focus](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate) — SwiftUI AccessibilityFocusState.
- [rtl](https://developer.apple.com/design/human-interface-guidelines/right-to-left) — HIG: Right to left.
- [reduced-motion](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria) — Reduced Motion evaluation criteria.
- [ui-audit](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityauditissue) — XCUI accessibility audits.
- [localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization) — Preparing views for localization.
