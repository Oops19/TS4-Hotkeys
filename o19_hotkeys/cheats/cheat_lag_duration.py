#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import sys

from o19_hotkeys.modinfo import ModInfo
from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_late_load import S4CLZoneLateLoadEvent
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, \
    CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput


class CheatLagDuration:

    @staticmethod
    def _set_lag_duration(t: int) -> int:
        dt = int(sys.getswitchinterval() * 10_000)
        sys.setswitchinterval(t/10_000)
        return dt

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.hk.lag', 'Set the keyboard lag.',
                          command_arguments=(
                                  CommonConsoleCommandArgument('t', 'number', 'The lag.', is_optional=True, default_value=50),
                          )
                          )
    def cheat_o19_hk_lag(output: CommonConsoleCommandOutput, t: int):
        """
        t = 1..1000, default: 50
        Set the keypress lag duration. 1===0.0001s; 10===0.001s; 50===0.005s 100===0.01s
        Setting this value to 5 .. 10 helps a lot to decrease the delay.
        """
        try:
            if 1 <= t <= 1000:
                output(f'Setting lag to {t}')
                t = CheatLagDuration._set_lag_duration(t)
            else:
                output(f"Only lag values from '1' to '1000' are supported.")
            output(f'Previous lag: {t} ({t/10_000:0.5f})')
        except Exception as e:
            output(f"Error: {e}")

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
    def o19_handle_event(event_data: S4CLZoneLateLoadEvent):  # S4CLZoneEarlyLoadEvent
        CheatLagDuration._set_lag_duration(7)
