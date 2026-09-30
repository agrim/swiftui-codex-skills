import Foundation
import Testing
@testable import SkillExamplesCore

struct NoteDeepLinkTests {
    private let idText = "550e8400-e29b-41d4-a716-446655440000"

    @Test func acceptsCanonicalLink() throws {
        let id = try #require(UUID(uuidString: idText))
        #expect(NoteDeepLink.parse("https://notes.example/notes/\(idText)") == .note(id))
    }

    @Test func schemeHostAndUUIDCaseDoNotChangeIdentity() throws {
        let id = try #require(UUID(uuidString: idText))
        #expect(NoteDeepLink.parse("HTTPS://NOTES.EXAMPLE/notes/\(idText.uppercased())") == .note(id))
    }

    @Test(arguments: [
        "http://notes.example/notes/", "file://notes.example/notes/",
        "https://notes.example.evil/notes/", "https://evil.notes.example/notes/",
        "https://notes.example@evil.example/notes/", "https://person@notes.example/notes/",
        "https://notes.example:443/notes/", "https://notes.example:/notes/",
        "https://notes.example./notes/", "https://notes.example/Notes/",
        "https://notes.example/notes//", "https://notes.example/a/../notes/",
        "//notes.example/notes/", " https://notes.example/notes/",
        "https://notes.example/notes/%35"
    ]) func rejectsUntrustedOriginAndNoncanonicalPath(prefix: String) {
        #expect(NoteDeepLink.parse(prefix + idText) == nil)
    }

    @Test(arguments: ["/", "?", "?delete=true", "?id=one&id=two", "#", "#edit", "\n", " "])
    func rejectsExtraRouteMeaning(suffix: String) {
        #expect(NoteDeepLink.parse("https://notes.example/notes/\(idText)" + suffix) == nil)
    }

    @Test(arguments: ["", "not-an-id", "550e8400e29b41d4a716446655440000", "../settings", "%35%35%30", "é"])
    func rejectsInvalidIDs(value: String) {
        #expect(NoteDeepLink.parse("https://notes.example/notes/" + value) == nil)
    }

    @Test func malformedAndRelativeInputsAreRejected() {
        #expect(NoteDeepLink.parse("") == nil)
        #expect(NoteDeepLink.parse("/notes/\(idText)") == nil)
        #expect(NoteDeepLink.parse("https://[not-a-host/notes/\(idText)") == nil)
    }
}
