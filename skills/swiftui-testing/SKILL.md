---
name: swiftui-testing
description: "Choose Swift Testing, XCTest, UI automation or previews for async, accessibility and behavior regressions."
---

# Choose a test that catches the SwiftUI regression

Use this to choose the smallest test that can catch a reported defect. A store test can expose an unwanted save. A VoiceOver user unable to reach Cancel needs an interaction test.

## Start here

Describe the action, expected outcome and affected build and destination. Find an existing test that reaches the same code.

## How to proceed

1. **Test at the level where the defect appears.** Check a wrong value in logic or storage, clipping in a rendered view and a broken control by activating it. <!-- TEST-004 -->
2. **Drive the production path.** Assert what the caller sees or what survives reopening. Reproduce the failure before fixing it when possible. Keep cases with distinct outcomes. <!-- TEST-001 -->
3. **Control event order.** Use a controllable client or clock. Wait for registration before releasing the response. <!-- TEST-002 -->
4. **Separate each test’s data.** Give parallel cases their own stores, accounts and mutable fixtures. Use local fixtures in previews. Inspect visual differences before accepting a new baseline. <!-- TEST-003 -->
5. **Verify the claimed experience.** Name simulated dependencies. For accessibility, use the claimed input. Confirm the selected cases ran and build the affected targets. <!-- TEST-005 -->

## Check the result

- Save in one fixture while cancelling in another. Only the saved store changes on reopen. <!-- TEST-001 TEST-003 -->
- Finish the older request last. Its result or error leaves the newer screen intact. Trigger and await any late callback before asserting zero updates. <!-- TEST-002 -->
- Find Cancel with VoiceOver and activate it. Verify the resulting screen and saved value. Identify any simulated store. <!-- TEST-004 TEST-005 -->

## What to report

Give the revision, command, toolchain, destination, outcome, supporting evidence and any skipped cases.

- [Choose fixtures and regression checks](references/testing-patterns.md)
- [Test callback timing and consolidate repeated cases](references/async-and-migration-tests.md)
