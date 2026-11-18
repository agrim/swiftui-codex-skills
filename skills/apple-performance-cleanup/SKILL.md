---
name: apple-performance-cleanup
description: "Use Instruments to diagnose launch delays, UI hangs, scrolling hitches and retained memory, then verify the original interaction."
---

# Make a slow interaction feel responsive

Start with the moment someone waits. A sheet that hangs on its first presentation and a list that misses frames while scrolling call for different evidence.

## Design choices

1. **Record the affected interaction.** Profile a representative build and destination with Instruments. Use Hangs for a blocked tap, Time Profiler for CPU work, or the SwiftUI instrument for repeated view updates where available. Separate cold and warm runs. <!-- SPEED-001 -->
2. **Change the work that delays the result.** Select the troubled interval and follow the main thread. A broad fetch, formatter in a row body, or wait on a worker suggests different fixes. Keep a short navigation tap free of unrelated migrations, disk I/O and telemetry. <!-- SPEED-002 -->
3. **Preserve what the person sees.** Narrow observation to the views that use each value. Keep missing, zero, stale and failed readings distinct. For suspected retention, repeat a present/dismiss cycle and follow surviving owners in Xcode’s Memory Graph or Instruments Allocations. <!-- SPEED-003 -->

## Try it

Repeat the original interaction on the same destination and configuration.

- Compare the same cold and warm gesture before and after. For a slow editor, measure first presentation and then tapping the field. Deferred keyboard or database work can move the delay to the next tap. <!-- SPEED-001 SPEED-002 -->
- During a scroll, change a row and advance a download. Both still update within the chosen frame target. For retained memory, repeat the same cycles and check whether the suspected objects are released. <!-- SPEED-003 -->

- [Which update delayed this scroll?](references/a-scrolling-hitch.md)
