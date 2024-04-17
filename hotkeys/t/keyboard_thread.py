#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


import threading
import time
from typing import Callable

from hotkeys.t.keyboard_hook import KeyboardHook

from hotkeys.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'KeyboardThread')
log.enable()


class KeyboardThread:

    def __init__(self, callback: Callable):
        log.debug(f"KeyboardThread({callback})")
        self.keyboard_hook = KeyboardHook(callback)
        self._stop = False

    def loop(self):
        while True:
            time.sleep(1)
            # log.debug("KeyboardThread: loop()")
            self.keyboard_hook.do_hook()
            if self._stop:
                break
        log.debug("KeyboardThread: loop(end)")

    def start_thread(self):
        log.debug("KeyboardThread: start_thread()")
        self._stop = False
        thread: threading.Thread = threading.Thread(target=self.loop)
        thread.daemon = True
        thread.start()
        log.debug("KeyboardThread: start_thread(end)")
