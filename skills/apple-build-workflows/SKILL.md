---
name: apple-build-workflows
description: "Set up or repair Xcode and SwiftPM build, test, debug, or simulator workflows. Use for scheme selection, CI reproduction, and failed commands."
---

# Reproducible Apple builds and debugging

## Inputs

Read the build instructions. Identify project, workspace, or package, source revision, toolchain, action, configuration, SDK, and destination.

## Rules

- **BUILD-001 — Discover targets.** Use SwiftPM for package checks it supports. For destination-specific claims, select an available Apple scheme and destination.
- **BUILD-002 — Reuse the CI command.** Use the same settings, dependency locks, and generator inputs locally and in CI.
- **BUILD-003 — Preserve the first failure.** Capture raw output and exit status before formatting. Stop dependent steps on failure.
- **BUILD-004 — Separate side effects.** Plan build, test, install, launch, reset, signing, and publication independently. Execute only the requested actions.
- **BUILD-005 — Inspect executable inputs.** Inspect scripts, plugins, generators and debugger expressions. Run untrusted tools only within the authorized scope.

## Workflow

1. List commands and their file, device, network, or account effects.
2. Run the authorized phase, passing paths and names as separate arguments.
3. Identify the failing phase and rerun it after the fix.

## Verify

- BUILD-002: For a clean-build claim, build the selected scheme or package from a fresh checkout. For test success, confirm the requested cases ran and passed.
- BUILD-003: A failed build returns its nonzero status through the wrapper and prevents launch.

## Output

Report revision, toolchain, destination, commands, exit statuses, artifacts, and blocked or skipped actions.

## References

- [Project discovery, CLI commands, and debugger checks](references/bootstrap-and-cli.md)
