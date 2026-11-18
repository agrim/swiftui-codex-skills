---
name: apple-app-store-readiness
description: "Match an Xcode archive and TestFlight build to the app’s storefront promise, production services, screenshots and App Review access."
---

# Prepare an App Store build a reviewer can actually use

Choose one advertised journey and try it from the reviewer’s starting point. A sharing feature that works between two development accounts still needs a working invitation, production service and usable recipient path in the candidate.

## Design choices

1. **Identify the same candidate everywhere.** Match the Xcode archive’s bundle ID, version and build with the processed build in App Store Connect and the installed TestFlight build. Include any embedded watch app or extension the promise relies on. <!-- STORE-101 -->
2. **Make the journey repeatable outside development.** Use functioning support and privacy URLs, production links and a review account or sample where needed. If hardware, subscriptions or a second user are essential, provide a reproducible route for review. <!-- STORE-102 -->
3. **Reconcile the listing with the installed experience.** Capture the shipping states, check the installed icon and compare the description and privacy answers to actual behavior. Track processing, TestFlight access, review submission, approval and public availability separately. <!-- STORE-103 -->

## Try it

Exercise the feature using only the candidate, access and instructions available to a reviewer.

- Install the selected build via TestFlight and follow the review notes from a clean state. Open any required public link and finish the action through its production path. <!-- STORE-101 STORE-102 -->
- Compare the resulting screens and icon to the storefront assets. Read the exact build’s status in App Store Connect before describing it as available. <!-- STORE-103 -->

- [A reviewer opens an invitation to a shared trip](references/review-a-shared-trip.md)
