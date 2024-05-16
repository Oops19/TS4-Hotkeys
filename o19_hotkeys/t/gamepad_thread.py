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


from o19_hotkeys.t.gamepad_hook import GamepadHook
from o19_hotkeys.gp.gamepad_state import GamepadState

from o19_hotkeys.modinfo import ModInfo
from ts4lib.utils.simple_ui_notification import SimpleUINotification

try:
    from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'GamepadThread')
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(ModInfo.get_identity().name, 'GamepadThread', custom_file_path=None)
log.enable()


class GamepadThread:

    def __init__(self, callback: Callable):
        log.debug(f"GamepadThread({callback})")
        self.gamepad_hook = GamepadHook(callback)
        self.gamepad_state = GamepadState()
        self._stop = False

    def loop(self):
        log.debug("GamepadThread: loop(start)")
        while True:
            if self.gamepad_state:
                error_code = self.gamepad_hook.read()
                if error_code == 0:
                    time.sleep(self.gamepad_state.poll_delay)
                    continue
                else:
                    SimpleUINotification().show(f"Gamepad '#{self.gamepad_state.gamepad_id}'", f"Connection error: '{error_code}'")

            time.sleep(3)  # while disabled or if an error occurs idle at least 3 seconds
            if self._stop:
                break
        log.debug("GamepadThread: loop(end)")

    def start_thread(self):
        log.debug("GamepadThread: start_thread()")
        self._stop = False
        thread: threading.Thread = threading.Thread(target=self.loop)
        thread.daemon = True
        thread.start()
        log.debug("GamepadThread: start_thread(end)")
