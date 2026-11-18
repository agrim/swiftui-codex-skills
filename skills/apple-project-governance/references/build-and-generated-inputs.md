# Generated membership and configuration drift

**A fresh checkout loses a generated file.** Reproduce from tracked inputs and pinned generator versions. Compare the generated project with the expected products, then regenerate again without edits. A persistent diff or dependency on an untracked local file identifies the owner to repair. Check automatically included folders for preview or test fixtures that landed in a shipping target.

**Debug imports a framework that Release cannot find.** Compare resolved settings for the same scheme and destination. Trace the missing path to the configuration layer that replaced it. If the target should extend that path, repair the owning layer and rebuild Release from tracked inputs.

If an extension deliberately excludes an app-only dependency, keep its boundary. A misplaced source file or a missing shared interface can cause the same import error. Verify target membership before broadening search paths across products.

A newer compiler can coexist with an older deployment minimum. Check each affected target’s effective language and runtime settings before propagating a compiler or isolation change.
