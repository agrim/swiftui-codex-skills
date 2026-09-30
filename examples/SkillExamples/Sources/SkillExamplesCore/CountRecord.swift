import Foundation

/// A whole-item count, not a general measurement. Other units need their own
/// validation policy. UI adapters own localized text parsing and formatting.
public struct ItemCount: Equatable, Sendable {
    public let value: Int

    public init(_ value: Int) throws {
        guard value >= 0 else { throw ValidationError.negativeCount }
        self.value = value
    }

    public enum ValidationError: Error, Equatable, Sendable {
        case negativeCount
    }
}

public enum CountObservation: Equatable, Sendable {
    case unknown
    case estimated(ItemCount, source: String)
}

/// Planning and observing do not produce a confirmed result or export.
public struct CountDraft: Equatable, Sendable {
    public let id: UUID
    public var target: ItemCount?
    public var observation: CountObservation

    public init(target: ItemCount? = nil) {
        id = UUID()
        self.target = target
        observation = .unknown
    }

    public func confirm(_ actual: ItemCount) -> CountRecord {
        CountRecord(id: id, target: target, observation: observation, confirmed: actual)
    }
}

/// An immutable value ready for an explicit store operation. Constructing this
/// value is not a durable save, remote acknowledgement, or sensor validation.
public struct CountRecord: Equatable, Sendable {
    public let id: UUID
    public let target: ItemCount?
    public let observation: CountObservation
    public let confirmed: ItemCount

    fileprivate init(id: UUID, target: ItemCount?, observation: CountObservation, confirmed: ItemCount) {
        self.id = id
        self.target = target
        self.observation = observation
        self.confirmed = confirmed
    }

    public func repeatDraft() -> CountDraft {
        // This product copies the plan, never the prior observation or result.
        CountDraft(target: target)
    }

    public var export: CountExport {
        CountExport(recordID: id, itemCount: confirmed)
    }
}

/// A projection payload, not a receipt. Transport and storage own delivery.
public struct CountExport: Equatable, Sendable {
    public let recordID: UUID
    public let itemCount: ItemCount
}
