---
name: apple-performance-cleanup
description: "Use Instruments to fix a measured delay or memory problem, and simplify Swift code without losing behavior on the affected path."
---

# Make a slow interaction feel responsive

For a delayed sheet, measure tap to first usable frame. For a cleanup, name the behavior to preserve, such as a missing sensor reading staying distinct from zero.

## Design choices

1. **Capture a repeatable baseline.** Match device, configuration and data. Use Hangs for a stall, Time Profiler for CPU work or the SwiftUI instrument for view updates. Separate cold and warm runs. <!-- SPEED-001 -->
2. **Follow work inside the delay.** Select the missed frame or blocked tap. If the main thread waits, follow the dependency. If many short row updates fill the frame, find the changing input they share. Change one suspected cause. <!-- SPEED-002 -->
3. **Preserve the visible behavior.** Keep ordering, cancellation and missing values intact. For memory growth, repeat a present/dismiss cycle and find the surviving owner in Xcode’s Memory Graph. <!-- SPEED-003 -->

## Try it

Choose a pass condition before comparing builds.

- Repeat the original gesture. If deferring work speeds up a sheet, also measure the first field tap that now triggers it. <!-- SPEED-001 SPEED-002 -->
- During a scroll, edit a visible row and advance a download. The row and toolbar still update, and hitch durations meet the chosen target across repeats. For a cleanup, compare the same edge cases before and after. <!-- SPEED-003 -->

- [Which update delayed this scroll?](references/a-scrolling-hitch.md)
