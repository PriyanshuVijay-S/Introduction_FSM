"""This module contains the rounds definitions for valory_abci."""
import typing as t
from enum import Enum

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AppState,
    BaseSynchronizedData,
    CollectDifferentUntilThresholdRound,
    DegenerateRound,
)

from packages.valory.skills.valory_abci.payloads import (
    ChanceToFlipCoinPayload,
    DeclareWinnerOrLoserPayload,
    RandomTaskPayload,
    RegistrationPayload,
    ResetAndPausePayload,
    SelectKeeperPayload,
)


class Event(Enum):
    """Event enum for state transitions."""

    DONE = "done"
    NONE = "none"
    NO_MAJORITY = "no_majority"
    RESET_TIMEOUT = "reset_timeout"
    ROUND_TIMEOUT = "round_timeout"


class SynchronizedData(BaseSynchronizedData):
    """Synchronised data."""


class SelectKeeperRound(CollectDifferentUntilThresholdRound):
    """SelectKeeperRound round implementation."""

    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    payload_class = SelectKeeperPayload
    selection_key = "content"
    collection_key = "content"


class DeclareWinnerOrLoser(CollectDifferentUntilThresholdRound):
    """DeclareWinnerOrLoser round implementation."""

    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    payload_class = DeclareWinnerOrLoserPayload
    selection_key = "content"
    collection_key = "content"


class RandomTaskRound(CollectDifferentUntilThresholdRound):
    """RandomTaskRound round implementation."""

    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    payload_class = RandomTaskPayload
    selection_key = "content"
    collection_key = "content"


class RegistrationRound(CollectDifferentUntilThresholdRound):
    """RegistrationRound round implementation."""

    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    payload_class = RegistrationPayload
    selection_key = "content"
    collection_key = "content"


class ChanceToFlipCoin(CollectDifferentUntilThresholdRound):
    """ChanceToFlipCoin round implementation."""

    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    payload_class = ChanceToFlipCoinPayload
    selection_key = "content"
    collection_key = "content"


class ResetAndPauseRound(CollectDifferentUntilThresholdRound):
    """ResetAndPauseRound round implementation."""

    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    payload_class = ResetAndPausePayload
    selection_key = "content"
    collection_key = "content"


class ValoryAbciApp(AbciApp[Event]):
    """AbciApp definition for valory_abci"""

    initial_round_cls: AppState = RegistrationRound
    initial_states: t.Set[AppState] = {RegistrationRound}
    transition_function: AbciAppTransitionFunction = {
        RegistrationRound: {Event.DONE: RandomTaskRound},
        RandomTaskRound: {
            Event.DONE: SelectKeeperRound,
            Event.NONE: RandomTaskRound,
            Event.NO_MAJORITY: RandomTaskRound,
            Event.ROUND_TIMEOUT: RandomTaskRound,
        },
        SelectKeeperRound: {
            Event.DONE: ChanceToFlipCoin,
            Event.NONE: RegistrationRound,
            Event.NO_MAJORITY: RegistrationRound,
            Event.ROUND_TIMEOUT: RegistrationRound,
        },
        ChanceToFlipCoin: {
            Event.DONE: DeclareWinnerOrLoser,
            Event.NONE: ChanceToFlipCoin,
            Event.NO_MAJORITY: ChanceToFlipCoin,
            Event.ROUND_TIMEOUT: ChanceToFlipCoin,
        },
        DeclareWinnerOrLoser: {
            Event.DONE: ResetAndPauseRound,
            Event.NONE: RegistrationRound,
            Event.ROUND_TIMEOUT: RandomTaskRound,
        },
        ResetAndPauseRound: {
            Event.DONE: RandomTaskRound,
            Event.NO_MAJORITY: RegistrationRound,
            Event.RESET_TIMEOUT: RegistrationRound,
        },
    }
    final_states: t.Set[AppState] = set()
    event_to_timeout: t.Dict[Event, float] = {Event.ROUND_TIMEOUT: 30.0}
    db_pre_conditions: t.Dict[AppState, t.Set[str]] = {RegistrationRound: set()}
    db_post_conditions: t.Dict[AppState, t.Set[str]] = {}
