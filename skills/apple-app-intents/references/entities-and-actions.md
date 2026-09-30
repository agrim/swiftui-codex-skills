# Entities, commands, and invocation proof

Separate a lightweight system-facing entity from the live persistence model. Expose only display data needed for selection, and resolve the selected ID against current authorization when performing the action. Suggestions are not permission grants. A formerly valid entity may be deleted, belong to another account, or no longer be available.

A query should resolve the IDs requested, not return arbitrary favorites when resolution fails. Provide bounded suggestions and search behavior with deterministic ordering. Do not leak another account's cached entity names in disambiguation or error output.

An intent adapter validates inputs, obtains the needed services through an explicit composition path, and calls the canonical command. Actor annotations must match that command, not merely silence diagnostics. Cold/background invocation cannot depend on a view's `onAppear` having initialized the store. Confirm a committed outcome before reporting success.

Define authentication and confirmation independently from parameter parsing. A syntactically valid request, shortcut installed by a user, or model-interpreted phrase does not authorize destructive data access. Recheck current platform authentication policies and supported modes; SDK declarations, runtime OS, and the target hosting the intent all matter.

For side effects that can be retried, use domain-level operation identity and reconciliation where the caller provides or the app can durably establish that identity. Do not promise exactly-once invocation from the framework. A cancelled UI does not necessarily undo already committed external work.

## Proof ladder

1. Build the intended target and inspect metadata extraction/embedding.
2. Confirm the action is discoverable in the supported system surface.
3. Resolve real entities under the intended account and process state.
4. Invoke and inspect the canonical store, result text, and projected UI.
5. Repeat with a stale ID, cold app, denied access, and interrupted execution.

A compile, screenshot of a shortcut, or mocked `perform` call proves only its own rung. Keep app schemas, assistant exposure, widgets, controls, and shortcuts as related but distinct integration contracts.

## Official sources

- [AppIntent protocol](https://developer.apple.com/documentation/appintents/appintent).
- [AppEntity](https://developer.apple.com/documentation/appintents/appentity).
- [EntityQuery](https://developer.apple.com/documentation/appintents/entityquery).
- [AppIntent authentication policy](https://developer.apple.com/documentation/appintents/appintent/authenticationpolicy).
- [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests).
