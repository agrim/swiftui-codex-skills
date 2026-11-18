# Which update delayed this scroll?

A places list scrolls smoothly until a download starts. Moving thumbnail decoding to a worker lowers overall CPU usage. The scroll still catches.

In an illustrative trace, the worker finishes before the gesture. During the missed frame, 24 visible rows receive hundreds of short updates while the toolbar’s download percentage changes. That gives you a specific experiment. Have the toolbar observe aggregate progress. Give each row only the item data it displays. Leave thumbnail decoding alone for this comparison.

Repeat the same scroll during a download at the same refresh rate. Compare missed frames and hitch duration across runs. Edit a title, toggle a saved flag and watch the progress indicator. If frames arrive on time because those updates silently stopped, the experiment failed. If the hitch remains with few row updates, follow the remaining wait in that frame.

For a measured row-update problem, trace a gesture in Instruments with the SwiftUI instrument available in the installed toolchain. Select the missed frames, find the view updates in that interval and inspect their changing dependencies. If the main thread is waiting during the missed frame, follow what it is waiting on. If repeated view updates occupy the frame, try narrowing the row inputs. Repeat with identical data, gesture and download progress.
