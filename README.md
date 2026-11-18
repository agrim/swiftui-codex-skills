# Apple app development skills

Use SwiftUI, Xcode and Apple’s system services to build, refine and ship a native app. Pick the skill for the work in front of you.

| I want to… | Skill |
| --- | --- |
| Fix an unreadable button or replace hand-built glass with a native toolbar | [Build a feature that feels at home in SwiftUI](skills/apple-swiftui-native-apps/SKILL.md) |
| Keep an edit through an iPad resize or a workout in sync on Apple Watch | [Keep a task usable as the interface changes](skills/swiftui-platform-adaptation/SKILL.md) |
| Make Save and Cancel reliable in a SwiftData or Core Data editor | [Save the changes someone meant to keep](skills/apple-data-persistence/SKILL.md) |
| Bring a useful app action to Shortcuts or current information to a widget | [Extend an app task beyond the open app](skills/apple-system-experiences/SKILL.md) |
| Add Health sharing with an honest permission and fallback experience | [Add an Apple integration people can trust](skills/apple-privacy-system-integrations/SKILL.md) |
| Wire the app and its extensions to the right resources and signed capabilities | [Wire an Apple capability through the right Xcode targets](skills/apple-project-governance/SKILL.md) |
| Find the cause of a hitch, slow tap or growing memory footprint in Instruments | [Make a slow interaction feel responsive](skills/apple-performance-cleanup/SKILL.md) |
| Capture the actual screen or reproduce a failure on a paired or physical device | [Verify the experience on Simulator and device](skills/apple-device-validation/SKILL.md) |
| Deliver a signed Mac app that opens and updates after download | [Ship a Mac app people can install and update](skills/macos-productization/SKILL.md) |
| Match the App Store listing and review instructions to the TestFlight build | [Prepare an App Store build a reviewer can actually use](skills/apple-app-store-readiness/SKILL.md) |

## Use a skill

Read its Markdown directly, or copy its directory into a host that supports the [Agent Skills format](https://agentskills.io/specification). Each guide contains its design choices, observable checks and links to local worked cases. Load a case when the situation fits.

The optional CLI uses Python 3.10+ and the standard library. Run it from the repository root.

```bash
python3 scripts/skillctl.py list
python3 scripts/skillctl.py route "My saved shortcut moves the wrong note"
python3 scripts/skillctl.py contract apple-system-experiences
python3 scripts/skillctl.py bundle apple-system-experiences --entrypoints-only
python3 scripts/skillctl.py install apple-system-experiences --dest /path/to/existing-directory
python3 scripts/skillctl.py status apple-system-experiences --dest /path/to/existing-directory --diff
```

`contract` returns JSON from the same Markdown. Plain `bundle` includes the worked cases. For a specific case, pass `--reference` with its repository path. Installation preserves existing folders and supports `--dry-run`. [CLI and installation details](docs/layering.md)

## Upgrading from v2

Version 3.1 restores all six skills from the first publication and the App Store readiness skill from the first expansion. It keeps the later guides for editing, platform adaptation and external actions. The migration guide maps the previous IDs and links to the original revisions. [Catalog migration](docs/skill-migration.md)

## Maintaining the library

Ground guidance in the app’s source, a useful Apple tool and a result someone can observe. Keep worked examples in local playbooks and research receipts in the repository. [Contributing](CONTRIBUTING.md) · [Coverage](docs/coverage.md) · [Community research](docs/ecosystem-integration.md)

The repository also contains an optional build helper, a lexical scanner and a Swift example package. The verification matrix distinguishes repository checks, Apple builds and historical agent evaluations. [Build helper](docs/build-workflows.md) · [Examples](examples/SkillExamples/README.md) · [Verification](docs/verification-matrix.md)

## License

The repository owner has not selected a license. Public access does not grant additional distribution terms.
