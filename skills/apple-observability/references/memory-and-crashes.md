# Memory graphs and crash investigation

## Memory rises after reopening a screen

Compare memory after several identical presentation and dismissal cycles. If it settles at a new level while the screen owner deallocates, inspect cache bounds and transient allocations. If dismissed owners accumulate, follow a retaining path from one instance to its task, observer, timer or delegate. Change the lifetime at that boundary and verify the owner deallocates while callbacks still arrive for a live screen.

A suspended task can hold an owner after promoting a weak capture. Stop the operation, await its teardown and repeat the capture. For a device-pressure claim, reproduce on the affected hardware. Remove object content and filenames from the shared report.

## Crash reports from multiple builds

Match the incident’s binary UUID to the dSYM before attributing an address to a source line. If a near-identical build has different symbols, keep the original incident and mark the frame unresolved. Distinguish app assertions, access violations, watchdogs and memory termination before choosing which workload to reproduce.
