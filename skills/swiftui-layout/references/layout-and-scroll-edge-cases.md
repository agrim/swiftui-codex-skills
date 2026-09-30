# Layout proposals, lists, and scroll state

Before adding geometry work, identify the parent's size proposal, intrinsic content, alignment, layout priority, safe area, and scrolling role. A fixed width can conceal a broken proposal while failing Dynamic Type or window resizing. `GeometryReader` is appropriate when measured geometry is genuinely needed, not a default root for every screen.

Prefer container-aware layouts and semantic padding when they express the design. Use custom `Layout` for an actual measurement/placement algorithm; keep cache keys valid when subviews, environment, or proposed sizes change. Avoid feeding measurement into state in a loop that changes the measured layout again.

## Collections

Keep identity stable and per-element output predictable. Filter/sort outside the row builder when needed so the container can understand the collection. Do not convert large dynamic lists into an eager stack without measuring memory, accessibility, and interaction tradeoffs. A lazy container is not automatically faster for a small bounded layout.

Use stable data IDs for scroll targets. Test insertion above the viewport, pagination, filtering, deletion of the current anchor, keyboard appearance, and restored position. Distinguish user scrolling from programmatic repositioning; do not repeatedly fight the user's position whenever data changes.

## Risk matrix

Validate smallest practical window, large text, long localized labels, RTL, empty/error/loading content, and visible keyboard. Test text wrapping instead of shrinking every label to fit a fixed frame. Ensure overlays and pinned controls do not obscure scrollable content or focus.

Throttle or reduce geometry observations to the value actually needed. State publication at every scroll pixel can invalidate a broad tree. Measure before replacing a native list or table with custom drawing. Preserve selection, row actions, keyboard navigation, and assistive semantics when changing containers.

## Official sources

- [SwiftUI Layout protocol](https://developer.apple.com/documentation/swiftui/layout).
- [HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout).
- [HIG: Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left).
