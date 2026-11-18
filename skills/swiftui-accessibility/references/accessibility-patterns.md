# Auditing the blocked step

Start at the first operation the user cannot complete. Record which element actually receives focus, what is announced, what activation does, and how the user could recover. A passing automated audit can help narrow the search. Hands-on results are needed for claims about completing the task.

| Failure | Probe | Repair boundary |
| --- | --- | --- |
| A parent row announces both titles but neither secondary action | Try editing and deleting different rows while reading in task order. | Keep a shared summary only if independent controls still expose their own actions. |
| A save error appears but focus returns to the toolbar | With VoiceOver or Full Keyboard Access, find the invalid field, correct it and dismiss. Repeat after the next background refresh. | Fix field association or focus routing at the first lost step. Check keyboard and assistive focus separately. |
| Removing motion hides the only sign of completion | Submit once with Reduce Motion, then retry after a forced error. Compare the two outcomes without animation. | Preserve distinct status long enough to find it. If live updates interrupt the announcement, coalesce progress separately from completion. |
| Tapping one compact control invokes its neighbor | Probe the boundary between their actual hit regions at large text sizes. | Increase clearance or reflow the pair. Shrinking their glyphs alone can leave overlapping targets. |

For a task that depends on hearing audio, play it muted and check whether captions or equivalent information still distinguish the events the user needs.
