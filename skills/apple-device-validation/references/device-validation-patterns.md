# Apple Runtime Proof Playbook

Use this playbook when static inspection or compile success cannot establish the requested Apple-app behavior.

## Proof Matrix

Choose the lowest row that fully supports the claim. Higher rows normally require the relevant lower-row prerequisites, but never report a higher evidence level that was not observed.

| Claim | Minimum sufficient evidence | Insufficient on its own |
| --- | --- | --- |
| Source contract is present | Inspect the owning source, target membership or configuration, and focused source-contract checks. | A screenshot or remembered repository state. |
| Code compiles and links | Successful build for the exact scheme, configuration, platform, and destination class. | Static inspection or another target's build. |
| Focused tests pass | Successful execution of the named test target and relevant test cases on the recorded destination. | Build success, discovered tests, or stale results. |
| App installs | Install action succeeds and the expected bundle is present on the intended simulator or device. | A successful archive or build-for-testing. |
| Installed app icon renders correctly | The exact build is installed and the launcher, Dock, Home Screen, or other requested host surface shows the intended icon and relevant appearance variant at a representative size. | Source artwork, an Icon Composer preview, asset compilation, or bundle inspection alone. |
| App launches | A launch action succeeds on the intended destination and the process remains alive long enough to observe the expected initial state. | Install success. |
| Optimized release-device launch is reliable | The intended signed configuration is installed on the physical release device, survives repeated terminate-and-relaunch cycles, and produces no new crash report. Preserve the existing app container when upgrade state is part of the claim. | A Debug simulator launch, a successful Release build, installation alone, or one launch command without a process-lifetime check. |
| Screen renders correctly | Screenshot or live UI inspection captures the exact state, destination size, orientation, and appearance needed by the claim. | Build, launch, snapshot tests alone, or a different screen state. |
| Interaction works | The tap, drag, keyboard, focus, accessibility, or state transition is exercised and its visible and model effects are observed. | A static screenshot or unit test that does not cross the interaction boundary. |
| A reported interaction hang is removed | Install the intended build on the physical device, reproduce the same cold or warm data state, exercise the exact action under on-device Hang Detection or Instruments, and observe no stall at the configured threshold. Exercise the next dependent action separately to show that blocking work was not merely moved. | A green build, a source-level actor change, result tests, simulator UI timeouts, or a settled destination screenshot. |
| Personal AutoFill or system input-session behavior works | Exercise the exact focus, submit or dismissal, and transition sequence on a physical device with the relevant keyboard, My Card or credential state, and content-type hints; capture the immediate destination state. | A simulator with generic data, a screenshot taken only after relaunch, or a test that adds an extra dismissal cycle before the transition. |
| Permission-mediated setup works | Exercise the not-determined screen, system prompt, denial or restriction path, grant path, and the resulting interaction and layout state. | One pre-prompt screenshot, a mocked authorization value, or grant-path unit tests alone. |
| Lifecycle or persistence works | Exercise the relevant background, termination, relaunch, interruption, or restoration sequence and inspect the resulting state. | Observing state before the lifecycle transition. |
| A creation flow is truly draft-only until confirmation | Record the persisted collection before opening the editor; enter a recognizable draft, then test Cancel and force-termination followed by relaunch and confirm no record appeared. Separately create a uniquely named record, terminate, relaunch, reopen it, and verify every claimed saved choice. | A source assertion that insert/save moved, an in-memory model test, Cancel without relaunch, or successful creation without the termination path. |
| Persistence bootstrap is usable | Observe store readiness, perform the first meaningful mutation, inspect the resulting state, and relaunch when durability is claimed. | A welcome screen, a process that remains alive before a write, or an in-memory fallback. |
| Hardware-dependent behavior works | Observe the behavior on compatible physical hardware with the required permission, sensor, camera, microphone, protected store, or accessory state. | Simulator behavior or mocked data. |
| Phone/watch behavior agrees | Observe the initiating action, transport or delivery evidence when available, and resulting state on both paired surfaces. | Only the phone or only the watch. |
| App Intent or system-routed action works | Prove compiled metadata, entity or parameter resolution, command execution and persistence, and the requested system-routed invocation at the appropriate destination. | Metadata extraction, a direct unit call, or an in-app invocation alone. |
| Widget or extension renders current data | Prove the extension is embedded and registered, the intended shared state reaches its provider, and the host renders the exact entry and family under inspection. | Main-app rendering, an extension build, provider unit tests, or source inspection alone. |
| Widget or projection stays truthful over time | Observe at least one relevant refresh, countdown, stale, unavailable, or recovery transition using controlled timestamps or live elapsed time. | A single fresh screenshot or one provider callback. |

## Destination Selection

- Use the narrowest destination that can prove the claim.
- For layout and truncation, start with the smallest supported relevant size and add a representative larger size.
- For platform-adaptive UI, include each affected device family or size class rather than treating one simulator as universal.
- For watch, select a valid paired phone/watch destination and record which surface initiates and which receives the state change.
- For hardware, use a physical destination only after confirming it is visible, trusted or paired as needed, compatible with the target, and in the expected lock and permission state.
- Resolve destinations live. Do not embed local device identifiers, names, or paths in source, fixtures, documentation, or reports intended for publication.
- Treat simulator and physical-device lanes separately when they use different storage, cloud, account, protected-data, or service implementations. State which lane ran instead of presenting one as a substitute for the other.

## Phone Delivery Contract

Interpret delivery language conservatively:

- **`Build`** means compile or link only unless runtime proof is part of the same request.
- **`Install` or `send to my phone`** means build as needed, install, and verify bundle presence. Do not launch.
- **`Install and launch`** authorizes both actions but not uninstall or data reset.
- **`Fresh install` or an explicit reset request** authorizes uninstalling the app first, verifying the prior bundle is absent when relevant, reinstalling, and verifying the new bundle is present.

When shell tooling is used, query the connected device's installed apps with `devicectl device info apps --bundle-id <bundle-id>` or the current equivalent. An app uninstall resets that app's container; it does not by itself prove that HealthKit, CloudKit, Keychain, or other system-managed data was erased.

## Screenshot Protocol

Before capture, record or control:

- destination model or size and OS runtime;
- orientation, window size, and display scale when relevant;
- app route and exact interaction state;
- light or dark appearance, contrast settings, Dynamic Type, and locale when material;
- status-bar or time policy when stable comparison requires it;
- deterministic seed, fixture, launch argument, account, or permission state;
- output path outside tracked source unless screenshots are intentional repository assets.

Capture the screen after layout and state have settled. A screenshot that omits the state setup cannot prove which branch rendered. Remove capture-only arguments, fixtures, overlays, or source hooks and run the final narrow build again if source was touched.

When the defect is itself a brief post-action state—such as a button resizing, a spinner flashing, or input chrome lingering—inspect or capture inside that transition window as well as at the settled destination. A clean destination screenshot does not disprove a transient regression.

For permission-driven UI, capture or inspect the meaningful sequence rather than one endpoint: not determined, request in flight or system prompt, denied or restricted recovery, and granted. Compare the owning row or surface before and after transition, and inspect runtime diagnostics when geometry, focus, or container identity has previously regressed.

## Watch And Cross-Device Protocol

1. Confirm the watch target and companion app build for their actual destinations.
2. Confirm the simulator pair or physical pairing is healthy before debugging transport code.
3. Establish which surface owns the state and which surface projects it.
4. Exercise the transition from the initiating surface.
5. Observe labels, enabled state, timers or other side effects, and persistence on both surfaces.
6. Exercise interruption or relaunch when the feature promises continuity.
7. Keep phone and watch UI expectations separate; shared state does not imply identical controls or layout.

If target membership, entitlements, application groups, bundle relationships, or schemes are wrong, pair with `apple-project-governance`. If connectivity or protected-data semantics are wrong, pair with `apple-privacy-system-integrations`.

## Widget And Extension Projection Protocol

Treat a widget, Live Activity, extension, or similar host-rendered surface as a pipeline rather than a small app screen:

1. Confirm the intended extension target builds, embeds in the containing product, signs appropriately, and registers with the host.
2. Identify the canonical state owner and the exact app-group, file, defaults suite, database, activity state, or other boundary used to project it.
3. Seed or produce a deterministic source state and verify the provider receives the expected value, timestamp, and availability status.
4. Exercise placeholder, snapshot, and timeline or update paths that the host actually uses; do not infer one from another.
5. Render the exact family, size, appearance, privacy or redaction state, and host surface in scope.
6. Advance through the relevant refresh, countdown, stale, unavailable, and recovery boundaries. Keep valid retained state distinct from genuinely expired or absent state.
7. Verify accessibility output and any bystander-sensitive fields when the surface exists outside the primary app.
8. Repeat the final projection check after reinstall, source changes, shared-container changes, or timeline-policy changes that could invalidate earlier evidence.

Provider tests can prove formatting and entry logic. Registration queries can prove the system sees an extension. Shared-store inspection can prove data crossed the process boundary. Only host rendering and elapsed-state observation prove the corresponding runtime claims.

For App Intents and system-routed commands, use the analogous chain: compiled metadata → entity and parameter resolution → typed command execution and canonical persistence → system-routed invocation and result disclosure. Verify each link separately; real Siri or provider routing can remain a physical-device gate even when metadata and command semantics are fully tested.

## Interaction Hang Protocol

When the system reports a short app hang during a tap or transition:

1. Establish ownership before editing. Compare the badge or diagnostic with system Hang Detection, search the product source for matching overlay copy, and record the configured threshold.
2. Record the exact build, destination, OS, data state, permissions, and action sequence. Keep cold first-run and warm-store runs separate.
3. Inspect the action and the work it invokes before the next visual state. Synchronous persistence, file I/O, broad fetches, service waits, and main-actor computation are higher-confidence suspects than the destination that happens to appear afterward.
   For modal forms, inspect first-frame composition separately from text input. Redundant persistence observers, `onAppear` state rewrites, and forced focus can combine sheet construction, another render, keyboard or AutoFill startup, and input-session work in one run-loop interval even when each piece looks small alone.
4. Preserve the matching binary and dSYM, and capture the action with the Hangs instrument or another trace that exposes the main-thread stack. A hang log may arrive later; report its absence instead of treating it as proof that no hang occurred.
5. After the correction, repeat the exact action and independently exercise the next action that could inherit deferred work. Validate both behavior and responsiveness.
   If automatic focus was removed, tap the field separately under the same detector; a quiet sheet presentation is not proof that keyboard work was eliminated rather than relocated.
6. Keep claims narrow. A structural change can prove that work left a handler; only runtime evidence under the relevant threshold proves the hardware-observed hang is gone.

Apple documents on-device Hang Detection and main-thread responsiveness in [Improving app responsiveness](https://developer.apple.com/documentation/xcode/improving-app-responsiveness).

## Failure Classification Matrix

| Symptom | Evidence to collect | Likely class | Correct next action | Verification |
| --- | --- | --- | --- | --- |
| `CoreSimulatorService`, `simdiskimaged`, runtime discovery, or boot fails before app launch. | Destination listing, runtime availability, service error, and a minimal simulator operation independent of the app. | Simulator infrastructure. | Repair or restart the relevant simulator service or choose a healthy runtime; do not edit app source. | Repeat the independent simulator operation, then the original narrow command. |
| Build fails before installation. | First compiler or linker error, exact scheme, destination, and target membership. | App source or project configuration. | Fix source only for a source diagnostic; route scheme, identity, target, or generated-project ownership to `apple-project-governance`. | Re-run the exact failed build. |
| Device is not visible or usable. | Live device list, trust or pairing state, lock state, platform compatibility, and connection status. | Device environment. | Restore visibility, trust, pairing, unlock, or compatibility before rebuilding. | Re-list the destination and run a minimal device query. |
| Installation fails after a successful build. | Install-service error, bundle identity, signing and provisioning output, device OS compatibility, and existing app state. | Installation, signing, provisioning, or device state. | Classify the specific error; route configuration ownership appropriately. Do not rewrite unrelated UI code. | Repeat install and verify bundle presence. |
| Launch fails or the process exits. | Launch result, crash report or console logs, process lifetime, metadata and concurrency diagnostics, and initial route or persistence-store output. | Runtime app failure or launch environment. | Diagnose the first app-owned failure; distinguish missing permissions or fixtures from a crash. | Relaunch the same build into the same controlled state. |
| Screenshot or UI inspection times out. | Whether the app launched, UI responsiveness, simulator service state, capture-tool output, and destination load. | Capture infrastructure, hung app, or unsettled state. | Prove which layer is unresponsive before changing code; retry with a stable known state only after classification. | Capture a simple independent screen, then the target state. |
| Watch state does not arrive. | Pair health, both process states, initiating mutation, transport logs, delivery timing, and receiver persistence. | Pairing infrastructure, connectivity, or app state projection. | Repair pairing first if unhealthy; otherwise trace sender, transport, receiver, and projection in order. | Repeat the transition and observe both surfaces. |
| Widget shows unavailable or stale data while the app is current. | Extension registration, shared-container identity, source and entry timestamps, provider path, refresh policy, retained-state cutoff, host logs, and rendered family. | Project wiring, data handoff, timeline policy, stale-state semantics, or host refresh behavior. | Trace source state through the shared store and provider before changing the view; correct the first broken boundary and preserve distinct missing, stale, and failed states. | Produce a fresh entry, render it, then cross the relevant refresh or expiry boundary and observe the intended transition. |
| Visual hierarchy, truncation, or glass is wrong despite a green build. | Exact screenshot state, sizes, appearances, modifier and control ownership, and comparison target. | UI semantics or rendering. | Pair with `apple-swiftui-native-apps` for the correction. | Re-capture the same deterministic states after the focused fix. |

## Release-Only Launch Crash Protocol

When a physical optimized build exits at launch while a simulator or Debug build works:

1. Reproduce with the exact signed configuration and destination without uninstalling first. Existing-container compatibility may be part of the failure.
2. Pull the fresh system crash report and record its exception, termination timing, thread, image UUID, and first app-owned frame. Do not infer the cause from the most recent visible feature.
3. Match the crash image UUID to the exact local app binary and dSYM. Symbolication from another build is not evidence.
4. Symbolicate the app-owned frames. If the frame is compiler-generated metadata or an opaque body accessor, inspect the optimized binary's symbols and disassembly to map the failure to its generated type or stored-property sequence.
5. Make the smallest correction at that owning boundary. Keep runtime-only reference resources in an explicitly owned, actor-confined lifecycle instead of turning each one into independent rendering state.
6. Rebuild the same signed configuration, install it over the existing app, and verify bundle identity.
7. Perform multiple terminate-and-relaunch cycles, check that the process remains alive after each, and confirm that the device created no new crash report.
8. Run focused simulator or unit regressions as supporting evidence. Report them separately because they do not replace the signed physical-device gate.

## Completion Report

Report validation as an evidence ledger:

- **Claim:** the behavior requested.
- **Destination:** platform, OS runtime, device class or size, and pairing state when relevant.
- **Action:** exact command or tool operation.
- **Evidence:** test result, bundle-presence query, launch observation, screenshot path, interaction outcome, logs, or paired-surface state.
- **Classification:** app, project configuration, infrastructure, device state, or still unknown.
- **Unverified:** every stronger claim not directly observed.

Do not collapse `built`, `installed`, `launched`, `rendered`, `interacted`, and `hardware-verified` into a generic statement that the app works.
