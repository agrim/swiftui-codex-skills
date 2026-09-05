# Visual language, materials, and motion: playbook

## Hierarchy before styling

Define the current task and its next useful action. Most screens benefit from a clear primary action, but an app-wide “exactly one prominent button” law ignores tool palettes, split views, and other legitimate contexts. Resolve competing actions by their meaning, frequency, and risk. Minimalism removes unnecessary decisions; it must not erase persistence, undo, state, or recovery semantics.

A welcome screen should explain the actual shipped outcome, not promise a future feature inventory. Defer setup that is not required for the immediate experience. Keep secondary information available without overwhelming a live task.

## Typography, color, and symbols

Use semantic typography and a small hierarchy of text roles. Custom fonts need Dynamic Type scaling, fallback, and long-string tests. Avoid tiny secondary text as a substitute for deciding what matters. Numeric alignment can use monospaced digits when the display benefits, without imposing a monospaced font on all copy.

Prefer semantic foreground and background roles; test brand colors and custom contrast pairs. Keep destructive meaning and disabled state truthful. Use color as a supplement to text or symbols, not the only carrier of meaning.

Select an SF Symbol for meaning and verify its availability at the deployment minimum. Review the symbol together with its container: an enclosed symbol inside another heavy enclosure can add needless weight. Multicolor and hierarchical rendering have different roles; do not assume tint affects every rendering mode identically. Remove redundant icons before sacrificing readable labels on compact screens.

## Materials and Liquid Glass

Apple's material guidance distinguishes the functional control/navigation layer from the content layer. Standard system controls acquire appropriate system presentation; custom glass effects should be restrained and should not create multiple competing floating layers. Start by removing opaque custom chrome that fights the intended native surface, but keep intentional readable content backgrounds.

Check the exact API's availability and platform support. Do not replace old behavior merely because a symbol exists in a newer SDK. Avoid pretending blur or an arbitrary translucent fill is equivalent to native Liquid Glass. Use a functional fallback on older systems rather than reproducing undocumented system internals.

Validate with real content behind the material, both appearances, accessibility contrast/transparency settings, scrolling edges, and disabled controls. Clear material is not a universal default for text-heavy surfaces.

## Animation and transactions

Animate a specific state change with an appropriate scoped transaction or value-based animation. An animation modifier can affect other changes in the same transaction; locate it at the smallest meaningful scope. Use transitions for insertion/removal, and interpolation for changing an existing view. Preserve identity when matching elements across states.

Use phase/keyframe or symbol animation APIs only when available and justified by the interaction. Test interruption, repeated activation, reversal, and rapid state changes. Do not rely on an animation duration as the business-operation completion signal. Reduced-motion alternatives must retain meaningful status feedback without unnecessary scaling, parallax, or spinning.

## Data-rich content

Charts need a question, labeled units, honest scales, meaningful empty/missing states, and accessible summaries. Zero, absent, estimated, and stale data are different. Prefer a platform chart or map when its semantics fit; custom drawing needs an equivalent accessible representation. Images need appropriate resolution, aspect handling, loading/error states, and resource limits. A beautiful placeholder is not a successful network load.

## Component contract

A reusable component states its role, inputs, supported states, style ownership, accessibility semantics, and layout behavior. Share this contract when semantics repeat; do not force every rounded shape through a mega-component with dozens of booleans. Audit the real rendered result instead of measuring quality by the number of native modifiers.

## Sources

- [design](https://developer.apple.com/design/human-interface-guidelines/design-principles) — HIG: Design principles.
- [materials](https://developer.apple.com/design/human-interface-guidelines/materials) — HIG: Materials.
- [glass](https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass) — Liquid Glass technology overview.
- [typography](https://developer.apple.com/design/human-interface-guidelines/typography) — HIG: Typography.
- [symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) — HIG: SF Symbols.
- [color](https://developer.apple.com/design/human-interface-guidelines/color) — HIG: Color.
- [animation](https://developer.apple.com/documentation/SwiftUI/Animation) — SwiftUI Animation.
- [reduced-motion](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria) — Reduced Motion evaluation criteria.
- [charts](https://developer.apple.com/documentation/charts) — Swift Charts.
