# Adaptive layout and scrolling: playbook

## Read the proposal, then the response

SwiftUI layout is a negotiation between a container's proposed size and a child's chosen size. A frame can constrain or expand the proposal without making the child's content intrinsically readable. Debug the smallest subtree that first exceeds its intended space. Add borders temporarily if useful, then remove diagnostic decoration.

| Requirement | Start with | Escalate when |
| --- | --- | --- |
| Horizontal/vertical composition | Stacks, alignment guides, spacing | A layout genuinely depends on all children's sizes |
| Alternative compact arrangement | `ViewThatFits` or an explicit adaptive branch | Different semantic structures are required |
| Small aligned matrix | `Grid` where available | Content volume justifies lazy creation |
| Long collection with row semantics | `List` | Custom scrolling semantics are needed |
| Custom large scrolling arrangement | `ScrollView` plus lazy stack/grid | Measurement proves a more specialized path necessary |
| Content-dependent placement | `Layout` protocol | Existing containers cannot express the geometry |
| Container measurement | Scoped geometry reader or supported geometry API | The measurement cannot be expressed structurally |

`GeometryReader` is a tool, not a violation. Its proposed size and position in a stack matter. Do not use a full-screen reader to calculate local widths from stale global assumptions. Compare a semantic derived value, such as a width class or an item range, instead of publishing every fractional geometry change.

## Text and controls

Choose semantic fonts, leading/trailing alignment, and flexible vertical space. Use `fixedSize` deliberately: it can preserve an intrinsic dimension, but also force overflow. `layoutPriority` resolves competition; it does not repair impossible constraints. A single-line truncating secondary identifier can be reasonable; hiding the primary action or core user data is not.

Do not lock a control's entire height merely to avoid label movement. Preserve a comfortable target while allowing content to wrap or selecting a different composition. A layout can keep visual rhythm without freezing dimensions across all accessibility sizes.

## Scrolling and safe areas

Let backgrounds extend when the design calls for it; keep controls clear of system gestures, hardware intrusions, and the keyboard. Prefer safe-area-aware placement for persistent actions instead of arbitrary bottom padding. Avoid nested same-axis scrolling unless interaction ownership is intentional and tested.

Programmatic scrolling requires stable IDs and content that actually exists when the request executes. A count change is not a reason to scroll away from what the user is reading. Define policies for first load, appended content, restored position, and user-initiated jumps. Test keyboard presentation while an input row is near the bottom.

## Custom Layout correctness

Handle unspecified, zero, and finite proposals without returning invalid dimensions. Compute sizes and placements consistently, respect layout direction, and invalidate any cache when its inputs change. Do not store environment-dependent measurements forever. Test empty children, mixed intrinsic sizes, a very long label, and resizing through the breakpoint.

## Localization and adaptive windows

Use leading/trailing semantics, localizable format styles, and layout-direction-aware icons. Do not mirror every image: photographs, media controls, and directional symbols have different semantics. Inspect long German-like text, Arabic/Hebrew text, and mixed-direction identifiers. On desktop and tablet, resize the actual window; a device-class check alone is not a layout strategy.

## Sources

- [layout](https://developer.apple.com/documentation/swiftui/layout) — SwiftUI Layout protocol.
- [hig-layout](https://developer.apple.com/design/human-interface-guidelines/layout) — HIG: Layout.
- [rtl](https://developer.apple.com/design/human-interface-guidelines/right-to-left) — HIG: Right to left.
- [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) — HIG: Accessibility.
