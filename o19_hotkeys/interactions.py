#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


try:
    from hk_move2.move import Move
except:
    pass
from o19_hotkeys.modinfo import ModInfo

from typing import Any

from interactions.context import InteractionContext
from objects.terrain import TerrainPoint
from sims.sim import Sim

from sims4communitylib.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from sims4communitylib.classes.testing.common_execution_result import CommonExecutionResult
from sims4communitylib.classes.testing.common_test_result import CommonTestResult
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry


log: CommonLog = CommonLogRegistry().get().register_log(ModInfo.get_identity(), 'InteractionsHotkeys')
log.enable()


class InteractionsHotkeys(CommonImmediateSuperInteraction):

    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        log.debug(f"InteractionsHotkeys: on_test({interaction_sim}, {interaction_target}, {interaction_context})")
        return CommonTestResult.TRUE

    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        log.debug(f"on_started({interaction_sim}, {interaction_target}, )")
        try:
            if isinstance(interaction_target, TerrainPoint):
                Move().item = None
                log.debug(f"New move object: None >> The Active Sim while be moved / rotated.")
            else:
                Move().item = interaction_target
                log.debug(f"New move object: {interaction_target}")
            return CommonExecutionResult.TRUE
        except Exception as e:
            log.warn(f"Error {e}")
