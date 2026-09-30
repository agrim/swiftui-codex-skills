# Deep links, restoration, and presentation identity

Treat external navigation as a pipeline: bounded parsing, typed route, current-account authorization, object resolution, scene selection, and presentation. Parsing a UUID does not prove its object exists or belongs to the current user. Never create a replacement object merely to make a stale link succeed.

Keep navigation state scoped to the right scene or tab. Restoring a path may require waiting for store/account readiness, but should not retry forever or duplicate pushes. Validate persisted routes against the current schema and gracefully remove unsupported or deleted destinations. Preserve the remaining valid path only when that behavior is coherent.

Use value-based navigation and destination registration where the intended stack can see it. Do not hide essential destination registration inside a lazy row whose lifetime is unrelated to the route. For presentation, use an item carrying stable identity when the presented content is selected data. Separate dismissal from commit: dismissing a draft is not proof of a save.

## Failure probes

Open the same link twice, a malformed link, a deleted item, an unauthorized item, and a valid route before login/store initialization. Reopen with an old route version, switch accounts mid-resolution, and open a second window. Assert one intended destination and no hidden mutation.

A sidebar-detail workflow should retain stable selection when space permits and adapt coherently on compact windows. Do not force every platform into a phone push stack. Preserve keyboard commands, back behavior, sheet escape, and deep-link intent through adaptation.

Interactive dismissal, explicit Cancel, and programmatic replacement can differ. Test each applicable path and its focus/task cleanup. Do not use a global sheet boolean plus unrelated selected data when inconsistent combinations can show the wrong item.

## Official sources

- [Understanding the navigation stack](https://developer.apple.com/documentation/swiftui/understanding-the-navigation-stack).
- [Migrating to new navigation types](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types).
- [HIG: Windows](https://developer.apple.com/design/human-interface-guidelines/windows).
