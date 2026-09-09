# Screen inventory and batch review

Use this engineering workflow for a requested whole-app audit or coordinated review of many screens. A narrow UI fix needs only the affected states. Inventory scope before promising completeness; a screenshot count alone is not coverage.

## Build the inventory

Give each screen and material state a stable semantic ID, independent of file order or list position. Include sheets, menus, focused input, validation failure, loading/empty/error, permission fallback, and companion surfaces where relevant. Start from actual routes and workflows, then reconcile captures against them. Explicitly list omitted or unreachable states and the next capture needed.

For each captured item, record:

| Field | Purpose |
| --- | --- |
| Screen/state ID and title | Stable feedback target, such as `record-editor.invalid-count` |
| Entry path and fixture | Reproduce the state; identify synthetic or staged values |
| Candidate and capture revision | Prevent an old image or annotation from approving new UI |
| Environment | Runtime/device class, window size, appearance/theme, text size, locale, keyboard/focus |
| Artifact and kind | Distinguish native runtime, preview, generated concept, or unavailable capture |
| Review status and finding | Unreviewed, changes requested, accepted for that capture, or blocked |
| Verification | Interaction performed separately from visible-state inspection |

Use relative artifact paths in a private app review manifest; keep personal data, device identifiers, and private screenshots out of a public skill repository. Demonstration data should be sufficient to expose long text, realistic density, and failure states without production records.

## Compare shared surfaces

Group repeated presentations of the same entity and compare equivalent data. Include representative high-risk theme, contrast, large-text, and keyboard combinations; expand coverage when differences or defects warrant it. Do not claim a full combination matrix from a representative sample.

Keep original captures intact. A resized contact sheet helps navigation but does not replace inspecting the source capture. Generated concepts communicate direction; they cannot establish native rendering or interaction. Forced success/error fixtures demonstrate presentation only, not real service, storage, sensor, or permission outcomes.

## Collect feedback once

For batch feedback, keep comments anchored to the screen/state ID and capture revision. Store image marks in normalized coordinates with the original image dimensions so display resizing preserves their location. Separate app-wide direction from per-screen findings. Save drafts durably, verify reopening them, and export or submit one complete review batch with its manifest revision.

Do not transfer an accepted status to a replacement capture automatically. Retain prior comments as history, mark their capture superseded, and require review of the changed evidence. Duplicate images may illustrate two paths, but must not inflate unique-state coverage.

## Close the loop

Turn accepted feedback into concrete changes and the smallest relevant regression probes. Recapture affected states from the resulting candidate, inspect them, and report resolved, remaining, and blocked findings by stable ID. For a keyboard-obscured button, operate it with the keyboard actually present; a screenshot alone does not prove reachability.

Distinguish implementation complete, captured, reviewed, interaction verified, and user accepted. A blank comment is not approval. If review software was built, test its save/reload/export behavior separately from the app being reviewed.
