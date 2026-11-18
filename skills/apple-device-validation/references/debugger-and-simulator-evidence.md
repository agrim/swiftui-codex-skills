# Diagnosing a failed interaction

Record the first missing observation. An install error belongs to the installer. A launch crash needs its crash evidence. If capture times out while the app is running, check the session’s bundle, destination and current screen before changing the view. Remove temporary probes and retry timing-sensitive behavior from a clean launch.

**A row exists but a tap has no effect.** Query by a stable accessibility identifier. For an offscreen row, scroll it into view. For a sheet covering it, follow the expected dismissal path. After the control is hittable, perform the action and assert its outcome, such as a saved value appearing in the detail view. A successful tap call alone leaves the outcome open.

When coordinates are the only option, keep the uncropped frame, orientation and size for that run. Re-query after rotation or navigation. Synthetic fixtures can show a denied-permission layout, while actual permission handling needs a run through that boundary.
