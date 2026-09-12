import Foundation

/// A deliberately narrow example route. Parsing is not authorization.
/// The caller must load the object and verify access before navigation or mutation.
public enum NoteDeepLink: Equatable, Sendable {
    case note(UUID)

    /// Accepts only HTTPS links of the form https://notes.example/notes/<UUID>.
    /// The example intentionally rejects ports, credentials, query parameters,
    /// fragments, escapes, and non-ASCII input instead of guessing their meaning.
    /// Replace the host and grammar deliberately when integrating into an app.
    public static func parse(_ raw: String) -> Self? {
        guard !raw.isEmpty,
              raw.unicodeScalars.allSatisfy({ (33...126).contains($0.value) }),
              !raw.contains("%"),
              let parts = URLComponents(string: raw),
              parts.scheme?.lowercased() == "https",
              parts.host?.lowercased() == "notes.example",
              parts.user == nil, parts.password == nil, parts.port == nil,
              parts.query == nil, parts.fragment == nil else {
            return nil
        }
        let segments = parts.path.split(separator: "/", omittingEmptySubsequences: false)
        guard segments.count == 3, segments[0].isEmpty, segments[1] == "notes",
              let id = UUID(uuidString: String(segments[2])),
              id.uuidString.lowercased() == segments[2].lowercased() else {
            return nil
        }
        return .note(id)
    }
}
