# Deep links, restoration, and presentation identity

Treat external navigation as a pipeline: bounded parsing, typed route, current-account authorization, object resolution, scene selection, and presentation. Parsing a UUID does not prove its object exists or belongs to the current user. Never create a replacement object merely to make a stale link succeed.

Keep navigation state scoped to the right scene or tab. Restoring a path may require waiting for store/account readiness, but should not retry forever or duplicate pushes. Validate persisted routes against the current schema and gracefully remove unsupported or deleted destinations. Preserve the remaining valid path only when that behavior is coherent.

Use value-based navigation and destination registration where the intended stack can see it. Do not hide essential destination registration inside a lazy row whose lifetime is unrelated to the route. For presentation, use an item carrying stable identity when the presented content is selected data. Separate dismissal from commit: dismissing a draft is not proof of a save.

## Back skips an intermediate screen

In a `NavigationStack(path:)`, a link that supplies a destination view directly can show a screen without adding a value to the bound path. Pushing a value while these view destinations are on top removes them before the new destination appears. Inspect the sequence of link initializers when the Back button skips a screen or restoration loses a step. [Understanding the navigation stack](https://developer.apple.com/documentation/swiftui/understanding-the-navigation-stack)

| Action in one stack | Bound path | Visible screen |
| --- | --- | --- |
| Open a folder by value | `[folder]` | Folder |
| Open a guide using a direct destination view | `[folder]` | Guide |
| Follow a value link from the guide to a document | `[folder, document]` | Document |
| Press Back | `[folder]` | Folder |

If Back must return to the guide, represent the guide as a route value too. Repeat the journey, check that Back reveals the guide, and restore the saved path in a fresh scene if restoration is part of the feature. A disposable help screen at the end of a journey can keep its direct link. Check both the actual screen and the bound path when testing mixed links.

## Cancel closes the presenting window

A sheet editor's Cancel button calls a dismissal action captured by the window's root view. SwiftUI applies the action to the environment where it was read. Depending on the host, the sheet can stay open or the window itself can close. Read `@Environment(\.dismiss)` inside the presented editor when that editor owns dismissal. A coordinator that owns sheet selection can clear its selection directly. Keep Save behind a successful commit in either design.

From a pushed detail, open the editor, change a value and cancel. The same window and detail should remain with the original value. Reopen, force Save to fail, and verify the draft is still available for retry. [SwiftUI DismissAction](https://developer.apple.com/documentation/swiftui/dismissaction)

## Failure probes

Open the same link twice, a malformed link, a deleted item, an unauthorized item, and a valid route before login/store initialization. Reopen with an old route version, switch accounts mid-resolution, and open a second window. Assert one intended destination and no hidden mutation.

A sidebar-detail workflow should retain stable selection when space permits and adapt coherently on compact windows. Do not force every platform into a phone push stack. Preserve keyboard commands, back behavior, sheet escape, and deep-link intent through adaptation.

Interactive dismissal, explicit Cancel, and programmatic replacement can differ. Test each applicable path and its focus/task cleanup. Do not use a global sheet boolean plus unrelated selected data when inconsistent combinations can show the wrong item.

## Official sources

- [Understanding the navigation stack](https://developer.apple.com/documentation/swiftui/understanding-the-navigation-stack).
- [Migrating to new navigation types](https://developer.apple.com/documentation/swiftui/migrating-to-new-navigation-types).
- [HIG: Windows](https://developer.apple.com/design/human-interface-guidelines/windows).
