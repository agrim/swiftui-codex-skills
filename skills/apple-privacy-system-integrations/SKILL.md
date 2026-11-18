---
name: apple-privacy-system-integrations
description: "Request Apple service access at the right moment, handle missing readings, and verify what gets exported, indexed or removed."
---

# Add an Apple integration people can trust

A training diary can save a workout with Health sharing off. Live heart rate needs a reading. Gate the part of the feature that actually needs access.

## Design choices

1. **Ask at the point of use.** Match the data type, read or write operation, purpose text and signed target. Include SDK data flows when checking privacy declarations. <!-- PRIVACY-101 -->
2. **Show only what the service establishes.** An empty HealthKit query can mean no readable samples. Offer a useful empty state. Handle an actual query error separately and keep unrelated work available. <!-- PRIVACY-102 -->
3. **Account for each external copy.** Separate local save from cloud sync, Health export and system indexing. Export only measured fields. Keep an export ID for retries and decide what sign-out or deletion removes. <!-- PRIVACY-103 -->

## Try it

Follow one workout across the selected boundaries.

- Save with sharing off, then on. Both sessions remain in local history. Only the opted-in export reaches Health. Unmeasured energy stays absent, and an empty query displays “No readings available.” <!-- PRIVACY-101 PRIVACY-102 PRIVACY-103 -->
- After sign-out, search for an indexed private title. Check that the result neither reveals it nor opens the old account’s record. <!-- PRIVACY-102 PRIVACY-103 -->

- [Save a workout when Health sharing is unavailable](references/optional-health-export.md)
