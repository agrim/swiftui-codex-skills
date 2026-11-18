---
name: apple-background-execution
description: "Handle BGTaskScheduler, background transfers, expiration, and relaunch recovery."
---

# Finish or safely resume work after the app leaves the screen

Use this when a refresh never seems to run, a transfer stops halfway, or an upload appears twice after relaunch. Identify whether the job ran, what it saved, and whether retrying is safe.

## Start here

For one report upload, identify the requesting target, its background capabilities, when the result is needed, and what the app records as success.

## How to proceed

1. **Choose how the job will run.** Choose refresh, processing or transfer for the job’s duration and delivery needs. For an upload that must continue through suspension, check background transfer support. <!-- BG-004 -->
2. **Find the last observed step.** Follow the request through submission, eligibility, handler launch and completion. Record when the handler actually starts. <!-- BG-001 -->
3. **Save enough to resume.** Persist the operation ID and last confirmed change. After relaunch, check account access and whether the service accepted earlier work before retrying. <!-- BG-002 -->
4. **Give completion one owner.** Have the same component decide the outcome when expiration, cancellation and a late callback race. <!-- BG-003 -->
5. **Measure the real schedule.** Use unforced device runs for scheduling and energy claims. Label forced launches as handler checks. <!-- BG-005 -->

## Check the result

- Expire a job during commit, then deliver its callback. Completion fires once and the saved checkpoint matches what actually committed. <!-- BG-002 BG-003 -->
- Lose the upload acknowledgement and relaunch. If you cannot tell whether the service accepted it, leave it pending. Revoking access prevents another upload. <!-- BG-002 -->
- Submit a short refresh on-device. Record submission and observed launch separately, including any run where launch was never observed. <!-- BG-001 BG-004 BG-005 -->

## What to report

Name the mechanism, last confirmed step, observed outcome and condition for retry.

- [Recover an interrupted upload or a locked checkpoint](references/lifetimes-and-recovery.md)
