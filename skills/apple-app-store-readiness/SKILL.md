---
name: apple-app-store-readiness
description: "Verify that a specific TestFlight or App Store build delivers its listing, works for a reviewer and has reached the requested distribution stage."
---

# Prepare an App Store build a reviewer can actually use

Can a reviewer open a shared-trip invitation on a clean install and finish as the recipient? Start there, with the build the listing describes.

## Design choices

1. **Pin the build.** Trace the Xcode archive to the uploaded build number and match that build in App Store Connect and TestFlight. Check the companion if the feature uses it. <!-- STORE-101 -->
2. **Give the reviewer a working route.** Provide the access, sample data and hardware instructions the feature needs. Exercise its public links and services, including support and privacy pages. <!-- STORE-102 -->
3. **Check what testers or customers can get.** Compare screenshots, icon, description and privacy answers with that build. Check the exact group’s TestFlight access or the storefront’s availability before reporting delivery. Processing, approval and release are separate events. <!-- STORE-103 -->

## Try it

Start with the supplied review notes and access.

- Open the invitation in the selected candidate. After signing in, the recipient lands on that trip and can join it. <!-- STORE-101 STORE-102 -->
- For beta delivery, a tester in the named group can install that build. For public release, the intended storefront offers that version and its listing matches the installed result. <!-- STORE-103 -->

- [A reviewer opens an invitation to a shared trip](references/review-a-shared-trip.md)
