# Performance Cleanup Playbook

Use this playbook after establishing an explicit performance or memory constraint. Preserve existing behavior, edge-case fixes, and diagnostics while removing or reorganizing work.

## Write the Contract Before Editing

Record the smallest useful contract:

- Name the hot, startup-sensitive, user-visible, allocation-sensitive, or leak-producing path.
- List observable outputs, side effects, error behavior, ordering, cancellation, thread or actor ownership, persistence, logging, and UI projections that must remain stable.
- Identify the current tests, source samples, traces, metrics, or bug reproductions that establish the baseline.
- State the suspected cost and whether it is measured, inferred from code structure, or still unknown.
- Choose evidence proportional to the risk before selecting a transformation.

Read the implementation and every relevant call site before extracting a helper. Include debug-only branches and source-format quirks; cleanup must not erase an existing fix merely because the common path looks simpler.

## Whole-Repository Compaction Protocol

Use this protocol only for an explicit broad-compaction request. The objective is the smallest codebase that still expresses and proves the product contract clearly, not the smallest raw line count.

### 1. Freeze A Reproducible Baseline

- Record the intentional source state, branch, generated-project state, toolchain, build configuration, and known unrelated changes.
- Run the broadest relevant behavior suite and retain compatibility fixtures, representative data, warnings, analyzer output, and packaging or extension checks.
- Capture comparable launch, hot-path, memory, allocation, binary or bundle evidence only for metrics that matter to the contract.
- Preserve a reference build or source archive outside generated and cleanup-prone directories when it materially improves comparison. Create a commit or tag only when the user authorizes it.

### 2. Produce A Complete Pass Report

Inventory the whole repository before editing and classify candidates:

| Candidate class | Ask before changing it | Typical proof |
| --- | --- | --- |
| Duplicate production behavior | Are implementations semantically identical across all call sites and platforms? | Call-site matrix, state and failure tests, target builds |
| Redundant state or model storage | Does each field preserve a distinct lifecycle, compatibility, projection, or persistence meaning? | Migration and round-trip tests, memory-layout evidence when relevant |
| Obsolete compatibility path | Which supported version, data format, device, or migration still needs it? | Version policy, legacy fixtures, installed-data migration |
| Repeated test machinery | Are only helpers duplicated, or would consolidation erase a unique scenario or assertion? | Scenario inventory before and after, complete test outcomes |
| Generated or dead code | Is it owned by a generator, reflection, serialization, target membership, runtime discovery, or conditional build? | Source-owner inspection, target builds, generated diff, runtime registration |
| Abstraction overhead | Does the layer clarify a stable boundary, or only forward calls and allocate work? | Call graph, allocation or trace evidence, error and ownership review |
| Diagnostics and fallbacks | Do logs, debug branches, stale-data retention, retry, or graceful degradation encode a prior production fix? | Failure fixtures, debug-output checks, runtime recovery proof |

Rank candidates by confidence, expected simplification, semantic risk, performance risk, and required evidence. Organize the work into coherent passes such as model consolidation, duplicate behavior, test infrastructure, or dead compatibility—not arbitrary file order.

### 3. Execute And Re-scan By Pass

For each pass:

1. State the complete candidate set and invariants before editing.
2. Apply small reviewable transformations within that semantic group.
3. Run the pass-specific behavior and performance checks.
4. Run the broad regression gate appropriate to the accumulated risk.
5. Record source and artifact changes without treating reduction alone as success.
6. Re-scan the entire simplified repository and write the next pass from current evidence.

Do not defer all verification until the end. Conversely, do not abandon the whole-repo view and turn the effort into unrelated one-file cleanups. Preserve proof scenarios rather than arbitrary test-method counts; consolidate exact duplicates only when the resulting matrix still names every scenario.

### 4. Track Honest Metrics

| Metric | Useful for | Does not prove |
| --- | --- | --- |
| Production source lines or bytes | Directional structural reduction | Readability, behavior preservation, or faster runtime |
| Test source lines or bytes | Helper and fixture consolidation | Preserved scenario coverage |
| Test scenario and assertion inventory | Detecting lost unique behavior | Runtime performance or production size |
| Built app, extension, binary, or package size | Shipping-artifact impact | Faster launch, lower memory, or correct signing |
| Stored-model stride or serialized size | A specific memory or persistence change | Whole-app memory improvement or migration safety |
| Launch, throughput, allocation, RSS, CPU, hitch, or trace evidence | The named runtime cost under recorded conditions | Other devices, states, or unmeasured paths |

Keep before-and-after conditions comparable. A reduction in code or bundle size is worthwhile evidence, but not a performance claim unless the relevant runtime cost was measured.

### 5. Apply A Stop Rule

Stop when the remaining candidates require any of the following without a product reason and stronger proof:

- flattening distinct domain or lifecycle states;
- removing supported migration or data compatibility;
- deleting unique regression scenarios or diagnostics;
- obscuring actor, thread, ownership, or error boundaries;
- replacing readable code with compressed cleverness;
- changing public behavior or platform support; or
- accepting a measured regression to achieve a cosmetic size target.

Finish with a final independent residual scan. Report why each surviving large or repetitive area earns its keep and distinguish “no more safe compaction found” from “the codebase is theoretically minimal.”

## Risk-to-Evidence Matrix

| Risk surface | Behavior proof | Performance proof | Specialized pairing when diagnosis is primary |
| --- | --- | --- | --- |
| Parsing or telemetry | Source-contract fixtures, exact value and error assertions, debug-output checks | Repeated representative workload, decode or event count, allocation or duration evidence | Trace or allocation profiler |
| Startup or launch | Launch state, initialization order, readiness, fallback, and failure tests | Comparable cold and warm launch samples; trace expensive stacks | An ETTrace or equivalent launch profiler |
| SwiftUI rendering or invalidation | State-transition, interaction, layout, and projection checks | Update counts, hitch or frame evidence, body-cost trace | A SwiftUI performance-audit workflow, then a trace if needed |
| Persistence or I/O | Round-trip, migration, ordering, cancellation, and failure tests | Read/write counts, bytes, duration, and main-thread evidence | I/O or runtime profiler |
| Allocation, memory growth, or a confirmed leak | Object-lifetime and teardown behavior; retained state remains available as required | Allocation trend, steady-state memory, leak reproduction, before/after memgraph | A memgraph or equivalent leak workflow |
| Concurrency or synchronization | Ordering, isolation, cancellation, reentrancy, and error propagation | Contention, wait time, task count, or end-to-end latency | Concurrency instrument or runtime trace |

Use source-contract tests when parsing or telemetry behavior depends on upstream formats. A synthetic happy-path test alone does not protect source quirks.

## Keep Behavior Proof Separate from Performance Proof

Behavior proof answers: **Does the same input and state still produce the required result and side effects?**

- Exercise representative normal, boundary, unavailable, and failure cases before and after the change.
- Verify ordering, actor or thread ownership, cancellation, persistence, diagnostics, and UI projection when they are part of the contract.
- Retain focused regression tests for the exact behavior that motivated the original code, including debug fixes.
- Treat compile success as structural evidence only. It does not prove behavior or runtime performance.

Performance proof answers: **Did the relevant cost improve, or remain inside an explicit non-regression bound, without moving it somewhere unmeasured?**

- Name the metric before measuring: launch duration, event throughput, work count, allocation count, retained memory, I/O, invalidation, hitching, or another path-specific cost.
- Capture a baseline before editing whenever the environment permits.
- Compare the same build configuration, optimization level, hardware or simulator, OS/runtime, data size, app state, and instrumentation.
- Keep cold and warm runs separate. Record warm-up and cache policy instead of mixing them.
- Run enough samples to expose variance. Report the center and spread or the raw range; never select only the best run.
- Define any non-regression threshold before comparing results. Treat a result inside ordinary run-to-run variance as inconclusive; investigate noise or use a stronger workload before claiming improvement or regression.
- Keep instrumentation overhead comparable on both sides and retain raw evidence long enough to audit the conclusion.

If measurement is impossible, make only a bounded structural claim such as “removes one decode per event” or “avoids scheduling a duplicate task.” Do not translate that observation into an unmeasured latency, launch, memory, or responsiveness claim.

## Keep Discrete Interactions Free Of Maintenance Work

For a tap whose user-visible job is to navigate, dismiss, or confirm a short local action:

- Keep the handler limited to validation and the state transition the user requested. Do not synchronously seed a database, run broad fetches, save unrelated defaults, read files, or wait on a service before showing the destination.
- Render the destination first, then start required preparation on the appropriate isolated executor. Gate only the control that truly depends on that preparation; keep its label and geometry stable when the expected wait is brief.
- Snapshot mutable form input before launching asynchronous persistence. Give completion work an owner that remains mounted if navigation changes while the save is in flight.
- Do not disguise the same blocking work with `Task.yield`, an arbitrary sleep, a spinner, or by relocating it to the next tap. Re-measure the original interaction and the downstream action so the cost was removed rather than moved.
- Exercise a real cold state as well as a warm state. A multi-second UI existence timeout proves eventual navigation, not responsiveness, and a reused store can omit the expensive first-run branch.

Use a focused source contract to keep database and delay calls out of the discrete action. Pair that behavior proof with a physical-device Hang Detection or Instruments trace when the defect was observed on hardware; actor isolation and passing result tests do not by themselves prove that the main run loop stayed responsive. Apple's responsiveness guidance recommends keeping discrete main-thread work below 100 milliseconds and using Hang Detection or Instruments for longer stalls: [Improving app responsiveness](https://developer.apple.com/documentation/xcode/improving-app-responsiveness).

## Preserve State Semantics

Do not flatten states merely because they share a storage type or visual fallback:

| State | Meaning to preserve |
| --- | --- |
| nil or missing | No value was supplied or derived |
| zero | A present, valid measurement whose value is zero |
| unavailable | The source or capability cannot currently provide a value |
| stale | A prior value exists but is no longer current |
| denied | Policy or permission prevents access |
| failed | An attempted operation produced an error |

Preserve each state's fallback, caching, retry, error reporting, telemetry, and UI behavior unless the requested product change explicitly redefines it.

## Choose the Smallest Safe Transformation

- Prefer helper extraction, duplicated-branch removal, early exits, cached derived work, and narrower invalidation over architecture churn.
- Do not add a convenience wrapper, allocation, main-thread hop, log, lock, actor hop, persistence write, or view invalidation to a hot path merely for tidiness. Add one when its correctness or observability benefit is justified and the relevant evidence shows the tradeoff is acceptable.
- Defer or remove startup work only after proving initialization order, readiness, and failure behavior.
- Move formatting, timers, derived values, and expensive work out of SwiftUI `body` when they are recomputed unnecessarily; do not create wider-lived state without considering invalidation and lifetime costs.
- Correct concurrency ownership and isolation. Do not silence warnings with unchecked annotations, unnecessary dispatch, or synchronization that obscures the actual owner.
- Keep the diff narrow enough to review. If multiple transformations are needed, validate them independently where practical.

## Report Completion Precisely

State:

- what behavior was preserved and how it was proved;
- what performance evidence was collected under which conditions;
- which improvement is measured versus structurally inferred;
- which states and failure paths were exercised;
- what remains unmeasured, inconclusive, or unverified.
