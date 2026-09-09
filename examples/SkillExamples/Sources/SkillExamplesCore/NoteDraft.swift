import Foundation

/// A draft is a value, not a live persistent object. Creating/editing it has no
/// storage side effect. The caller owns the explicit commit and its failures.
public struct NoteDraft: Equatable, Sendable {
    public var title: String

    public init(title: String = "") {
        self.title = title
    }

    public func validated() throws -> NoteDraft {
        let trimmed = title.trimmingCharacters(in: .whitespacesAndNewlines)
        guard !trimmed.isEmpty else { throw ValidationError.emptyTitle }
        return NoteDraft(title: trimmed)
    }

    public enum ValidationError: Error, Equatable, Sendable {
        case emptyTitle
    }
}

/// Routes carry stable identifiers, not snapshots of mutable model objects.
public enum NoteRoute: Hashable, Codable, Sendable {
    case detail(UUID)
}
