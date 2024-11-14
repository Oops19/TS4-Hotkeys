#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.enums.affordance_list_ids import CommonAffordanceListId
from sims4communitylib.enums.enumtypes.common_int import CommonInt
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from sims4communitylib.services.resources.common_instance_manager_modification_registry import CommonInstanceManagerModificationRegistry
from sims4communitylib.services.resources.modification_handlers.common_add_interactions_to_affordance_lists_handler import CommonAddInteractionsToAffordanceListsModificationHandler


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class RegisterInteractionsHotkeysHotkeys0(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0xB6A68E0B9935BEE4,  # 'Move' - fnv('o19_Hotkeys_0_PMA_Move_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_TERRAIN_LOAD)
class RegisterInteractionsHotkeysHotkeys1(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0xB6A68E0B9935BEE4,  # 'Move' - fnv('o19_Hotkeys_0_PMA_Move_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return True


@CommonInstanceManagerModificationRegistry.register_modification_handler()
class RegisterInteractionsHotkeysHotkeys0_Debug(CommonAddInteractionsToAffordanceListsModificationHandler):
    @property
    def interaction_ids(self) -> Tuple[CommonInt, ...]:
        interactions: Tuple = (
            0xB6A68E0B9935BEE4,  # 'Move' - fnv('o19_Hotkeys_0_PMA_Move_debug')
        )
        return interactions

    @property
    def affordance_list_ids(self) -> Tuple[int, ...]:
        result: Tuple[int, ...] = (
            CommonAffordanceListId.DEBUG_AFFORDANCES,
        )
        return result


class RegisterInteractionsHotkeysHotkeys0_DD:
    def __init__(self):
        try:
            import deviousdesires
            from deviousdesires.sex._injects._block_interactions_during_animation import DDInteractionBlocker
            ids = list(self.interaction_ids)
            deviousdesires.sex._injects._block_interactions_during_animation.DDInteractionBlocker().add_allowed_interaction_ids(ids)
        except:
            pass

    @property
    def interaction_ids(self) -> Tuple[CommonInt, ...]:
        interactions: Tuple = (
            0xB6A68E0B9935BEE4,  # 'Move' - fnv('o19_Hotkeys_0_PMA_Move_debug')
        )
        return interactions


RegisterInteractionsHotkeysHotkeys0_DD()
