#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class Event(CommonEnum):
    EVENT_CONNECTED = 1
    EVENT_DISCONNECTED = 2
    EVENT_BUTTON_PRESSED = 3
    EVENT_BUTTON_RELEASED = 4
    EVENT_TRIGGER_MOVED = 5
    EVENT_STICK_MOVED = 6
