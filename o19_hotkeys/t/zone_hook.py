#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from typing import Callable

from o19_hotkeys.modinfo import ModInfo
from o19_hotkeys.t.focus_hook import FocusHook
from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_early_load import S4CLZoneEarlyLoadEvent

from sims4communitylib.events.zone_spin.events.zone_late_load import S4CLZoneLateLoadEvent
from sims4communitylib.events.zone_spin.events.zone_teardown import S4CLZoneTeardownEvent
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ZoneHook')
log.enable()


class ZoneHook:
    callback = None

    def __init__(self, callback: Callable = None):
        """ S4CL does call event handlers before the class has been initialized! """
        if callback is None:
            return
        ZoneHook.callback = callback
        log.debug(f"ZoneHook({callback})")

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity())
    def handle_event_zone_load_1(event_data: S4CLZoneEarlyLoadEvent):
        if ZoneHook.callback is not None:
            ZoneHook.callback(True)
            FocusHook._focus_handler(None, None, None, None, None, None, None)

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity())
    def handle_event_zone_unload(event_data: S4CLZoneTeardownEvent):
        if ZoneHook.callback is not None:
            ZoneHook.callback(False)
