# Native SwiftUI app skills

Build the experience someone came to the app for. These six guides cover decisions that belong to the app, such as whether an edit should take effect immediately, what Back should reveal after a resize, and how much of a task someone can finish from a widget.

Start with the guide matching the decision in front of you. If the question is how to declare a Swift type or use a particular API, go straight to the platform documentation.

| When you’re deciding… | Read |
| --- | --- |
| What should the first working version of this feature let someone accomplish? | [Build a complete native SwiftUI feature](skills/apple-swiftui-native-apps/SKILL.md) |
| What should remain selected, editable and reachable as the interface changes? | [Keep a task usable as the interface changes](skills/swiftui-platform-adaptation/SKILL.md) |
| When does an edit become real, and what survives cancellation, failure or sync? | [Save the changes someone meant to keep](skills/apple-data-persistence/SKILL.md) |
| Can someone finish this task from a glance or a shortcut, or do they need the app? | [Extend an app task beyond the open app](skills/apple-system-experiences/SKILL.md) |
| What is making this particular interaction slow? | [Make a slow interaction feel responsive](skills/apple-performance-cleanup/SKILL.md) |
| Does the installed update deliver the experience we promised? | [Decide if a changed experience is ready to ship](skills/apple-device-validation/SKILL.md) |

For example, “Add App Intents” starts one decision too late. If someone routinely files a known note into a known folder, a shortcut can save them a trip. If filing requires comparing notes, open the collection and let them choose. Only the first version needs a move operation that can finish while the app is closed. [Worked example](skills/apple-system-experiences/references/a-saved-action.md)

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

Version 3 consolidates 29 topics into six skills and seven cases. The migration guide accounts for every previous skill and explains how to keep a pinned copy or stage the replacements alongside an existing installation. [Catalog migration](docs/skill-migration.md)

## Maintaining the library

A new skill should change a decision that affects someone using the finished app. Keep framework mechanics in platform documentation, examples in local playbooks, and research receipts in the repository. [Contributing](CONTRIBUTING.md) · [Coverage](docs/coverage.md) · [Community research](docs/ecosystem-integration.md)

The repository also contains an optional build helper, a lexical scanner and a Swift example package. The verification matrix distinguishes repository checks, Apple builds and historical agent evaluations. [Build helper](docs/build-workflows.md) · [Examples](examples/SkillExamples/README.md) · [Verification](docs/verification-matrix.md)

## License

The repository owner has not selected a license. Public access does not grant additional distribution terms.
