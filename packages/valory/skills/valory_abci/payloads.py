"""This module contains the transaction payloads for common apps."""
from dataclasses import dataclass

from packages.valory.skills.abstract_round_abci.base import BaseTxPayload


@dataclass(frozen=True)
class SelectKeeperPayload(BaseTxPayload):
    """SelectKeeperPayload class."""

    content: str


@dataclass(frozen=True)
class DeclareWinnerOrLoserPayload(BaseTxPayload):
    """DeclareWinnerOrLoserPayload class."""

    content: str


@dataclass(frozen=True)
class RandomTaskPayload(BaseTxPayload):
    """RandomTaskPayload class."""

    content: str


@dataclass(frozen=True)
class RegistrationPayload(BaseTxPayload):
    """RegistrationPayload class."""

    content: str


@dataclass(frozen=True)
class ChanceToFlipCoinPayload(BaseTxPayload):
    """ChanceToFlipCoinPayload class."""

    content: str


@dataclass(frozen=True)
class ResetAndPausePayload(BaseTxPayload):
    """ResetAndPausePayload class."""

    content: str
