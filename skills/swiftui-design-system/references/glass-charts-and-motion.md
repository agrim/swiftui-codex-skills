# Glass, charts, and motion as semantic components

## Materials

Choose a material by functional role. Let native navigation, toolbars, and controls adapt before adding custom glass. New glass effects, containers, morphing identities, and interactive variants must be checked against compiler and OS availability. A fallback should preserve hierarchy and action meaning rather than imitate an unavailable effect with arbitrary blur.

Do not stack multiple decorative glass layers over reading content. Check legibility against changing underlying imagery, increased contrast, reduced transparency, and both appearances. A system style is not evidence that every custom fill and foreground combination remains readable.

## Motion

Tie animation to the state transition it communicates. Keep insertion/removal identity stable and scope animation so unrelated updates do not move unexpectedly. Repeated gestures, interrupted transitions, keyboard changes, and navigation replacement can expose invalid intermediate states.

Use matched geometry or phased/keyframe animation when continuity requires it, not as a reason to duplicate state owners. Provide a reduced-motion equivalent that conveys the same relationship without unnecessary movement. A spring constant copied from another app is not a design requirement.

## Charts

Start with the user question and data semantics. Define units, aggregation, missing data, time zone, sort order, and stable series identity before choosing marks. Bar length should not imply a zero baseline when a truncated scale changes the meaning. Distinguish a true zero from missing data.

Selection and annotations must correspond to the displayed transformed data. Test empty, single-point, dense, negative, outlier, and multi-series cases. Keep axes and legends readable at larger text sizes and provide accessible data navigation or a useful text/table alternative. A three-dimensional chart needs a specific analytical benefit and a usable nonspatial alternative.

Shared components should encode semantic roles, not force the same decoration on every platform. Keep brand choices explicit while preserving system behavior, and inspect the rendered result rather than equating more materials or symbols with quality.

## Official sources

- [Liquid Glass technology overview](https://developer.apple.com/documentation/TechnologyOverviews/liquid-glass).
- [HIG: Materials](https://developer.apple.com/design/human-interface-guidelines/materials).
- [SwiftUI Animation](https://developer.apple.com/documentation/SwiftUI/Animation).
- [Reduced Motion evaluation criteria](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/reduced-motion-evaluation-criteria).
- [Swift Charts](https://developer.apple.com/documentation/charts).
