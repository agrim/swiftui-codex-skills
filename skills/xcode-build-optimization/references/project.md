# Is a build dependency wrong?

If a generator repeats on unchanged builds, inspect its trigger and declared dependencies. A template-driven generator depends on both the data and template. After correcting its inputs and outputs, build once to establish the new state and measure a second identical build. If it still runs, inspect the phase’s dependency-analysis setting. If the phase is already skipped, follow the task that actually delays completion.

Prove that skipping work is sound. Edit only the template and confirm that the consumer observes the changed bytes. In a disposable build directory, remove the generated product and verify that the next build recreates it. A stamp can yield excellent no-change timings while silently leaving a stale or missing product.

When sibling targets rebuild apparently identical modules, compare their resolved inputs. A platform or conditional-definition difference can justify separate variants. Align settings only if both products still satisfy their own requirements.
