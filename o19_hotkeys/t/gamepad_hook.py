#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


import time

from o19_hotkeys.gp.enums.gamepad_constants import GamepadConstants
from o19_hotkeys.gp.gamepad_init import GamepadInit


from typing import Callable

from o19_hotkeys.gp.gamepad_state import GamepadState
from o19_hotkeys.modinfo import ModInfo

try:
    from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'GamepadHook')
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(ModInfo.get_identity().name, 'GamepadHook', custom_file_path=None)

log.enable()


# noinspection SpellCheckingInspection
class GamepadHook:
    callback = None

    def __init__(self, callback: Callable, trace_log: bool = False):
        GamepadHook.callback = callback
        self.gi = GamepadInit()
        self._last_state = self.gi.state()
        self._last_error = -1
        self.last_norm_values = None
        self.connected = False

        gs = GamepadState()
        self.gamepad_id = gs.gamepad_id
        self.button_repeat_rate = gs.button_repeat_rate  # n seconds delay if a gamepad key is held down
        self.repeat_at = 0

        self._trace_log = trace_log
    @property
    def trace_log(self) -> bool:
        return self._trace_log

    @trace_log.setter
    def trace_log(self, do_log: bool):
        self._trace_log = bool(do_log)

    def read(self) -> int:
        state = self.gi.state()

        _error = self.gi.XInputGetState(self.gamepad_id, state)
        if _error != GamepadConstants.ERROR_SUCCESS:
            if _error != self._last_error:
                self._last_error = _error
                log.debug(f"Controller error: {_error}")
                return _error

        keys_down = state.Gamepad.wButtons
        delta_keys_down = state.Gamepad.wButtons & ~self._last_state.Gamepad.wButtons
        if delta_keys_down:
            GamepadHook.callback(delta_keys_down, key_down=True)  # send only the new keys
            self._last_state.Gamepad.wButtons = keys_down  # set all pressed keys
            self.repeat_at = time.time() + self.button_repeat_rate
        elif keys_down:  # same keys are still held down
            if time.time() > self.repeat_at:
                GamepadHook.callback(keys_down, key_down=True)  # send all keys
                self.repeat_at = time.time() + self.button_repeat_rate

        x = 0.0
        y = 0.0
        z = 0.0
        stick_left_or_right = None
        for i in (
                ('y', -0.1, 'bLeftTrigger', GamepadConstants.XINPUT_GAMEPAD_LEFT_TRIGGER_THRESHOLD, 2**8-1),
                ('y', 0.1, 'bRightTrigger', GamepadConstants.XINPUT_GAMEPAD_RIGHT_TRIGGER_THRESHOLD, 2**8-1),
                ('stick_l_x', 0.1, 'sThumbLX', GamepadConstants.XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE, 2**15-1),
                ('stick_l_z', -0.1, 'sThumbLY', GamepadConstants.XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE, 2 ** 15 - 1),
                ('stick_r_x', 0.1, 'sThumbRX', GamepadConstants.XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE, 2**15-1),
                ('stick_r_z', -0.1, 'sThumbRY', GamepadConstants.XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE, 2 ** 15 - 1)
        ):
            axis, multiplier, analog_input_name, treshold, max_value = i
            new_state_int = getattr(state.Gamepad, analog_input_name)
            # check if the controller is outside a circular dead zone
            if abs(new_state_int) > treshold:
                # adjust magnitude relative to the end of the dead zone
                if new_state_int > treshold:
                    new_state = new_state_int - treshold
                else:
                    new_state = new_state_int + treshold
                new_state /= (max_value - treshold)
                new_state *= multiplier
            else:
                new_state = 0.0

            if axis == 'stick_l_x' or axis == 'stick_r_x':
                x = new_state
            elif axis == 'y':
                y = y + new_state
            elif axis == 'stick_l_z':
                z = new_state
                stick_left_or_right = True
            else:  # axis == 'stick_r_z'
                z = new_state
                stick_left_or_right = False

            if stick_left_or_right is None:
                continue
            if 0 == x == y == z:
                stick_left_or_right = None
                continue
            if stick_left_or_right is True:
                if self._trace_log:
                    log.debug(f"GamepadHook.callback stick_l {x} {y} {z} None")
                GamepadHook.callback(f"stick_l {x} {y} {z}", key_down=None)
            else:
                if self._trace_log:
                    log.debug(f"GamepadHook.callback stick_r {x} {y} {z} None")
                GamepadHook.callback(f"stick_r {x} {y} {z}", key_down=None)
            stick_left_or_right = None
        return 0
