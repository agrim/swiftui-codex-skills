# Assistive journeys and localized content

Audit a real task from entry to completion, including failure and recovery. Check element names, roles, values, actions, grouping, order, focus movement, announcements, and discoverability. An automated audit catches only part of this journey.

Use semantic labels even when visual presentation is icon-only. A symbol's visual meaning is not sufficient evidence that assistive output communicates the action. Do not combine a whole row into one accessibility element if that removes independently actionable controls. Conversely, avoid exposing decorative fragments as a tedious list of elements.

When content updates, move accessibility focus only for a meaningful user-facing change; avoid stealing focus on every refresh. Announce completion or error at a useful frequency, not each progress sample. Test alternative interactions rather than relying solely on a custom gesture.

## An action that works by touch but fails by voice

An editor shows a button titled “Save draft”. At larger text sizes the same action moves into a menu. Test the full journey with Voice Control on a supported destination, using the command language and locale under test.

1. Say the command for the visible title, such as “Tap Save draft” on iPhone. If it fails, use “Show names” to compare the exposed name with the visible title and “Show numbers” to check whether the button is individually reachable.
2. An ordinary labeled button may already respond to its visible title. If it needs spoken aliases, include that localized title in `accessibilityInputLabels(_:)` alongside the alternatives. For “Save draft”, put the localized visible title first, add any shorter alias, and try both. Keep changing values and status accessible to VoiceOver.
3. Repeat after reflow. Dictate a draft, edit a word, open the menu by voice, and invoke Save. Confirm that the intended record shows the edited text. If several records expose the same visible action title, exercise the app’s disambiguation path and check which record changed.

Record the spoken phrase, the name the system displayed, the destination, and the observed outcome. A number can help locate the failure even when the visible name still fails as a command.

## A custom dial announces a value but cannot adjust it

A dial exposes its current level as text. VoiceOver reads it, yet a listener cannot change the level. Prefer a native control with a custom appearance when it fits the interaction. If custom drawing owns the gesture, use `accessibilityRepresentation` where supported to supply a nonvisual Slider bound to the same level, bounds and step. The replacement supplies the dial's accessibility elements. Apply it to the dial alone so adjacent actions remain reachable.

With VoiceOver, adjust up and down, reach each limit, then move to the next control. Check the on-screen level and the announced value after each change. Both input methods should produce the same value at each stop. [SwiftUI accessibility representation](https://developer.apple.com/documentation/swiftui/view/accessibilityrepresentation%28representation%3A%29)

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
- [SwiftUI accessibility input labels](https://developer.apple.com/documentation/swiftui/view/accessibilityinputlabels%28_%3A%29).
- [Voice Control evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/voice-control-evaluation-criteria).
