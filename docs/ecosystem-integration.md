# Integrating the Apple skills ecosystem

This revision uses original engineering guidance, not a concatenation of upstream prompts. Start with the [coverage map](coverage.md); use the [provenance map](ecosystem.md) to inspect what was actually read and how it maps to local skills.

## Scope and access

The requested Paul Solt X article did not expose its full body during this review. Its author newsletter and an independently maintained resource list that explicitly cites the exact post established a best-effort inventory. The registry separately marks recovered article resources, current collection members, supporting evidence, and one-level directory discoveries. It does not claim that every link in a changing directory appeared in the original article.

All twenty original skill IDs remain. Each gains a focused optional reference; nine distinct specialists cover Swift language/API design, build workflows, build optimization, SwiftData, Core Data, App Intents, observability, background execution, and security. No mandatory model, editor, architecture, package, paid service, or MCP server is introduced.

## What was incorporated

| Resource family | Local treatment |
| --- | --- |
| Paul Hudson's directory and four focused skills | Review-first API/state/test/data decisions; secondary directory links stay discoverable without pretending they were audited |
| Antoine van der Lee's SwiftUI, concurrency, testing, Core Data, and build skills | Diagnostic routing, lifecycle-specific tests, contextual isolation, query/migration decisions, and six separate build-optimization tracks |
| Official iOS and macOS plugin collections | Twenty current entry points mapped to native UI, system actions, build/debug, trace/leak analysis, desktop scenes, signing, and distribution workflows |
| Krzysztof Zabłocki's public rules and related tools | Progressive loading, explicit dependencies, meaningful contracts, and source-owned generation; no prescribed architecture or course content copied |
| Paul Solt's AppCreator | Publicly described build-loop idea implemented independently with an explicit JSON plan, raw logs, return codes, and an optional Makefile |

The registry holds exact read-file blob hashes where available. New receipts include the commit and link directly to the file at that revision.

## Failure cases from the wider review

| Public example or skill | Local decision it helped clarify |
| --- | --- |
| Point-Free's identified collections and Paul Hudson's navigation review | Resolve a late save against the current record and edit. Check the visible Back history when direct-view and value links share a stack. |
| Hudson's accessibility review and CVS Health's spoken-label examples | Carry a draft through a layout change, then invoke the relocated action by its localized visible title. |
| Antoine van der Lee’s async sequence and testing references and the write-swift skill | Stage overflow before reading a stream. Join observer teardown and inject a late callback while the stream remains alive. |
| Nuke's request-coalescing tests | Let one caller leave a shared download while another continues. Reject late callbacks after a same-key replacement. |
| Dimillian’s performance audit | Inspect the CPU samples inside the hitch interval and check the same gesture after a change. |
| Hudson's SwiftData rules and the SwiftData Expert migration reference | Open a store at the previous schema, match each renamed field to its business ID, save an edit, and reopen again. |

The [provenance map](ecosystem.md) links the exact files inspected. The [primary-source registry](sources.md) records the Apple and Swift sources used to check the resulting platform guidance.

## Specialist skill review, November 2026

This pass reviewed 29 files across 12 GitHub repositories for decisions missing from the local playbooks. On November 18, Nuke had 8,698 stars, MobileBuildMCP had 6,585, Paul Hudson’s SwiftUI skill had 6,581, Dimillian’s collection had 4,029 and Antoine van der Lee’s SwiftUI skill had 3,931. Narrower collections supplied the Core Data, SwiftData, testing, concurrency and release cases. The file receipts record which passages informed each skill. [Reviewed files](ecosystem.md)

| Upstream example | Decision in the local playbook |
| --- | --- |
| [Dimillian’s scoped search](https://github.com/Dimillian/Skills/blob/05ba982bfeb0d77d3c97d4542b0ee15034d05f84/swiftui-ui-patterns/references/searchable.md) | The example changes scope but keys its task only to text. The [search playbook](../skills/swift-concurrency/references/concurrency-patterns.md) exercises a scope switch both during debounce and after a request starts. |
| [Nuke’s image-sizing skill](https://github.com/kean/Nuke/blob/740dff31db9d4b1916a1651e5e50abccd1f18cdf/Skills/nuke-optimize/SKILL.md) | The [networking playbook](../skills/apple-networking/references/transport-and-cache-boundaries.md) checks two screen scales. They can reuse source bytes and still need different decoded thumbnails. |
| [Axiom’s hang diagnosis](https://github.com/CharlesWiltgen/Axiom/blob/ffafd3b3e0dbaaa60b753ca4a835ae6603b873e1/axiom-codex/skills/axiom-performance/skills/hang-diagnostics.md) | In a freeze, another thread can keep process CPU high while the main thread waits. The [diagnostic playbook](../skills/apple-observability/references/logging-and-traces.md) follows the wait to the operation that can release it. |
| [TestFlight orchestration](https://github.com/rorkai/app-store-connect-cli-skills/blob/6d1c3c55fe4590fcbc3e3115de18c5721a73c23b/skills/asc-testflight-orchestration/SKILL.md) | The [release playbook](../skills/apple-app-store-readiness/references/review-and-release-ledger.md) distinguishes a build limited to internal groups from an externally approved build awaiting manual distribution. |

## Decisions deliberately not imported

Do not raise every app's deployment target to an upstream author's preferred OS/compiler. Check the installed SDK, language mode, and minimum supported runtime separately. Do not migrate an API merely because a newer spelling exists during unrelated work.

Do not turn an architectural preference into a universal requirement. Small value state, observable reference models, explicit injection, environments, coordinators, and established app architectures have different valid roles. Likewise, not every gesture is a fake button, not every custom binding is defective, and not every platform bridge is unnecessary.

Do not treat cumulative compilation seconds as elapsed savings or a simple ratio as proof of the critical path. Benchmark the developer's actual workload. Build settings remain reversible when compatibility, correctness, or measured costs require it; an upstream performance percentage is not a result for this project.

Do not describe task groups as always cancelling children on normal scope exit. They wait for their children; cancellation must follow the relevant API and control flow. An asynchronous sleep does not block an actor's thread merely because its caller is actor-isolated. Avoid fake suspension points and arbitrary sleeps in tests.

Do not use timestamps, a successfully started process, a screenshot, or an empty trace lane as stronger evidence than they provide. Source, build, execution, rendering, hardware, persistence, release, and comparative model outcomes remain separate claims.

## Optional tools, not dependencies

**XcodeBuildMCP:** can provide discovery, simulator, device, logging, and build operations. Read the current installed tool schema; do not freeze tool names into portable skills. Review macro-validation bypasses and telemetry settings before use. Shell/Xcode workflows remain valid alternatives.

**CodexMonitor:** is an optional workspace/agent host. It does not own domain rules or grant permission to access unrelated workspaces. Parallel agents need isolated edits and an explicit reconciliation step; no private session or memory harvesting is required by this library.

**Inject:** is optional hot reloading. Review supported targets, debug-only integration, and release artifact behavior. A reloaded frame is not a cold launch, persistence migration, or release build. Do not install an automatic source-rewriting build phase merely to shorten iteration.

**Sourcery:** is optional code generation. Own templates, configuration, inputs, and output membership in source control. Keep generated files deterministic, avoid rewriting unchanged content, and compile the generated result. Generated mocks do not prove real framework behavior.

**AppCreator / SwiftyStack:** the AppCreator public landing page was inspected, but its email-gated payload was not downloaded. The complete SwiftyStack course rules were not accessed. Neither is copied or represented as fully integrated.

## Maintenance and reuse

`sources.json` is the Apple/Swift authority registry. `upstreams.json` is the community/plugin provenance ledger. Do not mix popularity with API authority, or update review dates merely because a URL responds. Run `python3 scripts/upstream_audit.py --write` after deliberate provenance edits, then `--check` in verification.

No upstream skill bodies or scripts are vendored. Before future copying, inspect the exact revision's license, preserve notices, record modified files, and resolve compatibility with the owner's selected license. This revision does not choose that license. A public repository and a README badge do not independently grant new terms to this library.
