"""This package contains behaviour implementations."""
import typing as t
from abc import ABC

from packages.valory.skills.abstract_round_abci.behaviours import AbstractRoundBehaviour
from packages.valory.skills.abstract_round_abci.behaviours import (
    BaseBehaviour as AbstractBaseBehaviour,
)

from packages.valory.skills.valory_abci.payloads import (
    ChanceToFlipCoinPayload,
    DeclareWinnerOrLoserPayload,
    RandomTaskPayload,
    RegistrationPayload,
    ResetAndPausePayload,
    SelectKeeperPayload,
)
from packages.valory.skills.valory_abci.rounds import (
    ChanceToFlipCoin,
    DeclareWinnerOrLoser,
    RandomTaskRound,
    RegistrationRound,
    ResetAndPauseRound,
    SelectKeeperRound,
    ValoryAbciApp,
)


class BaseBehaviour(AbstractBaseBehaviour, ABC):
    """Base behaviour for the FSM App."""


class SelectKeeperBehaviour(BaseBehaviour):
    """SelectKeeperBehaviour behaviour implementation."""

    matching_round = SelectKeeperRound

    def async_act(self) -> t.Generator:
        """Do the action."""
        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            payload = SelectKeeperPayload(self.context.agent_address, "content")
        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()
        self.set_done()


class DeclareWinnerOrLoserBehaviour(BaseBehaviour):
    """DeclareWinnerOrLoserBehaviour behaviour implementation."""

    matching_round = DeclareWinnerOrLoser

    def async_act(self) -> t.Generator:
        """Do the action."""
        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            payload = DeclareWinnerOrLoserPayload(self.context.agent_address, "content")
        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()
        self.set_done()


class RandomTaskBehaviour(BaseBehaviour):
    """RandomTaskBehaviour behaviour implementation."""

    matching_round = RandomTaskRound

    def async_act(self) -> t.Generator:
        """Do the action."""
        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            payload = RandomTaskPayload(self.context.agent_address, "content")
        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()
        self.set_done()


class RegistrationBehaviour(BaseBehaviour):
    """RegistrationBehaviour behaviour implementation."""

    matching_round = RegistrationRound

    def async_act(self) -> t.Generator:
        """Do the action."""
        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            payload = RegistrationPayload(self.context.agent_address, "content")
        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()
        self.set_done()


class ChanceToFlipCoinBehaviour(BaseBehaviour):
    """ChanceToFlipCoinBehaviour behaviour implementation."""

    matching_round = ChanceToFlipCoin

    def async_act(self) -> t.Generator:
        """Do the action."""
        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            payload = ChanceToFlipCoinPayload(self.context.agent_address, "content")
        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()
        self.set_done()


class ResetAndPauseBehaviour(BaseBehaviour):
    """ResetAndPauseBehaviour behaviour implementation."""

    matching_round = ResetAndPauseRound

    def async_act(self) -> t.Generator:
        """Do the action."""
        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            payload = ResetAndPausePayload(self.context.agent_address, "content")
        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()
        self.set_done()


class ValoryRoundBehaviour(AbstractRoundBehaviour):
    """This behaviour manages the consensus stages."""

    initial_behaviour_cls = RegistrationBehaviour
    abci_app_cls = ValoryAbciApp
    behaviours: t.Set[t.Type[BaseBehaviour]] = {
        SelectKeeperBehaviour,
        DeclareWinnerOrLoserBehaviour,
        RandomTaskBehaviour,
        RegistrationBehaviour,
        ChanceToFlipCoinBehaviour,
        ResetAndPauseBehaviour,
    }
