---
name: swiftui-testing
description: "Choose Swift Testing, XCTest, UI automation or preview fixtures for a SwiftUI regression. Verify async ordering, accessibility and visible behavior."
---

# Behavior tests, previews, and evidence

## Inputs

Identify the failure, expected outcome, target, toolchain and dependencies to control.

## Rules

- **TEST-001 — Assert the user outcome.** Exercise the production path. For a cancelled edit, assert that the store is unchanged.
- **TEST-002 — Control time and I/O.** Inject clocks, clients, storage or IDs that affect the result. Order async work with registration or completion signals.
- **TEST-003 — Isolate fixtures.** Give concurrent tests independent state, files and test accounts. Use local fixtures in previews.
- **TEST-004 — Match the check to the claim.** Use Swift Testing or XCTest for behavior, UI automation for interactions and rendered inspection for layout.
- **TEST-005 — Label the evidence.** Identify which dependencies were simulated. Exercise assistive workflows with the relevant assistive technology.

## Workflow

1. Reproduce the defect. Extend the nearest test that exercises the failing path, including cancellation or restoration where relevant.
2. Stage affected visual states with fixtures. Inspect differences before accepting a new baseline.
3. Run the targeted check, affected suites and destination builds. Preserve distinct behavior checks when replacing tests.

## Verify

- TEST-001: Confirm the selected regression test executed. Where reproducible, it fails before the fix and passes afterward.
- TEST-002: For a race, force the failing completion order and assert the expected final state. For a zero-count confirmation, drive the late callback and await its effects inside the confirmation.

## Output

Report the source revision, command, toolchain, destination, results, artifacts and skipped checks.

## References

- [Fixtures, evidence and regression checks](references/testing-patterns.md)
- [Async streams, confirmations and test migration](references/async-and-migration-tests.md)
