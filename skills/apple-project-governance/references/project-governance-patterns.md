# Trace a configuration change to the product

| Report | Source owner to inspect | Product evidence |
| --- | --- | --- |
| CI misses a test target | Shared scheme, test plan and CI selection | Requested cases in the test result |
| The extension lacks an entitlement | Extension’s entitlement inputs, configuration and provisioning | Entitlements on the signed extension |
| A dependency intended for one extension reaches the app | Resolved version, binary distribution terms, platform constraints and target dependencies | Which shipping products link or embed the dependency |
| A permission prompt has stale text | Plist inputs, localization and target membership | Built plist and prompt on the affected locale |
| A model, privacy manifest or icon is missing | Resource pipeline and product membership | Compiled resource in the intended product |
| An extension cannot read existing data after a rename | App and extension identifiers, groups, containers and storage keys | Seeded pre-upgrade data accessible to both consumers |

Follow the row only as far as the requested claim. A generator can own part of a project. Identify its input before regenerating, keep unrelated edits intact and inspect the resulting diff. Compare products built for the affected configuration and destination. Debug simulator output cannot settle a Release signing discrepancy.

For a product rename, separate displayed names and icon inputs from durable identifiers. Keep an existing identifier unless migration is intended. Exercise the upgrade against real pre-change state when a persisted identity changes.
