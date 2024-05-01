#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from typing import Callable

from ts4lib.ts4l_ctypes import c_ulong, byref, get_last_error, windll, wintypes, WINFUNCTYPE, WinError, GetLastError
from ts4lib.ts4l_ctypes.wintypes import MSG

from o19_hotkeys.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'FocusHook')
log.enable()


class FocusHook:
    # Constants
    EVENT_SYSTEM_FOREGROUND = 3

    callback = None
    current_process_id = -1
    hook = 0

    def __init__(self, callback: Callable):
        FocusHook.callback = callback
        FocusHook.current_process_id = windll.kernel32.GetCurrentProcessId()
        # Call self to detect application focus
        FocusHook._focus_handler(None, None, None, None, None, None, None)

    # noinspection PyPep8Naming,PyUnusedLocal
    @staticmethod
    def _focus_handler(hWinEventHook, event, hwnd, idObject, idChild, dwEventThread, dwmsEventTime):
        # Get the handle of the foreground window
        foreground_window = windll.user32.GetForegroundWindow()

        # Get the process ID of the foreground window
        foreground_process_id = c_ulong()
        windll.user32.GetWindowThreadProcessId(foreground_window, byref(foreground_process_id))

        # Check if the current process is the active window
        is_active_window = FocusHook.current_process_id == foreground_process_id.value
        # log.debug(f"FocusHook._focus_handler is_active_window {is_active_window}")

        FocusHook.callback(is_active_window)

    @staticmethod
    def do_hook():
        log.debug("FocusHook.hook: start")
        # Initialize COM library
        windll.ole32.CoInitialize(0)

        # SetWinEventHook parameters
        # noinspection PyPep8Naming
        WinEventProcType = WINFUNCTYPE(
            None,
            wintypes.HANDLE,
            wintypes.DWORD,
            wintypes.HWND,
            wintypes.LONG,
            wintypes.LONG,
            wintypes.DWORD,
            wintypes.DWORD
        )
        # noinspection PyPep8Naming
        WinEventProc = WinEventProcType(FocusHook._focus_handler)
        FocusHook.hook = windll.user32.SetWinEventHook(FocusHook.EVENT_SYSTEM_FOREGROUND, FocusHook.EVENT_SYSTEM_FOREGROUND,
                                                0, WinEventProc, 0, 0, 0)

        if not FocusHook.hook:
            error_code = GetLastError()
            raise Exception(f"FocusHook: Error in setting the hook! {error_code}")

        log.debug("FocusHook.hook: active")
        msg = MSG()
        while True:
            # noinspection PyPep8Naming
            bRet = windll.user32.GetMessageW(byref(msg), None, 0, 0)  # blocking call
            if not bRet:
                break
            if bRet == -1:
                raise WinError(get_last_error())
            windll.user32.TranslateMessageW(msg)
            windll.user32.DispatchMessageW(msg)

        # unhook if not bRet
        windll.user32.UnhookWinEvent(FocusHook.hook)
        windll.ole32.CoUninitialize()

        log.debug("FocusHook.hook: end")
        FocusHook.callback(False)  # disable key processing
