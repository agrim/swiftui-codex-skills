# Mismatches between a control and its effect

| Symptom | Compare | Decision |
| --- | --- | --- |
| Choosing a filter unexpectedly pushes a detail | Change the filter, inspect history, then press Back. | Represent an exclusive choice in one selection. Open a destination only when visiting it is the intended action. |
| An icon works by touch but a shortcut bypasses its disabled state | Invoke both paths while the operation is busy. Inspect the effect count and the exposed name. | Route both paths through the same guarded command. Keep the localized action name when collapsing the visible label. |
| A button disappears on one backdrop | Remove the nearest custom foreground or style. Recheck pressed, disabled and focused states on the original material. | Correct the style that changes legibility. Escalate to owning activation behavior only if the control genuinely needs different activation semantics. |

## Gesture and drop conflicts

If a row swipe steals scrolling, try a diagonal drag near its primary action and find which handler consumed it. Keep gesture-only direct manipulation where the gesture determines the result, and provide another path to discrete commands such as Delete.

Drop the same item twice, then cancel a drop over an invalid destination. Reject unsupported types, sizes and destinations before committing. Compare the accepted result with the keyboard command so the alternate path cannot bypass validation or authorization.
