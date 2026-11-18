# State, identity, and architecture: playbook

## A document editor keeps the wrong title

Trace who owns the title. A read-only header should follow its parent’s current title. An editor with unsaved typing needs a draft and a policy for external changes. Promoting the first input to persistent view state can freeze the header. Overwriting a draft on every refresh can erase typing.

Decide whether a document switch should reuse the session or start another. If the switch ends the session, resolve unsaved work before keying the editor by document ID. Changing that identity also resets focus. When initialization appears expensive, count model constructions while refreshing the same document. A model constructed eagerly before passing it to `StateObject` can be allocated and discarded on every refresh.

Refresh the same document during editing, then switch to another one. Check that typing survives the refresh and Save targets the correct record after the switch. Also replace a parent-owned model deliberately and confirm later callbacks come only from the current instance. For a wrapper migration, run these checks on each supported observation path.

## Windows, restoration and drafts

- **Two windows.** Share account services when their scope is the account. Keep selection and edit drafts in the owning scene. Edit different documents in two windows and close one. Verify the other window retains its route and draft. Mount previews and new scenes with their own required providers.
- **Relaunch.** Resolve a restored route against current records and permissions. Delete the selected record between launches and verify recovery leads to a valid destination.
- **Create, cancel, retry.** Opening a creation editor should leave storage untouched. Keep the draft on a failed save. Confirm twice and check that the domain’s duplication policy holds. Add a coordinator only if existing owners cannot express this lifecycle.
