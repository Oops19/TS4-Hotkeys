#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from hotkeys.gp.enums.gamepad_constants import GamepadConstants
from hotkeys.t.gamepad_thread import GamepadThread
from hotkeys.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton
try:
    from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'GamepadManager')
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(ModInfo.get_identity().name, 'GamepadManager', custom_file_path=None)
log.enable()

try:
    from hk_move.translate_keys import TranslateKeys
    from hk_move.move import Move
    hk_move_found = True
except:
    hk_move_found = False

class GamepadManager(metaclass=Singleton):
    _gamepad_thread = None
    triggers_move_or_rotate = True  # True=Move, False=Rotate
    translate_keys = None

    def __init__(self):
        if hk_move_found is False:
            log.warn(f"HotkeyBindings not found. >> Gamepad support disabled!")
            return

        # Start the Keyboard thread
        GamepadManager._gamepad_thread = GamepadThread(GamepadManager._gamepad_callback)
        GamepadManager._gamepad_thread.start_thread()

        GamepadManager.translate_keys = TranslateKeys()
        log.debug(f"started")

    @staticmethod
    def _gamepad_callback(event, key_down: bool = None):
        try:
            log.debug(f"{event} {key_down}")
            if key_down is None:
                stick, _x, _y, _z = event.split(' ', 3)
                if stick == 'stick_l':
                    # Rotation
                    if GamepadManager.triggers_move_or_rotate is True:
                        _y = 0  # Triggers modify movement, ignore their value.
                    GamepadManager.translate_keys.move_gp(f"_rotate", float(_x) * 90, float(_y) * 90, float(_z) * 90)

                else:  # stick == 'stick_r':
                    if GamepadManager.triggers_move_or_rotate is False:
                        _y = 0  # Triggers modify rotation, ignore their value.
                    GamepadManager.translate_keys.move_gp(f"_move_rel", float(_x), float(_y), float(_z))

            elif key_down is True:
                if event & GamepadConstants.BUTTON_LEFT_SHOULDER:
                    """ Triggers modify rotation """
                    GamepadManager.triggers_move_or_rotate = False
                elif event & GamepadConstants.BUTTON_RIGHT_SHOULDER:
                    """ Triggers modify movement """
                    GamepadManager.triggers_move_or_rotate = True
                elif (event & GamepadConstants.BUTTON_DPAD_UP) or (event & GamepadConstants.BUTTON_DPAD_DOWN) or (event & GamepadConstants.BUTTON_DPAD_LEFT) or (event & GamepadConstants.BUTTON_DPAD_RIGHT):
                    y = 0
                    if event & GamepadConstants.BUTTON_DPAD_RIGHT:
                        x = 2.5
                    elif event & GamepadConstants.BUTTON_DPAD_LEFT:
                        x = -2.5
                    else:
                        x = 0
                    if event & GamepadConstants.BUTTON_DPAD_UP:
                        z = -2.5
                    elif event & GamepadConstants.BUTTON_DPAD_DOWN:
                        z = 2.5
                    else:
                        z = 0
                    GamepadManager.translate_keys.move_gp(f"go_to", x, y, z)
        except:
            log.debug(event)


if __name__ == '__main__':
    import os
    import time
    os.environ["log_to_stdout"] = "1"
    gm = GamepadManager()
    time.sleep(120)
