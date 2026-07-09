# Privacy And System Integration Patterns

Use this reference for Apple frameworks that cross app boundaries, ask for permissions, expose data outside the app, or depend on account/device state.

## Failure Patterns

- A framework import is easy; a complete permission and privacy story is harder.
- App-only truth often does not fit a system framework. Preserve app truth locally and export only truthful projections.
- Widgets, intents, live activities, search indexes, companion devices, and cloud stores can leak data if treated as harmless UI surfaces.
- Permission denial and account unavailability are common app states and need explicit UX.
- Retrying export/sync without durable state creates invisible data loss or repeated prompts.

## Default Checks

- What data leaves the app boundary?
- What user-facing purpose explains the access?
- What target owns the entitlement and purpose string?
- What happens if permission is denied, revoked, or unavailable?
- What is stored locally, synced, exported, indexed, or projected?
- What tests prove the mapping is truthful and failure-safe?
