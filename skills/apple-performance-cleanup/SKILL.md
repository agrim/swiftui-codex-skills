---
name: apple-performance-cleanup
description: "Find the work that delays a particular scroll, edit or launch and verify that the change improves that interaction while preserving its behavior."
---

# Make a slow interaction feel responsive

Start with something a person can feel, such as a list that catches while downloads are running. Choose the moment that should be faster and the behavior that must still work after the change.

## Design choices

1. **Measure the wait the person encounters.** Repeat the same gesture with representative data on the affected destination. Use frame deadlines for a hitch or elapsed time to a usable result for a delay. Keep a baseline you can repeat. <!-- SPEED-001 -->
2. **Locate the delay inside that interval.** Look for work, waiting or repeated updates on the path to the result. A busy background thread matters if the interaction depends on it. Change the smallest dependency that explains what happened. <!-- SPEED-002 -->
3. **Keep the visible contract.** If progress updates cause an entire list to redraw, let the progress display observe them directly. The list still needs to reflect changes to each item. Choose an improvement target and repeat the original interaction. <!-- SPEED-003 -->

## Try it

Judge the result using both the original delay and the behavior touched by the fix.

- Compare repeated runs with the same device, build configuration, data and gesture. If the scrolling hitch persists after average CPU falls, keep investigating the hitch interval. <!-- SPEED-001 SPEED-002 -->
- While scrolling, change a visible item and advance a download. The row and progress indicator both update, and the measured gesture meets the chosen target. <!-- SPEED-003 -->

- [Which update delayed this scroll?](references/a-scrolling-hitch.md)
