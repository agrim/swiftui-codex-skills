# Reproducible build plans and evidence

The [build workflow skill](../skills/apple-build-workflows/SKILL.md) chooses the right project and proof. The [optimization skill](../skills/xcode-build-optimization/SKILL.md) separates orchestration, benchmarking, compiler diagnostics, project configuration, packages, and verification.

The standard-library helper `scripts/apple_build.py` implements a narrow contract. It is not an Xcode project generator, simulator driver, package installer, release tool, or security sandbox.

## Configure and inspect

Copy [the example JSON](../templates/apple-build.json) to the app repository and replace its project, scheme, configuration, and destination using actual discovery. Choose exactly one `project` or `workspace`; do not guess from the mere presence of both. Paths are relative to the explicitly supplied app root. The named project/workspace must exist and cannot traverse symlinks.

From this library checkout:

```bash
python3 scripts/apple_build.py plan --root /path/to/app --config /path/to/app/apple-build.json
```

`plan` prints structured JSON and executes nothing. It does not create a build folder, mutate a project, select a global Xcode version, install dependencies, or accept tool trust prompts.

## Execute an authorized build or test

```bash
python3 scripts/apple_build.py run --root /path/to/app --config /path/to/app/apple-build.json --output /path/to/new-run --execute
python3 scripts/apple_build.py run --root /path/to/app --config /path/to/app/apple-build.json --action test --output /path/to/new-test-run --execute
```

The output directory's parent must already exist; the chosen directory must not exist. Each run keeps raw combined output in `build.log`, a structured `result.json`, scoped DerivedData, and the requested `.xcresult` location. A failed build preserves its exit status rather than allowing a successful formatter or `tee` to hide it. A missing executable and a timeout are not successes. The result-bundle field is the requested path, not proof that Xcode produced a valid bundle.

A successful process is only process evidence. For tests, inspect actual discovered/executed tests, failures, skips, and the destination. For UI, install/launch/render/operate separately within scope. No automatic retry, cleanup, reset, installation, upload, or release is performed.

**Trust boundary:** Xcode project scripts, package plugins, macros, dependency resolution, and configured signing may execute code or access the network. Review these before `--execute`. This helper neither sandboxes them nor guarantees that a timed-out process's descendants have stopped. A failed filesystem write can also leave partial output. Logs may contain sensitive paths, data, or credentials; keep them local and review before sharing.

## Descriptive benchmark summaries

The helper deliberately does not automate deleting build caches or touching source files. Record measurements from a controlled protocol as:

```json
{
  "schema_version": 1,
  "contract": {
    "source": "record the actual commit and dirty-state policy",
    "toolchain": "record the installed Xcode and Swift versions",
    "destination": "record the selected destination and runtime",
    "configuration": "Debug",
    "workload": "no-change rebuild after a successful baseline",
    "cache_policy": "warm scoped build output; describe external caches"
  },
  "samples": [
    {"phase": "no-change", "seconds": 3.1, "exit_code": 0},
    {"phase": "no-change", "seconds": 3.3, "exit_code": 0},
    {"phase": "no-change", "seconds": 3.2, "exit_code": 0}
  ]
}
```

These numbers are synthetic format examples, not measured repository performance. Run `python3 scripts/apple_build.py summarize measurements.json`. Results retain failed-sample counts and report median/min/max only for successful samples, with null values when none succeeded. Three successful samples meet a reporting minimum, not a significance test. No speedup is inferred. Separate clean, warmed-cache, no-change, and real-edit workloads; do not silently discard warm-up or failed observations.

[The optional Makefile](../templates/Makefile.apple) calls the same helper. It requires explicit library root, app root, configuration, and fresh output paths; `plan` is the default goal. It is a template, not a silently installed global workflow.
