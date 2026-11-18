# SwiftUI Skills

**Practical, source-linked SwiftUI and Apple-platform engineering skills for humans and coding agents.**

Start with a short task contract. Load the few skills the task needs. Follow concrete rules, inspect the current SDK, and prove the resulting behavior. No model, IDE, plugin, or hosted service is required.

The repository URL retains its historical name, `swiftui-codex-skills`. The skill content is provider-neutral; existing skill names and optional adapter metadata remain compatible.

## Start here

Read [the SwiftUI entry point](skills/apple-swiftui-native-apps/SKILL.md), then select a focused module from the [coverage map](docs/coverage.md). Each folder is self-contained: `SKILL.md` supplies the workflow and a local playbook supplies decisions, failure cases, and official sources.

For a host that supports the [Agent Skills format](https://agentskills.io/specification), install the selected folders in that host's configured skill directory. For any other tool, read or attach the Markdown directly, or generate a standalone bundle:

```bash
python3 scripts/skillctl.py route "SwiftUI navigation deep link restores the wrong screen"
python3 scripts/skillctl.py contract swiftui-navigation
python3 scripts/skillctl.py bundle swiftui-navigation swiftui-state-architecture --output selected-skills.md
```

Use `route` to find skills by phrase. If it finds no match, inspect the coverage map. Use `contract` for compact JSON containing the selected skills’ rules, ordered steps, and verification checks. Each check names the rule IDs it exercises. Use `bundle` for standalone Markdown with the playbooks included.

To copy folders into an **existing directory you choose**, without overwriting installed skills:

```bash
python3 scripts/skillctl.py install swiftui-navigation --dest /path/to/skill-directory --dry-run
python3 scripts/skillctl.py install swiftui-navigation --dest /path/to/skill-directory
```

Review changes before replacing an installed version. The installer deliberately has no force-overwrite option. An I/O failure may leave folders already copied; it will not remove user folders to recover.

New installations record content hashes and available Git identity. Inspect them later without writing to the destination:

```bash
python3 scripts/skillctl.py status swiftui-navigation --dest /path/to/skill-directory --diff
python3 scripts/skillctl.py status swiftui-navigation --dest /path/to/skill-directory --json
```

Status distinguishes `missing`, `untracked`, `current`, `source-changed`, `local-changed`, and `both-changed`. `matches_source` reports byte agreement independently: two sides can make the same change after installation. `--diff` lists installed-only, source-only, and modified file names, never file contents. Legacy copies without receipts cannot establish which side changed. Status exit code zero means inspection succeeded, not that every skill matches. No automatic replacement is performed.

The destination must exist and have no symlink ancestors. Resolve a trusted directory explicitly before passing it when your host exposes a canonical location through an alias. Tests canonicalize their own temporary directories; the installer retains its link-rejection policy.

## The library

The catalog contains 29 focused skills and 145 stable rules. All twenty original IDs remain; additional detail loads through local references.

| Work | Skills |
| --- | --- |
| Feature engineering | [Entry point](skills/apple-swiftui-native-apps/SKILL.md), [state and architecture](skills/swiftui-state-architecture/SKILL.md), [concurrency](skills/swift-concurrency/SKILL.md) |
| UI and interaction | [Navigation](skills/swiftui-navigation/SKILL.md), [layout](skills/swiftui-layout/SKILL.md), [controls and input](skills/swiftui-controls-input/SKILL.md), [accessibility](skills/swiftui-accessibility/SKILL.md), [design system](skills/swiftui-design-system/SKILL.md) |
| Data and boundaries | [Persistence](skills/apple-data-persistence/SKILL.md), [networking](skills/apple-networking/SKILL.md), [system experiences](skills/apple-system-experiences/SKILL.md), [privacy](skills/apple-privacy-system-integrations/SKILL.md) |
| Platform engineering | [Platform adaptation](skills/swiftui-platform-adaptation/SKILL.md), [UIKit/AppKit interop](skills/swiftui-interop/SKILL.md), [project governance](skills/apple-project-governance/SKILL.md) |
| Specialist engineering | [Swift language](skills/swift-language/SKILL.md), [build workflows](skills/apple-build-workflows/SKILL.md), [build optimization](skills/xcode-build-optimization/SKILL.md), [SwiftData](skills/swiftdata/SKILL.md), [Core Data](skills/core-data/SKILL.md), [App Intents](skills/apple-app-intents/SKILL.md), [observability](skills/apple-observability/SKILL.md), [background execution](skills/apple-background-execution/SKILL.md), [security](skills/apple-security/SKILL.md) |
| Verification and delivery | [Testing](skills/swiftui-testing/SKILL.md), [performance](skills/apple-performance-cleanup/SKILL.md), [device validation](skills/apple-device-validation/SKILL.md), [App Store readiness](skills/apple-app-store-readiness/SKILL.md), [macOS distribution](skills/macos-productization/SKILL.md) |

Coverage spans common iOS, iPadOS, macOS, watchOS, tvOS, and visionOS decisions. It is **not an exhaustive mirror of Apple documentation**, a guarantee of API availability, or a claim that every platform receives equal depth. The [coverage map](docs/coverage.md) states boundaries; the [source registry](docs/sources.md) distinguishes reviewed content from discovery links.

The [ecosystem integration guide](docs/ecosystem-integration.md) explains the Paul Solt resource review and deliberate limits. The [provenance ledger](docs/ecosystem.md) distinguishes reviewed entry points, public overviews, gated material, and discovery-only links. No third-party prompt pack is a mandatory dependency.

## What makes the rules useful

Each entry point has **Inputs → Rules → Workflow → Verify → Output → References**. Start with the inputs for the task. Cite the rule ID when reporting a finding and record the observed result. If a check could not run, say why. For example, the networking skill asks you to cancel one subscriber to a shared download and verify that the other still receives its image. Open the linked playbook for edge cases or source documentation.

Rules are scoped to failure modes, not arbitrary bans. Native control semantics matter; custom styles are allowed when they preserve behavior and contrast. Interop is a narrow capability boundary, not a forbidden import. `async` is not synonymous with background execution. A build is not a screenshot, device test, or release approval.

[Architecture and adapters](docs/layering.md) explains portability. [Use cases](docs/use-cases.md) shows task-to-skill selection. [Contributing](CONTRIBUTING.md) defines the evidence and maintenance bar.

## Tools and checks

Repository tooling requires Python 3.10+ and only the standard library. The Swift examples require Swift 6.0+; Apple-only views additionally require an Apple SDK. These requirements apply to the tooling/examples, **not** to the deployment minimum of an app using the skills.

```bash
python3 scripts/validate_skills.py .
python3 scripts/skillctl.py docs --check
python3 scripts/upstream_audit.py --check
python3 -m unittest discover -s tests -v
python3 scripts/scan_apple_repo.py /path/to/apple-app --format json
swift test --package-path examples/SkillExamples
```

The validator checks metadata, budgets, rule IDs, catalog/source consistency, local file links, portability, generated documentation, and selected public-hygiene risks. It accepts a documented scalar frontmatter profile, not arbitrary YAML. Optional `agents/openai.yaml` files are neither required nor interpreted by the core validator.

Hygiene checks scan UTF-8 text without NUL bytes regardless of filename, including extensionless files. Binary and other encoded assets are outside these pattern checks. Unreadable files fail validation, as do malformed Markdown, JSON, Python, YAML, Swift, and TOML files. Diagnostics redact matched content. Git metadata, symlinks, and ignored build/dependency directories remain excluded.

The scanner is **advisory lexical triage**, not an AST, compiler, accessibility audit, secret scanner replacement, or HIG certification. It ignores comments and strings for Swift code hints, distinguishes informational review prompts from warnings/errors, and never prints matched secret content. By default only error-level findings fail the command. Use `--fail-on warning` or `--fail-on info` deliberately. Skipped files and known blind spots are reported.

For a plan-first CLI build loop, see [build workflows](docs/build-workflows.md). The helper preserves raw logs and process failures; it does not certify an app or silently install tooling. [The verification matrix](docs/verification-matrix.md) separates implemented checks from remaining runtime and agent evaluations.

The [examples](examples/SkillExamples/README.md) exercise draft ownership, typed routes, value authority, stale-request protection, and a SwiftData rename on disk. The [evaluation protocol](docs/evaluation.md) covers mechanical checks and agent behavior. Two offline pilots record [release and screen-review decisions](evals/pilot-2026-09-09.md) and [interpretation of a scrolling trace](evals/scroll-trace-pilot.md), each with one attempt per condition.

The [deep-link parser](examples/SkillExamples/Sources/SkillExamplesCore/NoteDeepLink.swift) and [its tests](examples/SkillExamples/Tests/SkillExamplesCoreTests/NoteDeepLinkTests.swift) demonstrate a narrow input contract. Parsing a valid route does not establish object access or authorize a mutation.

## Source and maintenance policy

Apple documentation and HIG are authoritative for platform APIs and guidance; installed SDK declarations establish actual compilation availability. This library adds original decision procedures and engineering recommendations. Recheck version-sensitive APIs, beta behavior, privacy rules, and store requirements at use time. Do not turn a review date into a permanent freshness claim.

No Apple documentation is vendored wholesale. Sources are linked and summarized in original playbooks. Apple and SwiftUI are trademarks of Apple Inc.; this is an independent repository, not an Apple endorsement.

## License

The repository owner has not selected a license. This update does not grant a new license to existing or contributed material. Resolve licensing before presenting the project as freely reusable open-source software or distributing third-party contributions under assumed terms.
