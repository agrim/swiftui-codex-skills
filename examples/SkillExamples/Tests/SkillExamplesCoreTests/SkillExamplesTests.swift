import Foundation
import Testing
@testable import SkillExamplesCore

struct RequestStateTests {
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

struct NoteRouteTests {
    @Test func routeRoundTripsStableIdentity() throws {
        let route = NoteRoute.detail(UUID())
        let data = try JSONEncoder().encode(route)
        #expect(try JSONDecoder().decode(NoteRoute.self, from: data) == route)
    }
}
