#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from o19_hotkeys.modinfo import ModInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

try:
    from hk_move2.move import Move
except:
    pass

class CheatMoveSim:

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.hk.sim.select', 'Select active sim to move.'
    )
    def cheat_o19_hk_sim_select(output: CommonConsoleCommandOutput):
        sim_info = CommonSimUtils.get_active_sim_info()
        if Move().item == sim_info:
            sim_info = None
        output(f"Setting move object to '{sim_info}'")
        Move().item = sim_info
