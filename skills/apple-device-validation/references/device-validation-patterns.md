# Device Validation Patterns

Use this reference when proof depends on runtime behavior rather than static code inspection.

## Failure Patterns

- Visual regressions often survive builds and unit tests.
- Watch screens need their own validation because compact surfaces amplify truncation, mixed geometry, and hierarchy mistakes.
- Shell simulator discovery can fail because the simulator infrastructure is unhealthy, not because the app is broken.
- Physical-device installs have different failure modes from simulator builds.
- Screenshot harnesses and launch arguments can accidentally leak into tracked source if not removed after capture.

## Default Checks

- What exact behavior needs proof: compile, launch, render, tap, drag, sensor, sync, install, or persistence?
- Which device size is most likely to fail?
- Is the failure app code, simulator infrastructure, provisioning, signing, or device state?
- Are screenshots saved outside tracked source unless explicitly intended?
- Was temporary validation code removed before the final build?
