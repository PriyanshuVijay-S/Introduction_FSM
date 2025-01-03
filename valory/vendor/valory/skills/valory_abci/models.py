# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 valory
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
# mypy: disable-error-code="import"
# pylint: disable=import-error,  too-few-public-methods, unused-import

"""This module contains the shared state for the abci skill of ValoryAbciApp."""

from packages.valory.skills.valory_abci.rounds import (
    ValoryAbciApp,  # type: ignore[import]
)
from packages.valory.skills.abstract_round_abci.models import (  # type: ignore[import] # noqa: F401
    ApiSpecs,
    BaseParams,
)
from packages.valory.skills.abstract_round_abci.models import (
    BenchmarkTool as BaseBenchmarkTool,  # type: ignore[import]
)
from packages.valory.skills.abstract_round_abci.models import (
    Requests as BaseRequests,  # type: ignore[import]
)
from packages.valory.skills.abstract_round_abci.models import (
    SharedState as BaseSharedState,  # type: ignore[import]
)


Requests = BaseRequests
BenchmarkTool = BaseBenchmarkTool


class SharedState(BaseSharedState):
    """Keep the current shared state of the skill."""

    abci_app_cls = ValoryAbciApp


class Params(BaseParams):
    """A model to represent params for multiple abci apps."""
