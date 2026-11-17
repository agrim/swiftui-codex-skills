# Decide whether a scrolling change is ready

A customer sees a pause when scrolling Saved Places. A teammate moved thumbnail decoding to a worker and suggests closing the issue because the whole-recording CPU profile looks better. Review the evidence below. Write a short response for that teammate with your release decision, the next investigation or change, and what evidence would change your decision.

These are synthetic trace extracts. Times are milliseconds from recording start. Both builds used the same device, release configuration, data, cache state and scroll gesture. Each repeat captured one gesture.

| Build | Whole-recording CPU leader | Median main-thread CPU across recording | Hitch durations across three repeats |
| --- | --- | --- | --- |
| Before | Thumbnail decode | 23% | 41, 39, 42 ms |
| Candidate | Search index refresh | 17% | 40, 42, 39 ms |

Candidate recording, repeat 1:

| Interval | Track | Observation |
| --- | --- | --- |
| 40–410 | Main thread | Search index refresh at launch |
| 1640–1800 | Worker | Decoding prefetched thumbnails |
| 2200–2380 | Interaction | Scroll Saved Places |
| 2240–2280 | Hitches | Missed presentation deadlines |
| 2242–2276 | SwiftUI | 312 PlaceRow body updates, all below 1 ms |
| 2243–2274 | Time Profiler, main thread | Samples distributed across PlaceRow updates |
| 2242–2276 | Update causes, representative sample | Download progress → library model change → PlaceRow |

The same 24 record IDs were visible throughout the interval. Each row shows a title and a saved flag. A toolbar item displays aggregate download progress. There are no per-row thumbnail timings or post-change interaction tests in the handoff.
