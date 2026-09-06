import Foundation
import Testing
@testable import SkillExamplesCore

private enum ServiceFailure: Error { case privateDiagnostic }

/// Deliberately ignores task cancellation so publication guards are exercised.
/// Registration handshakes, not sleeps, establish the ordering under test.
private actor ControlledSearch {
    private var pending: [String: CheckedContinuation<[String], any Error>] = [:]
    private var registered: Set<String> = []
    private var waiters: [String: [CheckedContinuation<Void, Never>]] = [:]

    func search(_ query: String) async throws -> [String] {
        try await withCheckedThrowingContinuation { continuation in
            precondition(pending[query] == nil, "Test queries must be unique while pending")
            pending[query] = continuation
            registered.insert(query)
            for waiter in waiters.removeValue(forKey: query) ?? [] { waiter.resume() }
        }
    }

    func waitUntilRegistered(_ query: String) async {
        if registered.contains(query) { return }
        await withCheckedContinuation { waiters[query, default: []].append($0) }
    }

    func finish(_ query: String, with result: Result<[String], any Error>) -> Bool {
        guard let continuation = pending.removeValue(forKey: query) else { return false }
        continuation.resume(with: result)
        return true
    }
}

@MainActor
@Suite(.timeLimit(.minutes(1)))
struct SearchIntegrationTests {
    @Test func outOfOrderSuccessKeepsLatestResult() async {
        let service = ControlledSearch()
        let model = SearchModel { try await service.search($0) }
        let old = Task { await model.load("old") }
        await service.waitUntilRegistered("old")
        let latest = Task { await model.load("latest") }
        await service.waitUntilRegistered("latest")
        #expect(await service.finish("latest", with: .success(["new result"])))
        await latest.value
        #expect(await service.finish("old", with: .success(["obsolete result"])))
        await old.value
        #expect(model.request.value == ["new result"])
        #expect(!model.request.isLoading)
    }

    @Test func staleFailureCannotClearCurrentLoading() async {
        let service = ControlledSearch()
        let model = SearchModel { try await service.search($0) }
        let old = Task { await model.load("old") }
        await service.waitUntilRegistered("old")
        let latest = Task { await model.load("latest") }
        await service.waitUntilRegistered("latest")
        #expect(await service.finish("old", with: .failure(ServiceFailure.privateDiagnostic)))
        await old.value
        #expect(model.request.isLoading)
        #expect(model.request.errorMessage == nil)
        #expect(await service.finish("latest", with: .success(["new result"])))
        await latest.value
        #expect(model.request.value == ["new result"])
    }

    @Test func canceledOldTaskCannotCancelNewRequest() async {
        let service = ControlledSearch()
        let model = SearchModel { try await service.search($0) }
        let old = Task { await model.load("old") }
        await service.waitUntilRegistered("old")
        let latest = Task { await model.load("latest") }
        await service.waitUntilRegistered("latest")
        old.cancel()
        #expect(await service.finish("old", with: .success(["obsolete result"])))
        await old.value
        #expect(model.request.isLoading)
        #expect(model.request.value == nil)
        #expect(await service.finish("latest", with: .success(["new result"])))
        await latest.value
        #expect(model.request.value == ["new result"])
    }

    @Test(arguments: [false, true])
    func invalidationRejectsLateTerminalPaths(fails: Bool) async {
        let service = ControlledSearch()
        let model = SearchModel { try await service.search($0) }
        let task = Task { await model.load("account-a") }
        await service.waitUntilRegistered("account-a")
        model.invalidate()
        #expect(!model.request.isLoading)
        let result: Result<[String], any Error> = fails
            ? .failure(ServiceFailure.privateDiagnostic) : .success(["account-a data"])
        #expect(await service.finish("account-a", with: result))
        await task.value
        #expect(model.request.value == nil)
        #expect(model.request.errorMessage == nil)
    }

    @Test func currentCancellationRemainsQuietWhenServiceThrowsOtherError() async {
        let service = ControlledSearch()
        let model = SearchModel { try await service.search($0) }
        let task = Task { await model.load("query") }
        await service.waitUntilRegistered("query")
        task.cancel()
        #expect(await service.finish("query", with: .failure(ServiceFailure.privateDiagnostic)))
        await task.value
        #expect(model.request.errorMessage == nil)
        #expect(model.request.value == nil)
        #expect(!model.request.isLoading)
    }

    @Test func serviceCancellationIsNotDisplayedAsFailure() async {
        let model = SearchModel { _ in throw CancellationError() }
        await model.load("query")
        #expect(!model.request.isLoading)
        #expect(model.request.errorMessage == nil)
    }

    @Test func serviceErrorUsesSanitizedMessage() async {
        let model = SearchModel { _ in throw ServiceFailure.privateDiagnostic }
        await model.load("query")
        #expect(model.request.errorMessage == "Search could not be completed. Try again.")
        #expect(!model.request.isLoading)
    }

    @Test func queryIsTrimmedAndEmptyInputClearsResults() async {
        let model = SearchModel { [$0] }
        await model.load("  query\n")
        #expect(model.request.value == ["query"])
        await model.load(" \t\n")
        #expect(model.request.value == nil)
        #expect(!model.request.isLoading)
    }
}
