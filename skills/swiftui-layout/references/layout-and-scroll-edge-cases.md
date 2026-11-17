# Layout proposals, lists, and scroll state

Before adding geometry work, identify the parent's size proposal, intrinsic content, alignment, layout priority, safe area, and scrolling role. A fixed width can conceal a broken proposal while failing Dynamic Type or window resizing. `GeometryReader` is appropriate when measured geometry is genuinely needed, not a default root for every screen.

Prefer container-aware layouts and semantic padding when they express the design. Use custom `Layout` for an actual measurement/placement algorithm; keep cache keys valid when subviews, environment, or proposed sizes change. Avoid feeding measurement into state in a loop that changes the measured layout again.

## Reflow while editing

A reminder editor puts a title field, a date, and a Save button on one line. Enlarging the text clips Save. Switching to a vertical copy of the editor reveals the button but can discard an in-progress edit. Identify what changes at the breakpoint before choosing a layout.

| What varies | Decision | Check |
| --- | --- | --- |
| Available width determines which presentation fits | Where available, put the preferred presentation first in `ViewThatFits(in: .horizontal)`. It compares each candidate’s ideal width with the proposal. Give the compact alternative room to wrap. | Use the longest supported label in the narrowest window. Check the final alternative for clipping and reachability. |
| The same editable children change arrangement at a known threshold | Where available, choose an `HStackLayout` or `VStackLayout` through `AnyLayout` and declare the field, date, and button once inside it. Changing the layout type this way preserves the children’s state. | Type an unsaved title, switch arrangements twice, then save. Check the draft, actual focus, and saved value. |
| The compact presentation genuinely needs different controls | Keep the draft in one owner above the alternatives and bind both presentations to it. This also works on earlier deployment targets. | Start editing in each presentation and finish in the other. Check that a single save commits the current value. |

Vary text size and container width separately. A long translation can overflow a narrow window even at the default text size. Verify the reading order after reflow with the relevant assistive technology.

## Collections

Keep identity stable and per-element output predictable. Filter/sort outside the row builder when needed so the container can understand the collection. Do not convert large dynamic lists into an eager stack without measuring memory, accessibility, and interaction tradeoffs. A lazy container is not automatically faster for a small bounded layout.

Use stable data IDs for scroll targets. Test insertion above the viewport, pagination, filtering, deletion of the current anchor, keyboard appearance, and restored position. Distinguish user scrolling from programmatic repositioning; do not repeatedly fight the user's position whenever data changes.

## Risk matrix

Validate smallest practical window, large text, long localized labels, RTL, empty/error/loading content, and visible keyboard. Test text wrapping instead of shrinking every label to fit a fixed frame. Ensure overlays and pinned controls do not obscure scrollable content or focus.

Throttle or reduce geometry observations to the value actually needed. State publication at every scroll pixel can invalidate a broad tree. Measure before replacing a native list or table with custom drawing. Preserve selection, row actions, keyboard navigation, and assistive semantics when changing containers.

## Official sources

- [SwiftUI Layout protocol](https://developer.apple.com/documentation/swiftui/layout).
- [ViewThatFits](https://developer.apple.com/documentation/swiftui/viewthatfits).
- [AnyLayout](https://developer.apple.com/documentation/swiftui/anylayout).
- [HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout).
- [HIG: Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left).
