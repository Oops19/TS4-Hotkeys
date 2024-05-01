#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.utils.singleton import Singleton
from ts4lib.ts4l_ctypes import c_ushort, c_ubyte, c_ulong, c_short, c_uint, Structure


class GamepadConstants(metaclass=Singleton):
    XINPUT_DLLS = (
            "XInput1_4.dll",  # W11
            "XInput9_1_0.dll"  # W10
        )
    XINPUT_DLL = None  # Stores the loaded DDL

    # defining static global variables #
    WORD = c_ushort
    BYTE = c_ubyte
    SHORT = c_short
    DWORD = c_ulong
    UINT = c_uint

    ERROR_SUCCESS = 0
    ERROR_BAD_ARGUMENTS = 160
    ERROR_DEVICE_NOT_CONNECTED = 1167

    # These three values may be modified during initialization
    DEADZONE_LEFT_THUMB = 0
    DEADZONE_RIGHT_THUMB = 1
    DEADZONE_LEFT_TRIGGER = 2
    DEADZONE_RIGTH_TRIGGER = 3

    XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE = 7849
    XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE = 8689
    # XINPUT_GAMEPAD_TRIGGER_THRESHOLD = 30  # MSDN defines just one for L+R
    XINPUT_GAMEPAD_LEFT_TRIGGER_THRESHOLD = 30
    XINPUT_GAMEPAD_RIGHT_TRIGGER_THRESHOLD = 30

    BATTERY_DEVTYPE_GAMEPAD = 0x00
    BATTERY_TYPE_DISCONNECTED = 0x00
    BATTERY_TYPE_WIRED = 0x01
    BATTERY_TYPE_ALKALINE = 0x02
    BATTERY_TYPE_NIMH = 0x03
    BATTERY_TYPE_UNKNOWN = 0xFF
    BATTERY_LEVEL_EMPTY = 0x00
    BATTERY_LEVEL_LOW = 0x01
    BATTERY_LEVEL_MEDIUM = 0x02
    BATTERY_LEVEL_FULL = 0x03

    BUTTON_DPAD_UP = 0x000001
    BUTTON_DPAD_DOWN = 0x000002
    BUTTON_DPAD_LEFT = 0x000004
    BUTTON_DPAD_RIGHT = 0x000008
    BUTTON_START = 0x000010
    BUTTON_BACK = 0x000020
    BUTTON_LEFT_THUMB = 0x000040
    BUTTON_RIGHT_THUMB = 0x000080
    BUTTON_LEFT_SHOULDER = 0x000100
    BUTTON_RIGHT_SHOULDER = 0x000200
    BUTTON_GUIDE = 0x000400  # deprecated
    BUTTON_A = 0x001000
    BUTTON_B = 0x002000
    BUTTON_X = 0x004000
    BUTTON_Y = 0x008000

    STICK_LEFT = 0x010000
    STICK_RIGHT = 0x020000
    TRIGGER_LEFT = 0x040000
    TRIGGER_RIGHT = 0x080000

    FILTER_PRESSED_ONLY = 0x100000
    FILTER_RELEASED_ONLY = 0x200000
    FILTER_NONE = 0xFFFFFF - FILTER_PRESSED_ONLY - FILTER_RELEASED_ONLY


    DEADZONE_DEFAULT = -1

    EVENT_CONNECTED = 1
    EVENT_DISCONNECTED = 2
    EVENT_BUTTON_PRESSED = 3
    EVENT_BUTTON_RELEASED = 4
    EVENT_TRIGGER_MOVED = 5
    EVENT_STICK_MOVED = 6

    LEFT = 0
    RIGHT = 1

    button_dict = {
            0x0001 : "DPAD_UP",
            0x0002 : "DPAD_DOWN",
            0x0004 : "DPAD_LEFT",
            0x0008 : "DPAD_RIGHT",
            0x0010 : "START",
            0x0020 : "BACK",
            0x0040 : "LEFT_THUMB",
            0x0080 : "RIGHT_THUMB",
            0x0100 : "LEFT_SHOULDER",
            0x0200 : "RIGHT_SHOULDER",
            0x0400 : "GUIDE",  # n/a
            0x1000 : "A",
            0x2000 : "B",
            0x4000 : "X",
            0x8000 : "Y",
        }

# defining XInput compatible structures #
class XINPUT_GAMEPAD(Structure):
    _fields_ = [
        ("wButtons", GamepadConstants.WORD),
        ("bLeftTrigger", GamepadConstants.BYTE),
        ("bRightTrigger", GamepadConstants.BYTE),
        ("sThumbLX", GamepadConstants.SHORT),
        ("sThumbLY", GamepadConstants.SHORT),
        ("sThumbRX", GamepadConstants.SHORT),
        ("sThumbRY", GamepadConstants.SHORT),
    ]

class XINPUT_STATE(Structure):
    _fields_ = [
        ("dwPacketNumber", GamepadConstants.DWORD),
        ("Gamepad", XINPUT_GAMEPAD),
    ]
