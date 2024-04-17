#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from queue import Queue, Full

from hotkeys.t.focus_thread import FocusThread
from hotkeys.hk.hotkey_store import HotkeyStore
from hotkeys.hk.key_definition import KeyDefinition
from hotkeys.t.keyboard_hook import KeyboardHook
from hotkeys.t.keyboard_thread import KeyboardThread

from ts4lib.utils.singleton import Singleton
from sims4communitylib.enums.common_key import CommonKey

from hotkeys.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
from sims4communitylib.utils.common_time_utils import CommonTimeUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'HotkeyManager')
log.enable()
log.debug("starting ..")


class HotkeyManager(object, metaclass=Singleton):
    _is_l_shift_down = False
    _is_l_ctrl_down = False
    _is_l_alt_down = False
    _is_l_win_down = False
    _is_r_shift_down = False
    _is_r_ctrl_down = False
    _is_r_alt_down = False
    _is_r_win_down = False
    _is_shift_down = False
    _is_ctrl_down = False
    _is_alt_down = False
    _is_win_down = False

    _keyboard_thread = None
    _focus_thread = None
    _take_control = False

    _queue = None
    _hotkey_store = None
    _exception_logged = False

    kd_shift_alt = KeyDefinition(0, shift=True, alt=True).full_key_code
    kd_shift_ctrl_alt = KeyDefinition(0, shift=True, ctrl=True, alt=True).full_key_code

    _read_queue = False
    _log_all_keys = False  # enable it with 'o19.hk.toggle.log' for debugging purposes

    @staticmethod
    def hotkey_callback(event, key_down: bool = None):
        """
        Each log statement causes 100-200 ms delay
        """
        if HotkeyManager._log_all_keys:
            log.debug(f"Event: '{event}'; key_down='{key_down}'")

        if key_down is None:
            if CommonKey.ESCAPE == event:
                # Reset all saved key states
                HotkeyManager._is_l_shift_down = False
                HotkeyManager._is_l_ctrl_down = False
                HotkeyManager._is_l_alt_down = False
                HotkeyManager._is_l_win_down = False
                HotkeyManager._is_r_shift_down = False
                HotkeyManager._is_r_ctrl_down = False
                HotkeyManager._is_r_alt_down = False
                HotkeyManager._is_r_win_down = False
                HotkeyManager._is_shift_down = False
                HotkeyManager._is_ctrl_down = False
                HotkeyManager._is_alt_down = False
                HotkeyManager._is_win_down = False
            return

        if CommonKey.SHIFT_LEFT <= event <= CommonKey.ALT_RIGHT:
            if event == CommonKey.SHIFT_LEFT:
                HotkeyManager._is_l_shift_down = key_down
            elif event == CommonKey.SHIFT_RIGHT:
                HotkeyManager._is_r_shift_down = key_down
            elif event == CommonKey.CTRL_LEFT:
                HotkeyManager._is_l_ctrl_down = key_down
            elif event == CommonKey.CTRL_RIGHT:
                HotkeyManager._is_r_ctrl_down = key_down
            elif event == CommonKey.ALT_LEFT:
                HotkeyManager._is_l_alt_down = key_down
            else:
                # elif event == CommonKey.ALT_RIGHT:
                HotkeyManager._is_r_alt_down = key_down
            HotkeyManager._is_shift_down = HotkeyManager._is_l_shift_down or HotkeyManager._is_r_shift_down
            HotkeyManager._is_ctrl_down = HotkeyManager._is_l_ctrl_down or HotkeyManager._is_r_ctrl_down
            HotkeyManager._is_alt_down = HotkeyManager._is_l_alt_down or HotkeyManager._is_r_alt_down

            '''
            WINDOWS_LEFT: 'CommonKey' = 91
            WINDOWS_RIGHT: 'CommonKey' = 92
            APPLICATIONS: 'CommonKey' = 93
            '''
        elif 91 <= event <= 92:  # TODO fix CommonKey.WINDOWS_LEFT, CommonKey.WINDOWS_RIGHT
            if event == 91:
                HotkeyManager._is_l_win_down = key_down
            else:
                # elif event == 0x5C:  # CommonKey.WINDOWS_RIGHT:
                HotkeyManager._is_r_win_down = key_down
            HotkeyManager._is_win_down = HotkeyManager._is_l_win_down or HotkeyManager._is_r_win_down

        if key_down is False:  # process only key_down events
            return

        key_definition = KeyDefinition(event, shift=HotkeyManager._is_shift_down, ctrl=HotkeyManager._is_ctrl_down,
                                       alt=HotkeyManager._is_alt_down, win=HotkeyManager._is_win_down)
        full_key_code = key_definition.full_key_code

        if HotkeyManager._log_all_keys:
            log.debug(f"Event: '{event}'; {key_definition} ({full_key_code}) in Store == {HotkeyManager._hotkey_store.contains(full_key_code)}")

        if not HotkeyManager._hotkey_store.contains(full_key_code):
            return

        key_definition: KeyDefinition = HotkeyManager._hotkey_store.get_key_definition(full_key_code)
        callback = key_definition.callback
        parameter = key_definition.parameter
        synchronized = key_definition.synchronized
        if not synchronized or CommonTimeUtils.game_is_paused():
            try:
                if parameter:
                    callback(parameter)
                else:
                    callback()
            except:
                log.error(f"Error executing '{callback}({parameter}) - called via '{key_definition}'")
        else:
            try:
                HotkeyManager._queue.put((callback, parameter), block=False)
                HotkeyManager._read_queue = True
                HotkeyManager._hotkey_store.register_key_press(full_key_code)
            except Full:
                log.debug(f"Queue full - skipping '{key_definition}'")

    @property
    def read_queue(self) -> bool:
        return HotkeyManager._read_queue

    @read_queue.setter
    def read_queue(self, value: bool):
        HotkeyManager._read_queue = value

    @staticmethod
    def register_key(key_definition: KeyDefinition):
        if 0 < key_definition.key_code < 256:
            HotkeyManager._hotkey_store.register_key(key_definition)
            log.debug(f"Registered: {key_definition} -> {key_definition.description}")
        else:
            log.debug(f"Can't register reserved key with key code {key_definition.key_code}.")

    @staticmethod
    def un_register_key(key_definition):
        if 0 < key_definition.key_code < 256:
            HotkeyManager._hotkey_store.un_register_key(key_definition)

    @staticmethod
    def log_hotkeys():
        log.debug(f"All currently registered hotkeys:")
        for key_definition in HotkeyManager._hotkey_store.definitions.values():
            log.debug(f" * {key_definition} -> {key_definition.description}")

    def __init__(self, queue: Queue):
        HotkeyManager._queue = queue
        HotkeyManager._hotkey_store = HotkeyStore()

        # Start the Keyboard thread
        HotkeyManager._keyboard_thread = KeyboardThread(HotkeyManager.hotkey_callback)
        HotkeyManager._keyboard_thread.start_thread()

        # Start the Focus thread
        HotkeyManager._focus_thread = FocusThread(KeyboardHook.active)
        HotkeyManager._focus_thread.start_thread()
