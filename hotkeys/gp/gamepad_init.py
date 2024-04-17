#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from hotkeys.gp.enums.gamepad_constants import GamepadConstants, XINPUT_STATE
from ts4lib.utils.simple_ui_notification import SimpleUINotification
from ts4lib.utils.singleton import Singleton

from ts4lib.ts4l_ctypes import util, byref, POINTER, WinDLL


class GamepadInit(metaclass=Singleton):
    def __init__(self):
        self.gs = GamepadConstants()
        self.libXInput = None
        # loading the DLL #
        for name in self.gs.XINPUT_DLLS:
            found = util.find_library(name)
            if found:
                self.libXInput = WinDLL(found)
                self.gs.XINPUT_DLL = name
                break

        if self.libXInput is None:
            SimpleUINotification().show(f"Gamepad Error", f"Failed to load the XInput DLL!")
            self.gs.enabled = False
            return

        self.state = XINPUT_STATE

        self.libXInput.XInputGetState.argtypes = [GamepadConstants.DWORD, POINTER(XINPUT_STATE)]
        self.libXInput.XInputGetState.restype = GamepadConstants.DWORD

    def XInputGetState(self, dwUserIndex, state):
        libXInput = WinDLL(util.find_library(self.gs.XINPUT_DLL))
        return libXInput.XInputGetState(dwUserIndex, byref(state))

    def _XInputGetState(self, dwUserIndex, state):
        if self.libXInput:
            return self.libXInput.XInputGetState(dwUserIndex, byref(state))
        return None

    def set_deadzone(self, dzone, value):
        """Sets the deadzone <dzone> to <value>.
    Any raw value retruned by the respective stick or trigger
    will be clamped to 0 if it's lower than <value>.
    The supported deadzones are:
    DEADZONE_RIGHT_THUMB (default value is 8689, max is 32767)
    DEADZONE_LEFT_THUMB  (default value is 7849, max is 32767)
    DEADZONE_TRIGGER     (default value is 30,   max is 255  )"""


        if value == GamepadConstants.DEADZONE_DEFAULT:
            value = 7849 if dzone == GamepadConstants.DEADZONE_LEFT_THUMB else 8689 if dzone == GamepadConstants.DEADZONE_RIGHT_THUMB else 30

        if dzone == GamepadConstants.DEADZONE_LEFT_THUMB:
            assert value >= 0 and value <= 32767
            if value == GamepadConstants.DEADZONE_DEFAULT:
                GamepadConstants.XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE = 7849
            else:
                GamepadConstants.XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE = value

        elif dzone == GamepadConstants.DEADZONE_RIGHT_THUMB:
            assert value >= 0 and value <= 32767
            if value == GamepadConstants.DEADZONE_DEFAULT:
                GamepadConstants.XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE = 8689
            else:
                GamepadConstants.XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE = value

        elif dzone == GamepadConstants.DEADZONE_LEFT_THUMB:
            assert value >= 0 and value <= 32767
            if value == GamepadConstants.DEADZONE_DEFAULT:
                GamepadConstants.XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE = 8689
            else:
                GamepadConstants.XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE = value

        else:
            assert value >= 0 and value <= 255
            if value == GamepadConstants.DEADZONE_DEFAULT:
                GamepadConstants.XINPUT_GAMEPAD_TRIGGER_THRESHOLD = 30
            else:
                GamepadConstants.XINPUT_GAMEPAD_TRIGGER_THRESHOLD = value

    def get_connected(self):
        """get_connected() -> (bool, bool, bool, bool)
        Returns wether or not the controller at each index is
        connected.
        You shouldn't check this too frequently."""
        controller_id = 0
        state = XINPUT_STATE()
        return self.XInputGetState(controller_id, state)

    def get_state(self):
        """get_state(int) -> XINPUT_STATE
    Returns the raw state of the controller."""
        controller_id = 0
        state = XINPUT_STATE()
        res = self.XInputGetState(controller_id, state)
        # GamepadConstants.ERROR_DEVICE_NOT_CONNECTED
        # GamepadConstants.ERROR_BAD_ARGUMENTS
        # GamepadConstants.ERROR_SUCCESS = 0
        return res
