---
name: apple-system-experiences
description: "Integrate widgets, Live Activities, notifications, Spotlight, WatchConnectivity, HealthKit, and StoreKit."
---

# Keep system features in sync with the app

Use this when app data appears or changes outside the main app, such as a pass in a widget or an edit sent from a watch. Trace one record to its destination.

## Start here

For a widget that shows an expired pass as valid, find the stored pass, its expiry, the installed widget, and the affected account and device.

## How to proceed

1. **Choose the source of truth.** Decide which record the destination should display and how it should look after expiry, deletion or loss of access. <!-- SYS-001 -->
2. **Preserve the record’s meaning.** Keep the exported type and units consistent with the source. If the system hides read permission, leave it unknown. <!-- SYS-004 -->
3. **Trace the handoff.** Follow one record ID and revision from the request or queue to the receiving feature. Check which revision it actually applied. <!-- SYS-003 -->
4. **Reuse the app’s action for writes.** Validate the record, account access and required confirmation at execution. Reconcile a repeated delivery before applying its effect again. <!-- SYS-002 -->
5. **Exercise the receiving feature.** Check that the app ships and registers any required extension. On the device, confirm the destination can access the record and displays the intended change. <!-- SYS-005 -->

## Check the result

- Delay a refresh across restart and expiry. The installed widget marks the old pass stale or shows its fallback. <!-- SYS-001 SYS-003 SYS-005 -->
- Deliver the same watch edit twice. The app records one change. <!-- SYS-002 -->
- Export a workout and compare its units on-device. Switch accounts and check that private records disappear. An empty HealthKit read leaves read permission unknown. <!-- SYS-004 SYS-005 -->

## What to report

Identify the source record, destination, last observed handoff and user-visible result.

- [Choose what each system feature can show or change](references/system-patterns.md)
- [Check delivery, expiry and recovery](references/system-surface-contracts.md)
