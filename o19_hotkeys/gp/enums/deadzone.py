#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class Deadzone(CommonEnum):
    DEADZONE_DEFAULT = 2 ** 4 - 1

    DEADZONE_LEFT_THUMB = 2 ** 0
    DEADZONE_RIGHT_THUMB = 2 ** 1
    DEADZONE_LEFT_TRIGGER = 2 ** 2
    DEADZONE_RIGHT_TRIGGER = 2 ** 3

    # These values may be modified during initialization
    XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE = 7849
    XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE = 8689
    # XINPUT_GAMEPAD_TRIGGER_THRESHOLD = 30  # MSDN defines just one for L+R
    XINPUT_GAMEPAD_LEFT_TRIGGER_THRESHOLD = 30
    XINPUT_GAMEPAD_RIGHT_TRIGGER_THRESHOLD = 30
