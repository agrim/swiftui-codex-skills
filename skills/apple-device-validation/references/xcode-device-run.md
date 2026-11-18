# Capture the right build or diagnose a Release-only exit

Select the workspace and shared scheme. Use `xcodebuild -showdestinations -workspace "$workspace" -scheme "$scheme"` to find compatible destinations, or `-project` for a standalone project. For Simulator, match the OS and device in `xcrun simctl list devices booted`. Set the variables below to the chosen simulator UDID, simulator app bundle, bundle ID and output path.

```sh
xcrun simctl install "$udid" "$built_app"
xcrun simctl launch "$udid" "$bundle_id"
# Navigate to the affected state before taking the screenshot.
xcrun simctl io "$udid" screenshot "$capture_path"
```

Compare captures with the same fixture, appearance and text size. If only this app fails to capture, see whether its UI responds. If a known-good screen on the same simulator also fails, investigate the simulator or capture service.

**On hardware**, discover the destination with `xcrun devicectl list devices`. Xcode’s Devices and Simulators window or `xcrun devicectl device install app --device "$device" "$device_app"` can install the matching signed device build. Verify bundle presence for an install request. For a launch claim, observe the process reach its first usable screen.

**If Release exits**, retain the app data and device crash report. Match the failing image’s UUID against the archive’s dSYM using `dwarfdump --uuid "$dsym"`. Symbolicate the first app-owned frames with that archive. Install the corrected Release build over the failing data and repeat cold launches on the same device.
