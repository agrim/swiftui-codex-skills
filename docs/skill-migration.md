# Moving from 29 topics to six app-development skills

Version 3 changes what the library offers. A skill earns its own entry when a developer faces a recurring product choice, plausible alternatives lead to different app behavior, and someone can try the result. Knowing how to declare a framework type or run a tool is usually a documentation lookup.

## Where the previous topics went

The six linked IDs remain installable. A row describes the part of a former topic worth carrying into the app. The table also accounts for the four tooling topics retired outright.

| Current skill | Previous topics folded into it | What earns the space |
| --- | --- | --- |
| [`apple-swiftui-native-apps`](../skills/apple-swiftui-native-apps/SKILL.md) | `swift-language`, `swiftui-design-system` | Choose the app’s first useful interaction and the simplest native control and owner that can deliver it. Language conventions and visual catalogs belong with the SDK. |
| [`swiftui-platform-adaptation`](../skills/swiftui-platform-adaptation/SKILL.md) | `swiftui-navigation`, `swiftui-layout`, `swiftui-controls-input`, `swiftui-accessibility`, `swiftui-interop` | Keep selection, drafts, Back and access to actions intact as presentation or input changes. Bridge setup and modifier lists can be looked up independently. |
| [`apple-data-persistence`](../skills/apple-data-persistence/SKILL.md) | `swiftui-state-architecture`, `swift-concurrency`, `swiftdata`, `core-data`, `apple-networking`, `apple-background-execution` | Decide when an edit takes effect, who owns it, what a retry can change and what survives reopening. Storage, networking and task APIs depend on the chosen implementation. |
| [`apple-system-experiences`](../skills/apple-system-experiences/SKILL.md) | `apple-app-intents`, `apple-privacy-system-integrations`, `apple-security` | Choose a glance, an action or a handoff. Decide what the current account can see and change when an old selection returns. The scope is the user journey. |
| [`apple-performance-cleanup`](../skills/apple-performance-cleanup/SKILL.md) | `apple-observability` | Connect measured work to the exact delay a person feels, then check that the visible behavior survives the fix. Instrument setup can be looked up when needed. |
| [`apple-device-validation`](../skills/apple-device-validation/SKILL.md) | `swiftui-testing`, `apple-app-store-readiness` | Try the release promise in the installed candidate, from the state real people will bring. Test syntax and store administration follow their own tools. |
| Retired | `apple-project-governance`, `apple-build-workflows`, `xcode-build-optimization`, `macos-productization` | Project configuration, build tuning, signing and notarization remain separate engineering work. The optional [build helper](build-workflows.md) remains available. |

## Existing installs and automation

- For an existing installation, run `status --diff` from the catalog revision that installed it. Keep any local edits. Stage version 3 in a fresh destination, then switch your host to the guides you want. An old folder left in a host’s discovery path can still be loaded by that host.
- Update pinned names from the table or the `retired` map in `catalog.json`. A null target means the topic was retired outright. Commands given a retired name return a migration message. Each listed replacement has a narrower product purpose.
- Version 3 assigns new decision IDs because the decisions changed scope. Consumers that check old rule IDs or depend on specific v2 cases can use the pinned revision below. The structure of the JSON contract remains at schema version 1.

The complete prior catalog, rule IDs, playbooks and tools are available together at [the final v2 revision](https://github.com/agrim/swiftui-codex-skills/tree/104e1f69140ca14cf9bc3ad9f3c0eb464fb0e7a2).
