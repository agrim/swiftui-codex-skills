# Reproducing a CI failure

**Choose the build owner.** Compare the command used by CI with the active project or workspace, scheme, generator inputs and dependency locks. A saved simulator default pointing at a sample app explains a successful build of the wrong product. SwiftPM checks can finish a package-only task. Claims about an app bundle require its actual product and destination.

**Preserve a failure through the wrapper.** Pass paths as argument values. Capture the build process’s status and raw output even when a formatter succeeds. A nonzero build status must prevent install and launch. A green test process with zero matching cases calls for checking the selected plan, filter, skips and executed cases.

**Split CI jobs.** Keep the generated `.xctestrun` with the test products it references. On another runner, match their revision, configuration, paths and compatible destination before accepting a result. If the bundle cannot be found, inspect the restored layout before rebuilding. Yesterday’s green bundle answers only for yesterday’s revision.

**Scope the debugger.** A build script can upload symbols, and a debugger expression can call a service. Check the effects before executing either. If attaching a debugger changes the timing of the failure, remove temporary probes and reproduce on the same candidate without it. Preserve the original error before clearing any state.
