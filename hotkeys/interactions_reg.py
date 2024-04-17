#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler


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
