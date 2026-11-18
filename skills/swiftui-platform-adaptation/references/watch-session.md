# Pause on the watch and resume on the phone

Choose which device owns the session and how the other handles a disconnected tap. Carry the session ID, phase, revision and timing needed to reconstruct elapsed time. A watch can draw a clock from this state without a message for every tick.

**Decide what can be replaced.** WatchConnectivity’s application context replaces the previous pending snapshot. That fits a display of the latest accepted state. If each completed lap belongs in history, record the lap as an event with its own ID and reconcile delivery. A later snapshot must not erase an unacknowledged lap. If the watch can pause offline, show which change is pending and have the session owner resolve competing actions.

**Keep the watch usable.** Put the current interval and its action on the main screen. Move history elsewhere. Remove a redundant symbol before shrinking “Resume.” Try the smallest supported size with large text.

Pause just before automatic advance. Reconnect after the boundary and compare phase and elapsed time on both devices. Start a new session, then deliver an old pause. The new session keeps running. If laps are recorded, resending one lap leaves one entry.
