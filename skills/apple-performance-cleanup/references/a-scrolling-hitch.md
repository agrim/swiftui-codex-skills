# The CPU graph improved and scrolling still catches

In a sample trace, thumbnail decoding finished on a worker before the gesture. During a roughly 40 ms hitch, 24 visible rows received hundreds of short updates as download progress changed. Moving decoding off the main thread helped a different interval. The hitch remains open.

Select the missed frame in Instruments. If main-thread samples span row updates and the update cause leads back to aggregate progress, let the toolbar observe that progress and each row observe the title and saved flag it displays. Leave decoding alone for this experiment. If the main thread is waiting instead, follow the work it awaits.

Repeat the same scroll on the same build configuration, device, cache state and refresh rate with downloads active. Compare hitch durations and missed deadlines across runs. Edit one title, toggle another row’s flag and watch progress advance. Smoother scrolling caused by the UI no longer refreshing is a regression.

**For a cleanup without a measured slowdown**, pick the smallest transformation that removes duplicate work. Keep a fixture for distinct values such as missing, stale and zero and compare results and side effects before and after. A simpler implementation can be worthwhile on those terms alone.
