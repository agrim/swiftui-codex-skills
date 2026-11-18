# Pause on the watch, resume on the phone

Decide which device owns the live session and what a disconnected companion is allowed to do. Keep the session ID, phase and effective transition time together. Compute elapsed time from the session state so the phone, watch and Live Activity can agree without sending every clock tick. If the watch records an action offline, distinguish the accepted local change from delivery to the phone. On reconnect, reconcile newer transitions before applying a queued one.

Reserve the main watch screen for the current interval and one unambiguous action. Move history or session settings to a secondary view. Drop a redundant symbol before shrinking the word “Resume.” Keep the workout clock distinct from the interval timer. Try both supported size extremes with large text.

Start an interval, pause on one device and wait past the original interval boundary. The timer and automatic advance should both stay paused. Resume from the other device, reconnect, and reopen the app. A delayed pause from the previous session must not stop the new one.
