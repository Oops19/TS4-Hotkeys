#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from hotkeys.gp.gamepad_manager import GamepadManager
from hotkeys.gp.gamepad_state import GamepadState
from hotkeys.modinfo import ModInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput


class GamepadCheats:
    gs = GamepadState()

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.hk.gp.enable', 'Enable or disable the controller.')
    def cheat_o19_hk_gp_toggle_enable(output: CommonConsoleCommandOutput):
        GamepadCheats.gs.enabled = not GamepadCheats.gs.enabled
        GamepadCheats.gs.manager = GamepadManager()
        output(f"Gamepad state: {GamepadCheats.gs.enabled}; Gamepad manager: {GamepadCheats.gs.manager}")

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.hk.gp.verbose', 'Toggle logging for debug purposes.'
    )
    def cheat_o19_hk_gp_toggle_verbose_log(output: CommonConsoleCommandOutput):
        GamepadCheats.gs.verbose_log = not GamepadCheats.gs.verbose_log
        output(f"Gamepad verbose log: {GamepadCheats.gs.verbose_log}")

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.hk.gp.id', 'Select the controller ID (0-3).',
        command_arguments=(
                CommonConsoleCommandArgument('gamepad_id', 'int', 'ID of the gamepad to use.', is_optional=False),
        )
    )
    def cheat_o19_hk_gp_set_id(output: CommonConsoleCommandOutput, gamepad_id: int):
        GamepadCheats.gs.gamepad_id = int(gamepad_id)
        output(f"Gamepad ID: {GamepadCheats.gs.gamepad_id}")

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.hk.gp.button_repeat_rate', 'Set the button repeat rate.',
        command_arguments=(
                CommonConsoleCommandArgument('button_repeat_rate', 'float', 'tbd', is_optional=False),
        )
    )
    def cheat_o19_hk_gp_set_poll_delay(output: CommonConsoleCommandOutput, button_repeat_rate: float):
        GamepadCheats.gs.button_repeat_rate = float(button_repeat_rate)
        output(f"Gamepad button repeat rate: {GamepadCheats.gs.button_repeat_rate}")

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.hk.gp.poll_delay', 'Set the poll delay.',
        command_arguments=(
                CommonConsoleCommandArgument('poll_delay', 'float', 'The time to wait after checking the controller state', is_optional=False),
        )
    )
    def cheat_o19_hk_gp_set_poll_delay(output: CommonConsoleCommandOutput, poll_delay: float):
        GamepadCheats.gs.poll_delay = float(poll_delay)
        output(f"Gamepad poll delay: {GamepadCheats.gs.poll_delay}")
