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

The registry holds exact read-file blob hashes where available. These identify the fetched file bytes, not a complete repository audit or an immutable URL to the entire repository revision. Supporting files and tool implementations can have different coverage.

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
