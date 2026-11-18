---
name: apple-privacy-system-integrations
description: "Integrate HealthKit, CloudKit or another Apple service with a clear permission request, useful fallback and accurate treatment of data that leaves the app."
---

# Add an Apple integration people can trust

Start where the person asks for the feature. A workout diary can save a session locally while optional Health sharing is off. A feature that genuinely needs a live sensor reading should explain why it is unavailable.

## Design choices

1. **Ask for the access the feature needs.** Identify the data type, operation and requesting target. Match its capabilities and purpose text to the real call. Evaluate privacy manifests, SDK behavior and store disclosures against actual data flows. Each artifact serves a different purpose. <!-- PRIVACY-101 -->
2. **Represent what the framework lets you know.** HealthKit can return no readable samples without revealing whether read access was denied. Display the absence of readings honestly. Keep unrelated features usable when permission, account or device availability changes. <!-- PRIVACY-102 -->
3. **Track each copy beyond the app.** Distinguish a local save, cloud sync, Health export and lock-screen projection. Export only fields with a matching meaning, preserve retry identity, and decide what deletion or account changes do to retained copies. <!-- PRIVACY-103 -->

## Try it

Follow one real record through an allowed path and one unavailable path.

- Save the same kind of session with optional sharing off and on. Check the purpose shown, local history, exported fields and retry count. An absent reading stays absent. <!-- PRIVACY-101 PRIVACY-102 PRIVACY-103 -->
- Revoke access or switch accounts, then revisit history and any external display. Check the explanation, remaining local actions and previously visible private details. <!-- PRIVACY-102 PRIVACY-103 -->

- [Save a workout when Health sharing is unavailable](references/optional-health-export.md)
