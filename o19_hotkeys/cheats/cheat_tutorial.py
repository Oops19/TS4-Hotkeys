#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Dict

from o19_hotkeys.hk.hotkey_store import HotkeyStore
from o19_hotkeys.hk.key_definition import KeyDefinition
from o19_hotkeys.modinfo import ModInfo
from ts4lib.utils.simple_ui_notification import SimpleUINotification
from sims4communitylib.events.interval.common_interval_event_service import CommonIntervalEventRegistry
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from ts4lib.utils.singleton import Singleton


class CheatTutorial(object, metaclass=Singleton):
    show_hints = True

    @staticmethod
    @CommonIntervalEventRegistry.run_every(ModInfo.get_identity(), milliseconds=60 * 60 * 1000)
    def repeat_show_hint():
        if CheatTutorial.show_hints:
            CheatTutorial._show_hint()

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.hk.hint', 'Animate the player to use a random hotkey.', )
    def cheat_o19_hk_hint(output: CommonConsoleCommandOutput):
        output(f'Watch out for a notification ...')
        CheatTutorial._show_hint(output)

    @staticmethod
    def _show_hint(output: CommonConsoleCommandOutput = None):
        try:
            hs = HotkeyStore()
            definitions = hs.definitions
            stats: Dict[int, float] = {}  # full_key_count, counter
            for full_key_code, key_definition in definitions.items():
                stats.update({full_key_code: key_definition.counter})
            sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
            full_key_code, _ = sorted_stats.pop()  # low/end
            _, max_value = sorted_stats.pop(0)  # high/1st
            max_value += 1  # Don't hint this hotkey for a while
            hs.register_key_press(full_key_code, set_counter_to=max_value)
            hs.register_hint_displayed(full_key_code)

            kd: KeyDefinition = hs.get_key_definition(full_key_code)
            description = kd.description

            SimpleUINotification().show(f'Hotkeys', f"Press '{kd}' to '{description}'")

            if CheatTutorial.show_hints and (kd.hint_counter == 2):
                if output:
                    output(f"Disabling auto-hints.")
                CheatTutorial.show_hints = False

        except Exception as e:
            if output:
                output(f"Error: {e}")
