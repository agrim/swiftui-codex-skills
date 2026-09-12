# API and dependency review

## Decision table

| Symptom | First useful change | Counterexample |
| --- | --- | --- |
| Two `String` IDs can be swapped | Role-bearing ID types or explicit labels | A one-off display label needs no wrapper |
| A preview contacts production | Inject a fixture transport at the composition root | Pure computations need no service protocol |
| Five booleans encode mutually exclusive status | Enum plus associated values | Independent capabilities can remain independent flags |
| A method unexpectedly saves | Separate editing from commit, or name the side effect | An explicitly named command can own persistence |
| Generic code grows to support one use | Prefer the concrete implementation first | A stable multi-client boundary can justify abstraction |

For dependencies, separate *what* work is requested from *where* it executes. An injected closure is not automatically `Sendable`; annotate isolation according to the captured state. Avoid a global service locator that hides mutable dependencies from tests. Introduce a protocol when alternate implementations or module ownership justify it, not to create a mock for every type.

Prefer semantic formatting APIs for user-visible numbers, measurements, dates, and lists. Keep wire formats explicit and locale-independent. Test decimal separators, long currency text, time-zone transitions, and calendar assumptions without turning localized output into a storage key.

## Review contract

Report file and symbol, concrete failure, smallest change, migration impact, and verification. Separate correctness from optional style. A function can legitimately use `try?` when discarding that particular error is the contract; it is inappropriate when it converts a failed save into apparent success. A proven invariant can justify a precondition, but untrusted input cannot establish it.

Public documentation should describe failure, cancellation, mutation, and nontrivial complexity. Prefer scoped availability or compatibility adapters to raising deployment targets. Do not force a new observation system, persistence framework, or unidirectional architecture solely because another repository prefers it.

## Regression probes

Compile an external consumer, decode the oldest supported serialized fixture, and substitute a clock that crosses a date boundary. Confirm a cancelled operation is not reclassified as an error or committed as success. Inspect generated code separately from the template that owns it.

## Official sources

- [Swift API design guidelines](https://www.swift.org/documentation/api-design-guidelines/).
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
- [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization).
