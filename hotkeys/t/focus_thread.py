#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


import threading
from typing import Callable

from hotkeys.t.focus_hook import FocusHook

from hotkeys.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'FocusThread')
log.enable()


class FocusThread:
    # Constants
    EVENT_SYSTEM_FOREGROUND = 3
    callback = None
    current_process_id = -1
    event_hook = 0

    def __init__(self, callback: Callable):
        log.debug(f"FocusThread({callback})")
        self.focus_hook = FocusHook(callback)
        self._stop = False

    def loop(self):
        log.debug("FocusThread: loop()")
        self.focus_hook.do_hook()
        log.debug("FocusThread: loop(end)")

    def start_thread(self):
        log.debug("FocusThread: start_thread()")
        self._stop = False
        thread: threading.Thread = threading.Thread(target=self.loop)
        thread.daemon = True
        thread.start()
        log.debug("FocusThread: start_thread(end)")

    def stop_thread(self):
        self._stop = True
