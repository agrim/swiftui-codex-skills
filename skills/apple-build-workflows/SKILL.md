---
name: apple-build-workflows
description: "Set up or repair Xcode and SwiftPM build, test, debug and simulator commands, including CI reproduction."
---

# Apple build workflows

## Inputs

Read the CI invocation. Identify revision, toolchain, owner, action and destination.

## Rules

- **BUILD-001 — Select the build.** Use SwiftPM for package-only checks. Exercise app claims on the intended scheme and destination.
- **BUILD-002 — Reproduce CI.** Match configuration, locks and generator inputs.
- **BUILD-003 — Preserve failures.** Capture raw output and exit status before formatting. Stop dependent actions on failure.
- **BUILD-004 — Bound side effects.** Build, install, launch, reset, sign or publish only as authorized.
- **BUILD-005 — Inspect executable inputs.** Check scripts, plugins, generators and debugger expressions before running untrusted code.

## Workflow

1. Resolve active settings and review the command’s effects.
2. Reproduce the first failure. Rerun that phase after the fix.

## Verify

- BUILD-001, BUILD-002: Replay CI with its scheme or package, destination, lockfiles and generator inputs. Use a fresh checkout for clean-build claims. Confirm the requested tests passed.
- BUILD-003, BUILD-004: A build failure survives the wrapper and prevents launch.
- BUILD-005: If a phase uploads symbols, identify its destination and confirm upload authorization before execution.

## Output

Report revision, command, environment, status, artifacts and skipped actions.

## References

- [Discovery, CI and debugging](references/bootstrap-and-cli.md)
