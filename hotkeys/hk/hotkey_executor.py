#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


import os
from queue import Queue, Empty

from hk_move.translate_keys import TranslateKeys
from hotkeys.hk.hotkey_manager import HotkeyManager
from hotkeys.hk.hotkey_reader import HotkeyReader
from hotkeys.modinfo import ModInfo
from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.interval.common_interval_event_service import CommonIntervalEventRegistry
from sims4communitylib.events.zone_spin.events.zone_late_load import S4CLZoneLateLoadEvent
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
from ts4lib.utils.singleton import Singleton

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'HotkeyExecutor')
log.enable()


class HotkeyExecutor(object, metaclass=Singleton):
    """
    Provide a Queue to the HotkeyManager. The HkManager will write to this queue.
    This class reads the queue and executes the callback methods.
    """
    _queue = None
    _hk_manager = None
    translate_keys = None
    _error_count = 0
    MAX_ERROR_COUNT = 5

    def __init__(self):
        if not os.name == "nt":
            return
        try:
            _hotkey_reader = HotkeyReader()
            num_registered_keys = _hotkey_reader.read_configuration()
            if num_registered_keys <= 0:
                return

            HotkeyExecutor._queue = Queue(maxsize=10)
            HotkeyExecutor._hk_manager = HotkeyManager(HotkeyExecutor._queue)
            HotkeyExecutor._hk_manager.log_hotkeys()

            HotkeyExecutor.translate_keys = TranslateKeys()
        except Exception as e:
            log.error(f"Error {e}")

    @staticmethod
    @CommonIntervalEventRegistry.run_every(ModInfo.get_identity(), milliseconds=500)
    def queue_reader():
        # should we run this every time the TS4 scheduler is ready to run it, or only when needed?
        # This code should disable reading the queue after 5 read errors (empty queue)
        # When the queue is filled also 'read_queue' is set to True
        # 'read_queue' is bool and should be thread safe.
        # To be discussed whether 'if bool' is faster then 'try/queue.get()/except'.
        # Not very useful within run_every() as this function is called not too often.
        try:
            if HotkeyExecutor._queue is not None and HotkeyExecutor._hk_manager.read_queue is True:
                while True:
                    (callback, parameter) = HotkeyExecutor._queue.get(block=False)
                    HotkeyExecutor._error_count = 0
                    log.debug(f'queue: {callback}({parameter})')
                    try:
                        if parameter:
                            callback(parameter)
                        else:
                            callback()
                    except:
                        log.error(f"Error executing '{callback}({parameter})")

        except Empty:
            HotkeyExecutor._error_count += 1
            log.debug(f'empty queue ({HotkeyExecutor._error_count})')
            if HotkeyExecutor._error_count > HotkeyExecutor.MAX_ERROR_COUNT:
                HotkeyExecutor._hk_manager.read_queue = False


if True is True:
    HotkeyExecutor()
else:
    # noinspection PyUnusedLocal
    @CommonEventRegistry.handle_events(ModInfo.get_identity())
    def _zone_load(event_data: S4CLZoneLateLoadEvent):
        HotkeyExecutor()
