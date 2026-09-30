import Foundation

/// A value-owned state machine. Its owner must serialize mutation, for example
/// on MainActor. Tokens reject obsolete success, failure, AND cancellation.
/// This is not a durable job queue or an exactly-once side-effect mechanism.
public struct LatestRequestState<Value: Sendable>: Sendable {
    public struct Token: Hashable, Sendable {
        fileprivate let id: UUID
    }

    public private(set) var value: Value?
    public private(set) var errorMessage: String?
    public private(set) var isLoading = false
    private var current: Token?

    public init() {}

    /// Clear previous results so callers do not accidentally present stale data
    /// as the result of the new query. A stale-while-revalidate policy needs its
    /// own explicit freshness model instead of silently changing this behavior.
    @discardableResult
    public mutating func begin() -> Token {
        let token = Token(id: UUID())
        current = token
        value = nil
        errorMessage = nil
        isLoading = true
        return token
    }

    @discardableResult
    public mutating func succeed(_ result: Value, for token: Token) -> Bool {
        guard current == token else { return false }
        value = result
        errorMessage = nil
        finish()
        return true
    }

    @discardableResult
    public mutating func fail(_ message: String, for token: Token) -> Bool {
        guard current == token else { return false }
        errorMessage = message
        finish()
        return true
    }

    @discardableResult
    public mutating func cancel(for token: Token) -> Bool {
        guard current == token else { return false }
        finish()
        return true
    }

    /// Invalidate outstanding work on logout, empty input, or owner reset.
    /// The caller must also cancel resource-consuming work when appropriate.
    public mutating func invalidate() {
        value = nil
        errorMessage = nil
        finish()
    }

    private mutating func finish() {
        current = nil
        isLoading = false
    }
}
