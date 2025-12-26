#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class BatteryDevType(CustomEnum):
    BATTERY_DEVTYPE_GAMEPAD = 0x00


class BatteryType(CustomEnum):
    BATTERY_TYPE_DISCONNECTED = 0x00
    BATTERY_TYPE_WIRED = 0x01
    BATTERY_TYPE_ALKALINE = 0x02
    BATTERY_TYPE_NIMH = 0x03
    BATTERY_TYPE_UNKNOWN = 0xFF


class BatteryLevel(CustomEnum):
    BATTERY_LEVEL_EMPTY = 0x00
    BATTERY_LEVEL_LOW = 0x01
    BATTERY_LEVEL_MEDIUM = 0x02
    BATTERY_LEVEL_FULL = 0x03
