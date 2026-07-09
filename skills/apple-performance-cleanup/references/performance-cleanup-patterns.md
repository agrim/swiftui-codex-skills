# Performance Cleanup Patterns

Use this reference when the user asks to simplify code while preserving behavior, debug fixes, or performance.

## Failure Patterns

- Cleanup drifts into rewrite when the agent does not define the behavior contract first.
- Removing duplication can silently change nil, zero, unavailable, stale, or failed-state semantics.
- Logging and convenience wrappers can add work to hot paths.
- SwiftUI view cleanup can increase invalidation if derived data stays in `body`.
- Compile success does not prove performance-sensitive behavior.

## Default Checks

- What exact behavior must remain unchanged?
- What path is hot, user-visible, or startup-sensitive?
- What tests already cover the behavior?
- What edge cases distinguish nil, zero, missing, stale, denied, failed, and unavailable?
- What measurement or focused test will prove the cleanup?
