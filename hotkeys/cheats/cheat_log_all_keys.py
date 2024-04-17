#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from hotkeys.modinfo import ModInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput


class CheatLogAllKeys:
    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.hk.toggle.log.keys', 'Toggle logging for debug purposes.')
    def cheat_o19_hk_log_keys(output: CommonConsoleCommandOutput):
        try:
            from hotkeys.hk.hotkey_manager import HotkeyManager
            HotkeyManager._log_all_keys = not HotkeyManager._log_all_keys
            output(f"Logging of all keys = '{HotkeyManager._log_all_keys}'")
        except Exception as e:
            output(f"Error: {e}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.hk.toggle.log.move', 'Toggle logging for debug purposes.')
    def cheat_o19_hk_log_move(output: CommonConsoleCommandOutput):
        try:
            from hk_move.move import Move
            Move.trace_log = not Move.trace_log
            output(f"Move.trace_log = '{Move.trace_log}'")
        except Exception as e:
            output(f"Error: {e}")