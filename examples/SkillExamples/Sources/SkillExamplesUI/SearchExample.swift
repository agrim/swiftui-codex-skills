#if canImport(SwiftUI)
import SwiftUI
import SkillExamplesCore

/// Inject a cancellation-aware service. This view demonstrates request lifetime
/// and stale-result safety, not a complete networking or debounce implementation.
@MainActor
public struct SearchExample: View {
    @State private var query = ""
    @State private var model: SearchModel

    public init(search: @escaping @Sendable (String) async throws -> [String]) {
        _model = State(initialValue: SearchModel(search: search))
    }

    public var body: some View {
        let requestedQuery = query.trimmingCharacters(in: .whitespacesAndNewlines)
        let request = model.request
        VStack(alignment: .leading) {
            TextField("Search", text: $query)
                .textFieldStyle(.roundedBorder)
                .submitLabel(.search)
            if request.isLoading {
                ProgressView("Searching")
            } else if let message = request.errorMessage {
                Text(message)
                    .foregroundStyle(.secondary)
            } else if let results = request.value {
                if results.isEmpty {
                    Text("No results")
                } else {
                    // This demo service returns distinct strings. A real domain
                    // should use stable entity identifiers instead of display text.
                    List(results, id: \.self) { result in
                        Text(result)
                    }
                }
            }
        }
        .padding()
        .task(id: requestedQuery) {
            await model.load(requestedQuery)
        }
        .onDisappear {
            model.invalidate()
        }
    }
}
#endif
