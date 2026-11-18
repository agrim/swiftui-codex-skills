# Choosing a current skill for an older installation

The first publication contained six skills. Its companion notes showed how to trace a SwiftUI control, check the signed target, exercise permissions and verify the installed app. The August expansion added App Store readiness and worked through issues such as keyboard dismissal, watch state and Release-only crashes. Version 3.1 restores those seven IDs alongside three later guides. [Original skills](https://github.com/agrim/swiftui-codex-skills/tree/148ecfbd5d234981d1574c9feae221ad56065952/skills) · [Original layering notes](https://github.com/agrim/swiftui-codex-skills/blob/e0ee5b8f1a0d5796d7ce0f1fe3a1c3397ac20487/docs/layering.md) · [August expansion](https://github.com/agrim/swiftui-codex-skills/tree/b576d663655e22fe7e90fe4eb19eb771dfb08bee/skills)

## Where the v2 topics live

| Installable skill | Other v2 topics it covers | What to look for |
| --- | --- | --- |
| [`apple-swiftui-native-apps`](../skills/apple-swiftui-native-apps/SKILL.md) | `swift-language`, `swiftui-design-system` | Control hierarchy, foreground and material in the real view. |
| [`swiftui-platform-adaptation`](../skills/swiftui-platform-adaptation/SKILL.md) | `swiftui-accessibility`, `swiftui-controls-input`, `swiftui-interop`, `swiftui-layout`, `swiftui-navigation` | Selection, unfinished work, focus and the companion’s current action. |
| [`apple-data-persistence`](../skills/apple-data-persistence/SKILL.md) | `apple-background-execution`, `apple-networking`, `core-data`, `swift-concurrency`, `swiftdata`, `swiftui-state-architecture` | The owner of a durable write, pending sync or competing change. |
| [`apple-system-experiences`](../skills/apple-system-experiences/SKILL.md) | `apple-app-intents` | How a widget, shortcut or Live Activity reaches the right app state. |
| [`apple-performance-cleanup`](../skills/apple-performance-cleanup/SKILL.md) | `apple-observability` | The interval, thread or retained owner behind a visible delay. |
| [`apple-device-validation`](../skills/apple-device-validation/SKILL.md) | `swiftui-testing` | The simulator, physical device and installed build that can prove the claim. |
| [`apple-project-governance`](../skills/apple-project-governance/SKILL.md) | — | The source manifest, built resources and signed identity for a capability. |
| [`apple-privacy-system-integrations`](../skills/apple-privacy-system-integrations/SKILL.md) | `apple-security` | The data that leaves the app, its purpose and behavior when access changes. |
| [`macos-productization`](../skills/macos-productization/SKILL.md) | — | The signature, notarization, installation and update of the delivered Mac artifact. |
| [`apple-app-store-readiness`](../skills/apple-app-store-readiness/SKILL.md) | — | The connection between the archive, processed build, reviewer access and storefront. |

The standalone `apple-build-workflows` and `xcode-build-optimization` guides remain retired. The [build helper](build-workflows.md) can still capture a repeatable build.

## Existing installs and automation

- For an existing installation, run `status --diff` from the catalog revision that installed it. Keep any local edits. Stage version 3 in a fresh destination, then switch your host to the guides you want. An old folder left in a host’s discovery path can still be loaded by that host.
- Update pinned names from the table or the `retired` map in `catalog.json`. A null target means the topic was retired outright. Commands given a retired name return a migration message. Each listed replacement has a narrower product purpose.
- Version 3 assigns new decision IDs because the decisions changed scope. Consumers that check old rule IDs or depend on specific v2 cases can use the pinned revision below. The structure of the JSON contract remains at schema version 1.

The complete prior catalog, rule IDs, playbooks and tools are available together at [the final v2 revision](https://github.com/agrim/swiftui-codex-skills/tree/104e1f69140ca14cf9bc3ad9f3c0eb464fb0e7a2).
