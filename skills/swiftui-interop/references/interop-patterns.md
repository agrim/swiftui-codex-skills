# Hosting, sizing, and focus

Choose a bridge for a capability the supported SwiftUI targets cannot provide. Compare behavior on the oldest supported release.

## A reused AppKit cell keeps the previous row’s state

Expand row A’s disclosure toggle. Reuse its cell for B, then update B in place. The cell should retain one hosting view. Decide who owns the toggle. For state local to a record, update the hosting view’s root and key that row by record ID. If expansion must survive scrolling, keep it outside the cell, keyed by record. Verify B starts with its own value and the next update preserves it.

## A bridge works only at its preview size

Mount the bridge in a narrow window with large text, resize it, and move focus through it using the keyboard and assistive navigation. Check clipping, selection, and responder routing in the actual host. In a multiwindow app, opening the same bridge in a second window should leave focus in the intended window.
