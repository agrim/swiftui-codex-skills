---
name: apple-build-workflows
description: "Set up or repair Xcode and SwiftPM build, test, debug and simulator commands, including CI reproduction."
---

# Reproduce an Xcode build or test failure

Use this to set up a repeatable build, investigate a CI failure or explain why a green test run exercised no tests. The result should identify the command that built the intended product and the first step that failed.

## Start here

Get the revision, CI invocation and raw log. Identify the product under test and where it should run, such as an app on a particular simulator or a Swift package on macOS.

## How to proceed

1. **Select the intended product.** Use SwiftPM for package-only checks. For an app, identify the workspace or project, scheme and destination used by CI. <!-- BUILD-001 -->
2. **Match the build inputs.** Reproduce the toolchain, resolved configuration, dependency lockfiles and generator inputs. Use a fresh checkout when testing a clean build. <!-- BUILD-002 -->
3. **Identify allowed effects.** Check whether the request covers installing, launching, resetting, signing or publishing before taking those steps. <!-- BUILD-004 -->
4. **Inspect what the command will execute.** Review build scripts, package plugins, generators and debugger expressions that can write files, start services or upload data. <!-- BUILD-005 -->
5. **Reproduce the first failure.** Capture the underlying process’s exit status and raw output before formatting. Stop dependent steps, fix the cause and rerun the failed phase. <!-- BUILD-003 -->

## Check the result

- Replay CI on the chosen product and destination. Verify the named tests actually ran and passed. <!-- BUILD-001 BUILD-002 -->
- A failing build must return failure through the wrapper and prevent launch. If a phase uploads symbols, verify its destination and approval before running it. <!-- BUILD-003 BUILD-004 BUILD-005 -->

## What to report

Give the revision, command, toolchain, destination, exit status, relevant artifact and any skipped action.

- [Wrong schemes, zero tests and missing CI test products](references/bootstrap-and-cli.md)
