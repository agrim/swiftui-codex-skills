# Locating the first layout failure

| Symptom | Isolate it | Decision |
| --- | --- | --- |
| A translated action clips in a narrow window | Remove one fixed frame at a time, starting at the first clipped child. Change width while keeping the font size fixed, then reverse the experiment. | Wrap a secondary label or reflow the controls at the constraint that actually binds. Keep a fixed width only if the task requires it at both extremes. |
| Text fits until the layout switches direction | Put an identifier in a right-to-left sentence. Inspect its order separately from the ordering of adjacent controls. | Correct the offending field or placement. A global mirror can reverse imagery with its own direction. |
| A scroll hitches while its toolbar stays in one state | Count geometry-driven state writes until the toolbar crosses its visibility threshold. Compare scrolling with that observation removed. | Publish the threshold crossing when that is all the toolbar consumes. Measure row construction separately if the hitch persists. |

## When a custom layout earns its cost

Name the placement that a stack, grid or fitting alternative failed to produce. For a layout that equalizes column widths, measure, resize, then change only the longest localized label. A stale cached width can pass the resize check and still clip after translation. Check an empty collection and an unspecified proposal for finite dimensions before relying on the cache.
