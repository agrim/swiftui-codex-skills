# Assistive journeys and localized content

Audit a real task from entry to completion, including failure and recovery. Check element names, roles, values, actions, grouping, order, focus movement, announcements, and discoverability. An automated audit catches only part of this journey.

Use semantic labels even when visual presentation is icon-only. A symbol's visual meaning is not sufficient evidence that assistive output communicates the action. Do not combine a whole row into one accessibility element if that removes independently actionable controls. Conversely, avoid exposing decorative fragments as a tedious list of elements.

When content updates, move accessibility focus only for a meaningful user-facing change; avoid stealing focus on every refresh. Announce completion or error at a useful frequency, not each progress sample. Test alternative interactions rather than relying solely on a custom gesture.

## Text and locale matrix

Exercise large accessibility text, long translations, plural forms, interpolated content, dates/numbers, RTL, reduced motion, increased contrast, and reduced transparency. Keep storage/wire formatting separate from localized display. Layout direction should follow the environment unless the content has a genuine directional meaning.

Use string catalogs and supported localization APIs rather than assembling translated sentences from fragments. Give translators enough context for ambiguous labels. Preserve meaningful units and avoid using color, position, sound, or motion as the sole signal.

For charts, provide a meaningful accessible description or navigable data representation, including units, missing values, and the relevant trend. A visual annotation alone is insufficient. For forms, keep errors associated with fields and offer a recoverable path.

Record the destination, settings, tested journey, and what the audit tool did or did not cover. Do not certify VoiceOver, keyboard, or Switch Control behavior from source inspection or a screenshot. Re-run affected journeys after changing grouping, navigation, or custom controls.

## Official sources

- [HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- [SwiftUI accessible controls](https://developer.apple.com/documentation/swiftui/accessible-controls).
- [SwiftUI AccessibilityFocusState](https://developer.apple.com/documentation/swiftui/accessibilityfocusstate).
- [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization).
- [HIG: Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left).
