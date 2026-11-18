---
name: swiftui-interop
description: "Bridge UIKit or AppKit with SwiftUI representables, hosting, coordinators, and delegates."
---

# Connect SwiftUI screens to UIKit or AppKit

Use a bridge to put a native control in SwiftUI or host SwiftUI inside an existing native screen. If typing jumps or edits reach the wrong record, trace how changes cross that bridge.

## Start here

For a wrapped text editor, reproduce one edit in the app. Identify who owns the text, which object displays it and which callback writes it back.

## How to proceed

1. **Isolate the missing capability.** Wrap only the public API needed to fill the gap on your supported OS versions. <!-- BRIDGE-001 -->
2. **Update the existing native object.** While editing the same record, compare incoming values before assigning them. Rewriting unchanged text can interrupt active typing. <!-- BRIDGE-002 -->
3. **Keep callbacks pointed at the current model.** Refresh bindings when the editor changes records. Distinguish user edits from callbacks caused by your own assignments. <!-- BRIDGE-003 -->
4. **Check interaction in the host.** Apply UI changes on the main actor. Resize or reparent the editor and check its controller parent, proposed size and keyboard and accessibility focus. <!-- BRIDGE-005 -->
5. **Disconnect on removal.** Detach delegates, cancel work the adapter owns and ignore callbacks queued for an earlier editor. <!-- BRIDGE-004 -->

## Check the result

- Exercise the wrapped feature on the oldest supported OS. Unrelated controls still work without the adapter. <!-- BRIDGE-001 -->
- Refresh unrelated state while composing text. Marked text, selection and focus survive. A user edit writes once. A programmatic update adds no write. <!-- BRIDGE-002 BRIDGE-003 BRIDGE-005 -->
- Remove and remount the editor, then deliver an old callback. The previous resources are released and the new model stays unchanged. <!-- BRIDGE-004 -->

## What to report

Report the owner on each side, the interaction tested and the cleanup result.

- [Diagnose hosting, sizing and focus failures](references/interop-patterns.md)
- [Check native view updates and teardown](references/representable-lifecycle.md)
