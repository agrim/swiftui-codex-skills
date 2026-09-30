import Foundation
import Observation

/// The caller owns the task; this model never starts hidden background work.
/// Keep one instance per search surface and invalidate it on an account change.
@MainActor
@Observable
public final class SearchModel {
    public private(set) var request = LatestRequestState<[String]>()
    private let search: @Sendable (String) async throws -> [String]

    public init(search: @escaping @Sendable (String) async throws -> [String]) {
        self.search = search
    }

    public func load(_ query: String) async {
        guard !Task.isCancelled else { return }
        let query = query.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !query.isEmpty else {
            invalidate()
            return
        }
        let token = request.begin()
        do {
            let results = try await search(query)
            try Task.checkCancellation()
            request.succeed(results, for: token)
        } catch is CancellationError {
            request.cancel(for: token)
        } catch {
            if Task.isCancelled {
                request.cancel(for: token)
            } else {
                // Never publish arbitrary service error text or credentials.
                request.fail("Search could not be completed. Try again.", for: token)
            }
        }
    }

    /// Immediately revoke publication authority. The caller must separately
    /// cancel its task to ask a cooperating service to release resources.
    public func invalidate() {
        request.invalidate()
    }
}
