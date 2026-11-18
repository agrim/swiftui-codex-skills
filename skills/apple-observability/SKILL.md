---
name: apple-observability
description: "Diagnose Apple app failures with unified logs, signposts, Instruments, crash symbols and memory graphs."
---

# Diagnose an Apple app failure from a capture

Use this to explain a freeze, crash or growing memory footprint. During a freeze, a busy worker can hide a blocked main thread. Inspect the thread that stopped responding.

## Start here

Identify the build, process, device, action and time of the incident. Reproduce one symptom and identify what data you may collect.

## How to proceed

1. **Choose a capture that can show the cause.** Inspect main-thread work or waits during a freeze. Trace repeated view updates to the input that changed. For memory growth, find what retains dismissed screens. <!-- OBS-003 -->
2. **Limit what gets logged.** Log the operation, phase and error category. Correlate events with a short-lived ID that contains no account or user data. <!-- OBS-001 -->
3. **Match each start to its own end.** Include failures, cancellations and timeouts. Overlapping operations need distinct IDs to measure their durations. <!-- OBS-002 -->
4. **Check the capture before sharing a finding.** Confirm the trace covers the incident. Match a crashed binary’s UUID to its dSYM debug symbols. Keep the original private. <!-- OBS-004 -->
5. **Repeat without temporary instrumentation.** Replay on the final build to detect changes caused by logging or the debugger. <!-- OBS-005 -->

## Check the result

- Cancel one of two overlapping operations. Each has one matching end. The shared report identifies build, tool and capture conditions while protecting private data. <!-- OBS-001 OBS-002 OBS-004 -->
- Reopen and dismiss a screen repeatedly. Trace a surviving instance to its owner. After the fix, repeat without the debugger and compare. <!-- OBS-003 OBS-005 -->

## What to report

Give the symptom, build, observation that supports the diagnosis, result after the change and competing causes still open.

- [Distinguish a busy main thread from a blocked one](references/logging-and-traces.md)
- [Investigate retained screens and crash reports](references/memory-and-crashes.md)
