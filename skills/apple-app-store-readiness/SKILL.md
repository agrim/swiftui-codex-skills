---
name: apple-app-store-readiness
description: "Audit App Store candidates and reviewer materials, or perform an authorized TestFlight, submission, or release stage."
---

# Check whether this build is ready for the App Store

Use this to prepare a build for review or advance an approved release. An uploaded build can still be unavailable to testers. Verify which step finished before acting.

## Start here

Identify the app, version and build number, intended audience and storefront. Gather the listing, screenshots, private reviewer instructions and current App Store Connect status.

## How to proceed

1. **Confirm the requested stage.** Match existing approval to the build, audience and action. Check live status before repeating an upload or distributing the build. <!-- STORE-001 -->
2. **Try what the listing promises.** Trace each advertised feature and screenshot to a journey on this build. Mark anything you could not reach. <!-- STORE-002 -->
3. **Check which requirements apply.** Compare the app’s purchases, account flows and actual data use with its storefront disclosures and current requirements. <!-- STORE-003 -->
4. **Rehearse the reviewer’s first launch.** Follow the submitted instructions with the supplied access. Keep credentials private. <!-- STORE-004 -->
5. **Match the results to the candidate.** Trace the source revision and tested archive to the selected build and its service record. <!-- STORE-005 -->

## Check the result

- From first launch, reach support, privacy and advertised features. Where relevant, deny permission, go offline, restore a purchase or start account deletion. Compare what happens with the listing and applicable requirements. <!-- STORE-002 STORE-003 STORE-004 -->
- After an authorized action, reread the build number, stage and audience in App Store Connect. If approval covered upload only, the history should show no new distribution. <!-- STORE-001 STORE-005 -->

## What to report

For each stage, name the build, observed result and any failure, missing evidence, approval limit or inapplicable requirement.

- [Checking a listing against the shipped build](references/app-store-readiness-patterns.md)
- [When an external tester cannot see a build](references/review-and-release-ledger.md)
