#if canImport(SwiftUI)
import SwiftUI
import SkillExamplesCore

/// Inject a cancellation-aware service. This view demonstrates request lifetime
/// and stale-result safety, not a complete networking or debounce implementation.
@MainActor
public struct SearchExample: View {
    private let search: @Sendable (String) async throws -> [String]
    @State private var query = ""
    @State private var request = LatestRequestState<[String]>()

    public init(search: @escaping @Sendable (String) async throws -> [String]) {
        self.search = search
    }

    public var body: some View {
        let requestedQuery = query.trimmingCharacters(in: .whitespacesAndNewlines)
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
            guard !Task.isCancelled else { return }
            guard !requestedQuery.isEmpty else {
                request.invalidate()
                return
            }
            let token = request.begin()
            do {
                let results = try await search(requestedQuery)
                try Task.checkCancellation()
                request.succeed(results, for: token)
            } catch is CancellationError {
                request.cancel(for: token)
            } catch {
                if Task.isCancelled {
                    request.cancel(for: token)
                } else {
                    // Do not expose arbitrary service error text or credentials.
                    request.fail("Search could not be completed. Try again.", for: token)
                }
            }
        }
    }
}
#endif
