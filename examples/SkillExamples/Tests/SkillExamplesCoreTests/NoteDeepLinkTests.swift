import Foundation
import Testing
@testable import SkillExamplesCore

struct NoteDeepLinkTests {
    private let idText = "550e8400-e29b-41d4-a716-446655440000"

    @Test func linksResolveToTheSameNoteAcrossCaseVariations() throws {
        let id = try #require(UUID(uuidString: idText))
        #expect(NoteDeepLink.parse("https://notes.example/notes/\(idText)") == .note(id))
        #expect(NoteDeepLink.parse("HTTPS://NOTES.EXAMPLE/notes/\(idText.uppercased())") == .note(id))
    }

    @Test(arguments: [
        "http://notes.example/notes/", "https://notes.example.evil/notes/",
        "https://person@notes.example/notes/", "https://notes.example:443/notes/",
        "https://notes.example/Notes/", "https://notes.example/a/../notes/",
        "/notes/"
    ]) func rejectsUntrustedOriginAndNoncanonicalPath(prefix: String) {
        #expect(NoteDeepLink.parse(prefix + idText) == nil)
    }

    @Test(arguments: ["/", "?", "?delete=true", "#edit", "\n"])
    func rejectsExtraRouteMeaning(suffix: String) {
        #expect(NoteDeepLink.parse("https://notes.example/notes/\(idText)" + suffix) == nil)
    }

    @Test(arguments: ["", "not-an-id", "550e8400e29b41d4a716446655440000",
                      "%3550e8400-e29b-41d4-a716-446655440000", "é"])
    func rejectsInvalidIDs(value: String) {
        #expect(NoteDeepLink.parse("https://notes.example/notes/" + value) == nil)
    }
}
