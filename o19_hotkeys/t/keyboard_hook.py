#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from typing import Callable

from ts4lib.ts4l_ctypes import byref, c_uint32, c_ulong, cast, windll, WINFUNCTYPE, c_int, c_void_p, Structure, POINTER, GetLastError
from ts4lib.ts4l_ctypes.wintypes import MSG

from o19_hotkeys.modinfo import ModInfo
from sims4communitylib.enums.common_key import CommonKey
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'KeyboardHook')
log.enable()


# noinspection SpellCheckingInspection
class KeyboardHook:
    WH_KEYBOARD_LL = 13
    HC_ACTION = 0
    WM_KEYDOWN = 0x100
    WM_KEYUP = 0x101
    WM_SYSKEYDOWN = 0x104
    WM_SYSKEYUP = 0x105

    TIMEOUT = 1  # hook will stay idle 1s after switching task
    WAIT_OBJECT_0 = 0
    QS_ALLINPUT = 0x1FF

    callback = None
    is_active = False  # Require at least one focus change event before setting this to True
    is_loaded = True  # Keep True to avoid initialization issues.
    hook = None

    # noinspection SpellCheckingInspection
    class KBDLLHOOKSTRUCT(Structure):
        _fields_ = [
            ("vkCode", c_uint32),  # UInt32
            ("scanCode", c_uint32),  # UInt32
            ("flags", c_uint32),  # KBDLLHOOKSTRUCTFlags
            ("time", c_uint32),  # UInt32
            ("dwExtraInfo", c_ulong)  # UIntPtr
        ]

    # noinspection SpellCheckingInspection
    class KBDLLHOOKSTRUCTFlags:
        LLKHF_EXTENDED = 0x01
        LLKHF_INJECTED = 0x10
        LLKHF_ALTDOWN = 0x20
        LLKHF_UP = 0x80

    def __init__(self, callback: Callable):
        KeyboardHook.callback = callback

    @staticmethod
    def active(is_active: bool):
        # TS4 process is running in foreground
        if KeyboardHook.is_active == is_active:
            return
        log.debug(f"Focus: {is_active}")
        KeyboardHook.is_active = is_active
        if is_active is True and KeyboardHook.callback:
            KeyboardHook.callback(CommonKey.ESCAPE, key_down=None)  # Reset all key states keys

    @staticmethod
    def zone_loaded(is_loaded: bool):
        # Zone is loaded
        if KeyboardHook.is_loaded == is_loaded:
            return
        log.debug(f"Zone: {is_loaded}")
        KeyboardHook.is_loaded = is_loaded

    # noinspection PyPep8Naming
    @staticmethod
    def _keyboard_hook_proc(nCode, wParam, lParam):
        if KeyboardHook.is_active and KeyboardHook.is_loaded:
            if nCode == KeyboardHook.HC_ACTION:
                if wParam in (KeyboardHook.WM_KEYDOWN, KeyboardHook.WM_SYSKEYDOWN):
                    key = cast(lParam, POINTER(KeyboardHook.KBDLLHOOKSTRUCT)).contents.vkCode
                    KeyboardHook.callback(key, key_down=True)
                    # KeyboardHook._on_key_down(key)
                elif wParam in (KeyboardHook.WM_KEYUP, KeyboardHook.WM_SYSKEYUP):
                    key = cast(lParam, POINTER(KeyboardHook.KBDLLHOOKSTRUCT)).contents.vkCode
                    KeyboardHook.callback(key, key_down=False)
                    # KeyboardHook._on_key_up(key)

        # Enqueue the event for the next hook
        return windll.user32.CallNextHookEx(KeyboardHook.hook, nCode, wParam, lParam)

    @staticmethod
    def _on_key_down(key: int):
        log.debug(f"Key Down: {key}")

    @staticmethod
    def _on_key_up(key: int):
        log.debug(f"Key Up: {key}")

    def do_hook(self):
        # log.debug(f"KeyboardHook.hook: start ({KeyboardHook.is_active})")
        if KeyboardHook.is_active and KeyboardHook.is_loaded and KeyboardHook.callback:
            kb_hook_proc = WINFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))(
                self._keyboard_hook_proc)
            if not kb_hook_proc:
                raise Exception("Error in setting the kb_hook_proc! ")

            current_module_handle = 0
            KeyboardHook.hook = windll.user32.SetWindowsHookExW(
                KeyboardHook.WH_KEYBOARD_LL, kb_hook_proc, current_module_handle, 0)
            log.debug(f"KeyboardHook.hook {self.hook}")

            if not KeyboardHook.hook:
                error_code = GetLastError()
                raise Exception(f"KeyboardHook: Error in setting the hook! {error_code}")

            log.debug("KeyboardHook.hook: active")
            # KeyboardHook.hook
            while True:
                if KeyboardHook.is_active and KeyboardHook.hook:
                    result = windll.user32.MsgWaitForMultipleObjects(0, None, False, KeyboardHook.TIMEOUT, KeyboardHook.QS_ALLINPUT)
                    if result == KeyboardHook.WAIT_OBJECT_0:
                        msg = MSG()
                        while windll.user32.PeekMessageW(byref(msg), 0, 0, 0, 1):  # PM_REMOVE
                            # Dispatch the message (handle it as needed)
                            windll.user32.DispatchMessageW(byref(msg))
                            windll.user32.TranslateMessage(byref(msg))
                else:
                    break
            # unhook
            windll.user32.UnhookWindowsHookEx(KeyboardHook.hook)
            log.debug("KeyboardHook.hook: end")
