# Prove which build and screen you observed

Select the workspace and shared scheme in Xcode. From the shell, use `xcodebuild -showdestinations -workspace "$workspace" -scheme "$scheme"` (use `-project` for a standalone project). For a simulator, resolve the intended UDID with `xcrun simctl list devices booted`. With the matching app already built, a reproducible capture can be as short as:

```sh
xcrun simctl install "$udid" "$built_app"
xcrun simctl launch "$udid" "$bundle_id"
# Navigate to the affected state before capturing it.
xcrun simctl io "$udid" screenshot "$capture_path"
```

Set the placeholders to the chosen simulator, app bundle, identifier and output file. Use the same fixture, appearance and content size in both captures. For phone delivery, find the physical device with `xcrun devicectl list devices` and use Xcode Devices and Simulators or `devicectl device install app` with that destination. An install request can finish at confirming bundle presence. For a launch claim, observe the process and its first usable screen.

**When capture hangs**, try another screen on the same simulator. If the other screen captures, inspect the app’s responsiveness. If neither captures, inspect the simulator’s state before changing SwiftUI code.

**When only the installed Release build exits**, preserve the failing container, obtain the device crash report in Xcode, and match the image UUID with the binary and dSYM from the archive. Symbolicate the first app-owned frames. Install the corrected Release build over the same data and repeat cold launches. A working Debug launch exercises a different binary.
