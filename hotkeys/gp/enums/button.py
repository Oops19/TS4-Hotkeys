#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class Button(CommonEnum):
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
    BUTTON_GUIDE = 0x000400  # n/a / deprecated
    BUTTON_A = 0x001000
    BUTTON_B = 0x002000
    BUTTON_X = 0x004000
    BUTTON_Y = 0x008000
