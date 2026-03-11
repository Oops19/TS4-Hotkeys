#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


import sys
import ts4l_ctypes
from o19_hotkeys.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'KeyboardPriority')
log.enable()


class KeyboardPriority:
    # Thread priority constants
    THREAD_PRIORITY_LOWEST = -2
    THREAD_PRIORITY_BELOW_NORMAL = -1
    THREAD_PRIORITY_NORMAL = 0
    THREAD_PRIORITY_ABOVE_NORMAL = 1
    THREAD_PRIORITY_HIGHEST = 2
    THREAD_PRIORITY_TIME_CRITICAL = 15

    @staticmethod
    def set_priority(new_priority: int = 0):
        try:
            kernel32 = ts4l_ctypes.windll.kernel32
            # Get a pseudo-handle for the current thread
            thread_handle = kernel32.GetCurrentThread()

            # Set priority to highest non-realtime
            success = kernel32.SetThreadPriority(thread_handle, new_priority)

            if success:
                sys.setswitchinterval(0.0025)
            else:
                log.warn(f"Failed to set thread priority (success=False)")

        except Exception as e:
            log.warn(f"Failed to set thread priority ({e})")
