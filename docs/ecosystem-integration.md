# What community implementations contributed

The catalog borrows questions that survive a change of framework or app architecture. These three public sources helped decide what belongs in the guides. File links pin the excerpts reviewed.

| Source | Observation | Local decision |
| --- | --- | --- |
| [Ice Cubes’ app view](https://github.com/Dimillian/IceCubesApp/blob/98098b9c4b5928f89f338203193c2bf40ab7f38c/IceCubesApp/App/Main/AppView.swift) | Its tab and sidebar presentations can share the selected destination. | When a note editor changes shape, decide which window owns its selection and draft. Try a resize halfway through editing. |
| [AvdLee’s SwiftUI skill](https://github.com/AvdLee/SwiftUI-Agent-Skill/blob/62bd760f005093d1e2e4de5db156e456a5f96400/skills/swiftui-expert-skill/SKILL.md) | The review distinguishes view dependencies and leaves room for different app architectures. | Start with the native control and owner that serve the feature. Narrow a dependency when a measured interaction points to it. |
| [Point-Free’s identified collections](https://github.com/pointfreeco/swift-identified-collections/blob/3abaf5156efa9437192f8608fa94e6e4e7abf36a/README.md) | A row can move while an asynchronous edit is in flight. An old index can then refer to another record. | Carry the record’s identity through Save and apply the result to that record after a reorder. The app can do this with its existing collection. |

The [provenance ledger](ecosystem.md) preserves earlier reviews, their scopes, access limits and receipts. The [v2 research notes](https://github.com/agrim/swiftui-codex-skills/blob/104e1f69140ca14cf9bc3ad9f3c0eb464fb0e7a2/docs/ecosystem-integration.md) explain how those reviews informed the wider catalog. A retired topic in the ledger links to the [migration guide](skill-migration.md). Repository popularity was a discovery aid. The choice to retain guidance rests on the product decision it changes.
