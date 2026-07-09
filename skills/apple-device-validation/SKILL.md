---
name: apple-device-validation
description: Apple simulator, physical-device, watch, screenshot, and runtime validation for Swift and SwiftUI apps. Use when building, running, installing, screenshotting, testing, sending to a phone, validating watch parity, diagnosing simulator infrastructure, or proving UI behavior on real Apple devices.
---

# Apple Device Validation

## First Pass

- Resolve the project, scheme, target platform, destination, and requested proof before running tools.
- Prefer XcodeBuildMCP when available for simulator build, run, test, screenshots, UI inspection, and watch/iOS workflows. Verify session defaults before the first build/run/test in a session.
- If using shell tools, record the exact `xcodebuild`, `simctl`, or `devicectl` command and destination.
- Read `references/device-validation-patterns.md` when the task involves screenshots, phone delivery, watch parity, simulator failures, or visual QA.

## Rules

- Build success is not visual proof. Use screenshots when layout, typography, color, glass, truncation, watch sizing, or visual hierarchy matters.
- Simulator proof is not always interaction proof. Use physical-device confirmation when touch, drag, sensor, camera, microphone, watch, or install behavior matters and the user asks for confidence.
- Separate infrastructure failure from app failure. Simulator service crashes, device visibility, install-service errors, and screenshot timeouts should not trigger source changes without evidence.
- When asked to send/install to a phone, install only unless the user explicitly asks to launch, uninstall first, or reset state.
- For watch work, validate both the watch surface and the paired-phone projection when behavior crosses devices.
- Keep screenshots deterministic enough to compare: known device, orientation, state, time policy when possible, and stable output folders.

## Validation

- Run narrow builds/tests first, then visual or device proof.
- Capture affected screens across the smallest relevant device and a representative larger device when truncation or layout is at risk.
- Keep raw logs or command output long enough to separate app failure from tooling failure.
- Summarize what was actually verified and what remains unverified.
