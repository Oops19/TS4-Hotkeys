#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class Analog(CustomEnum):
    STICK_LEFT = 0x010000
    STICK_RIGHT = 0x020000
    TRIGGER_LEFT = 0x040000
    TRIGGER_RIGHT = 0x080000
