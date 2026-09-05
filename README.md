# SwiftUI Skills

**Practical, source-linked SwiftUI and Apple-platform engineering skills for humans and coding agents.**

Start with a short task contract. Load the few skills the task needs. Follow concrete rules, inspect the current SDK, and prove the resulting behavior. No model, IDE, plugin, or hosted service is required.

The repository URL retains its historical name, `swiftui-codex-skills`. The skill content is provider-neutral; existing skill names and optional adapter metadata remain compatible.

## Start here

Read [the SwiftUI entry point](skills/apple-swiftui-native-apps/SKILL.md), then select a focused module from the [coverage map](docs/coverage.md). Each folder is self-contained: `SKILL.md` supplies the workflow and a local playbook supplies decisions, failure cases, and official sources.

For a host that supports the [Agent Skills format](https://agentskills.io/specification), install the selected folders in that host's configured skill directory. For any other tool, read or attach the Markdown directly, or generate a standalone bundle:

```bash
python3 scripts/skillctl.py route "SwiftUI navigation deep link restores the wrong screen"
python3 scripts/skillctl.py bundle swiftui-navigation swiftui-state-architecture --output selected-skills.md
```

The router performs deterministic phrase matching, not model inference. No match means “inspect the catalog,” not “no skill applies.” Bundles contain only the selected skills and their playbooks; they do not require this repository's surrounding directory structure.

To copy folders into an **existing directory you choose**, without overwriting installed skills:

```bash
python3 scripts/skillctl.py install swiftui-navigation --dest /path/to/skill-directory --dry-run
python3 scripts/skillctl.py install swiftui-navigation --dest /path/to/skill-directory
```

Review changes before replacing an installed version. The installer deliberately has no force-overwrite option. An I/O failure may leave folders already copied; it will not remove user folders to recover.

## The library

| Work | Skills |
| --- | --- |
| Feature engineering | [Entry point](skills/apple-swiftui-native-apps/SKILL.md), [state and architecture](skills/swiftui-state-architecture/SKILL.md), [concurrency](skills/swift-concurrency/SKILL.md) |
| UI and interaction | [Navigation](skills/swiftui-navigation/SKILL.md), [layout](skills/swiftui-layout/SKILL.md), [controls and input](skills/swiftui-controls-input/SKILL.md), [accessibility](skills/swiftui-accessibility/SKILL.md), [design system](skills/swiftui-design-system/SKILL.md) |
| Data and boundaries | [Persistence](skills/apple-data-persistence/SKILL.md), [networking](skills/apple-networking/SKILL.md), [system experiences](skills/apple-system-experiences/SKILL.md), [privacy](skills/apple-privacy-system-integrations/SKILL.md) |
| Platform engineering | [Platform adaptation](skills/swiftui-platform-adaptation/SKILL.md), [UIKit/AppKit interop](skills/swiftui-interop/SKILL.md), [project governance](skills/apple-project-governance/SKILL.md) |
| Verification and delivery | [Testing](skills/swiftui-testing/SKILL.md), [performance](skills/apple-performance-cleanup/SKILL.md), [device validation](skills/apple-device-validation/SKILL.md), [App Store readiness](skills/apple-app-store-readiness/SKILL.md), [macOS distribution](skills/macos-productization/SKILL.md) |

Coverage spans common iOS, iPadOS, macOS, watchOS, tvOS, and visionOS decisions. It is **not an exhaustive mirror of Apple documentation**, a guarantee of API availability, or a claim that every platform receives equal depth. The [coverage map](docs/coverage.md) states boundaries; the [source registry](docs/sources.md) distinguishes reviewed content from discovery links.

## What makes the rules useful

Each entry point has **Inputs → Rules → Workflow → Verify → Output → References**. Stable rule IDs make findings and regression cases easy to cite. Core instructions have a 650-word ceiling; longer detail stays in playbooks that load only when needed.

Rules are scoped to failure modes, not arbitrary bans. Native control semantics matter; custom styles are allowed when they preserve behavior and contrast. Interop is a narrow capability boundary, not a forbidden import. `async` is not synonymous with background execution. A build is not a screenshot, device test, or release approval.

[Architecture and adapters](docs/layering.md) explains portability. [Use cases](docs/use-cases.md) shows task-to-skill selection. [Contributing](CONTRIBUTING.md) defines the evidence and maintenance bar.

## Tools and checks

Repository tooling requires Python 3.10+ and only the standard library. The Swift examples require Swift 6.0+; Apple-only views additionally require an Apple SDK. These requirements apply to the tooling/examples, **not** to the deployment minimum of an app using the skills.

```bash
python3 scripts/validate_skills.py .
python3 scripts/skillctl.py docs --check
python3 -m unittest discover -s tests -v
python3 scripts/scan_apple_repo.py /path/to/apple-app --format json
swift test --package-path examples/SkillExamples
```

The validator checks metadata, budgets, rule IDs, catalog/source consistency, local file links, portability, generated documentation, and selected public-hygiene risks. It accepts a documented scalar frontmatter profile, not arbitrary YAML. Optional `agents/openai.yaml` files are neither required nor interpreted by the core validator.

The scanner is **advisory lexical triage**, not an AST, compiler, accessibility audit, secret scanner replacement, or HIG certification. It ignores comments and strings for Swift code hints, distinguishes informational review prompts from warnings/errors, and never prints matched secret content. By default only error-level findings fail the command. Use `--fail-on warning` or `--fail-on info` deliberately. Skipped files and known blind spots are reported.

The [examples](examples/SkillExamples/README.md) exercise draft ownership, typed routes, and stale-request protection. The [evaluation protocol](docs/evaluation.md) separates mechanical checks from real agent behavior. Passing repository tests does not establish that every model follows the skills or that an app is production-ready.

## Source and maintenance policy

Apple documentation and HIG are authoritative for platform APIs and guidance; installed SDK declarations establish actual compilation availability. This library adds original decision procedures and engineering recommendations. Recheck version-sensitive APIs, beta behavior, privacy rules, and store requirements at use time. Do not turn a review date into a permanent freshness claim.

No Apple documentation is vendored wholesale. Sources are linked and summarized in original playbooks. Apple and SwiftUI are trademarks of Apple Inc.; this is an independent repository, not an Apple endorsement.

## License

The repository owner has not selected a license. This update does not grant a new license to existing or contributed material. Resolve licensing before presenting the project as freely reusable open-source software or distributing third-party contributions under assumed terms.
