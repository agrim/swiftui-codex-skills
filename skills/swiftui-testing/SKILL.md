---
name: swiftui-testing
description: "Choose Swift Testing, XCTest, UI automation or previews for async, accessibility and behavior regressions."
---

# Test SwiftUI behavior

## Inputs

Identify failure, expectation, destination, toolchain and dependencies.

## Rules

- **TEST-001 — Behavior.** Assert the outcome through the production path.
- **TEST-002 — Ordering.** Control relevant clocks, clients, storage and IDs. Await registration or completion signals.
- **TEST-003 — Isolation.** Give parallel tests independent state, files and accounts. Preview with local fixtures.
- **TEST-004 — Method.** Use Swift Testing or XCTest for behavior, UI automation for interactions, rendered inspection for layout.
- **TEST-005 — Evidence.** Label simulated evidence. Exercise the claimed assistive workflow.

## Workflow

1. Reproduce. Extend the nearest check of the affected path, including cancellation or restoration.
2. Stage visual states. Inspect differences before accepting a baseline.
3. Confirm the check ran. Run affected suites and builds. Preserve distinct behaviors.

## Verify

- TEST-001, TEST-003: Save and cancel concurrently in separate fixtures. Only the saved store changes. Confirm failure before the fix where reproducible, then success.
- TEST-002: Force the failing order and assert final state. Trigger and await late effects inside any zero-count confirmation.
- TEST-004, TEST-005: Complete a claimed VoiceOver journey with VoiceOver. Identify simulated dependencies.

## Output

Give revision, command, toolchain, destination, results, artifacts and skipped checks.

## References

- [Fixtures and regression checks](references/testing-patterns.md)
- [Async tests and migration](references/async-and-migration-tests.md)
