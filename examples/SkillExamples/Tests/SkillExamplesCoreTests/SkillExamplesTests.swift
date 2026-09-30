import Foundation
import Testing
@testable import SkillExamplesCore

struct RequestStateTests {
    @Test func latestSuccessWins() {
        var state = LatestRequestState<[String]>()
        let old = state.begin()
        let latest = state.begin()
        let staleAccepted = state.succeed(["old"], for: old)
        #expect(!staleAccepted)
        #expect(state.isLoading)
        let latestAccepted = state.succeed(["new"], for: latest)
        #expect(latestAccepted)
        #expect(state.value == ["new"])
        #expect(!state.isLoading)
    }

    @Test func staleFailureDoesNotReplaceCurrentResult() {
        var state = LatestRequestState<Int>()
        let old = state.begin()
        let latest = state.begin()
        let latestAccepted = state.succeed(42, for: latest)
        #expect(latestAccepted)
        let staleAccepted = state.fail("obsolete", for: old)
        #expect(!staleAccepted)
        #expect(state.value == 42)
        #expect(state.errorMessage == nil)
    }

    @Test func staleCancellationDoesNotClearNewLoadingState() {
        var state = LatestRequestState<Int>()
        let old = state.begin()
        let latest = state.begin()
        let staleAccepted = state.cancel(for: old)
        #expect(!staleAccepted)
        #expect(state.isLoading)
        let latestAccepted = state.cancel(for: latest)
        #expect(latestAccepted)
        #expect(!state.isLoading)
    }

    @Test func invalidationRejectsPendingCompletion() {
        var state = LatestRequestState<Int>()
        let token = state.begin()
        state.invalidate()
        let completionAccepted = state.succeed(42, for: token)
        #expect(!completionAccepted)
        #expect(state.value == nil)
        #expect(!state.isLoading)
    }

    @Test func terminalTokenCannotBeReused() {
        var state = LatestRequestState<Int>()
        let token = state.begin()
        let failureAccepted = state.fail("failed", for: token)
        #expect(failureAccepted)
        let completionAccepted = state.succeed(42, for: token)
        #expect(!completionAccepted)
        #expect(state.errorMessage == "failed")
    }

    @Test func newRequestClearsPreviousDataAndError() {
        var state = LatestRequestState<Int>()
        let first = state.begin()
        state.succeed(1, for: first)
        let second = state.begin()
        #expect(state.value == nil)
        state.fail("failure", for: second)
        state.begin()
        #expect(state.errorMessage == nil)
        #expect(state.isLoading)
    }

    @Test func tokensFromDifferentOwnersAreRejected() {
        var first = LatestRequestState<Int>()
        var second = LatestRequestState<Int>()
        let token = first.begin()
        second.begin()
        let wrongOwnerAccepted = second.succeed(1, for: token)
        #expect(!wrongOwnerAccepted)
        #expect(second.isLoading)
    }
}

struct DraftAndRouteTests {
    @Test func editingDraftDoesNotMutateOriginal() {
        let original = NoteDraft(title: "Original")
        var draft = original
        draft.title = "Edited"
        #expect(original.title == "Original")
        #expect(draft.title == "Edited")
    }

    @Test(arguments: ["", " ", "\n\t"])
    func blankDraftIsRejected(_ title: String) {
        #expect(throws: NoteDraft.ValidationError.emptyTitle) {
            try NoteDraft(title: title).validated()
        }
    }

    @Test func validationReturnsTrimmedValueWithoutMutatingInput() throws {
        let draft = NoteDraft(title: "  Useful title\n")
        #expect(try draft.validated().title == "Useful title")
        #expect(draft.title == "  Useful title\n")
    }

    @Test func routeRoundTripsStableIdentity() throws {
        let route = NoteRoute.detail(UUID())
        let data = try JSONEncoder().encode(route)
        #expect(try JSONDecoder().decode(NoteRoute.self, from: data) == route)
    }
}
