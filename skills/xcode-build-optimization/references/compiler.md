# Is the compiler hotspot delaying completion?

Locate the expensive compile on the dependency timeline. Use temporary diagnostics supported by the selected compiler to narrow it, then measure a normal build with those diagnostics removed.

For a slow SwiftUI result builder, try isolating the expensive expression behind a real view or an explicit type. Recheck view identity, environment propagation and accessibility. For a proposed `final` or access change, inspect subclasses, external callers and Objective-C dispatch before trading away behavior.

Keep the change only for its measured effect or a separately justified correctness improvement. A shorter warning list can coexist with unchanged developer wait time.
