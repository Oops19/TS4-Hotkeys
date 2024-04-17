#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


import importlib
import random
from typing import Dict, Union, List

from hotkeys.config.config_reader import ConfigReader
from hotkeys.gp.gamepad_manager import GamepadManager
from hotkeys.gp.gamepad_state import GamepadState
from hotkeys.hk.hotkey_store import HotkeyStore
from hotkeys.hk.key_definition import KeyDefinition
from sims4communitylib.enums.common_key import CommonKey
from ts4lib.utils.singleton import Singleton
from hotkeys.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'HotkeyReader')
log.enable()


class HotkeyReader(object, metaclass=Singleton):
    UNREGISTER = 'remove'

    def read_configuration(self) -> int:
        num_registered_keys = 0
        enable_hotkey = True
        enable_gamepad = True
        try:
            hk_store = HotkeyStore()
            cr = ConfigReader()
            cfg = cr.read_configuration({'hotkeys': None, })
            parsed_cfg: Dict[str, Union[List[str, str, bool, int], Dict[str, Union[str, int, float]]]] = {}
            hotkey_definition: Union[List[str, str, bool, int], Dict[str, Union[str, int, float]]] = []
            # parsed_cfg = {}
            for _, config_data in cfg.items():
                for author, hotkey_data in config_data.items():
                    for hotkey, hotkey_definition in hotkey_data.items():
                        parsed_cfg.update({hotkey: hotkey_definition})

            log.debug(f"Final configuration: {parsed_cfg}")

            gs = GamepadState()
            for hotkey, hotkey_definition in parsed_cfg.items():
                try:
                    if hotkey == 'Configuration':
                        hdd: Dict[str, Union[str, int, float]] = hotkey_definition
                        for key, value in hdd.items():
                            if isinstance(value, bool) and value is False:
                                if key == 'Hotkeys':
                                    enable_hotkey = False
                                elif key == 'Gamepad':
                                    enable_gamepad = False
                            elif isinstance(value, float) or isinstance(value, int):
                                if key == 'GamepadId':
                                    gs.gamepad_id = value
                                if key == 'GamepadPollDelay':
                                    gs.poll_delay = value
                                elif key == 'GamepadButtonRepeatRate':
                                    gs.button_repeat_rate = value
                        continue

                    shift = True if 'Shift+' in hotkey else False
                    ctrl = True if 'Ctrl+' in hotkey else False
                    alt = True if 'Alt+' in hotkey else False
                    key = hotkey[-1:]
                    key_code = ord(key)
                    kd = KeyDefinition(key_code, shift=shift, ctrl=ctrl, alt=alt)
                    if CommonKey.KEY_0 <= key_code <= CommonKey.KEY_Z:
                        hdl: List[str, str, bool, int] = hotkey_definition
                        callback_parameter = hdl.pop(0) if hdl else ''
                        callback_parameter: str = str(callback_parameter)
                        description = hdl.pop(0) if hdl else callback_parameter
                        synchronized = bool(hdl.pop(0)) if hdl else False
                        order = int(hdl.pop(0)) if hdl else 0
                        # log.debug(f"{callback_parameter}")
                        # log.debug(f"{description}")
                        # log.debug(f"{synchronized}")
                        # log.debug(f"{order}")
                        if not callback_parameter:
                            log.debug(f"Can't register hotkey '{hotkey}' with empty callback.")
                            continue
                        if callback_parameter == HotkeyReader.UNREGISTER:
                            print(f"Un-Registering {kd}")
                            hk_store.un_register_key(kd)
                            num_registered_keys -= 1
                            continue
                        if callback_parameter == 'EXIT':
                            callback = 'EXIT'
                            parameter = ''
                        else:
                            callback, _, parameter = callback_parameter.partition(' ')
                            _class_string, _function_name = callback.rsplit('.', 1)
                            _module_name, _class_name = _class_string.rsplit('.', 1)
                            _class = getattr(importlib.import_module(_module_name), _class_name)
                            callback = getattr(_class, _function_name)
                            parameter = parameter.strip()

                        print(f"Registering {kd} -> '{callback_parameter}' ({description}) {synchronized}")
                        kd.callback = callback
                        kd.parameter = parameter
                        kd.synchronized = synchronized
                        kd.description = description
                        kd.counter = random.random()  # Make sure that a random hint key is displayed after one hour.
                        hk_store.register_key(kd)
                        num_registered_keys += 1
                    else:
                        log.debug(f"Can't register hotkey '{hotkey}' with key code '{key_code}'.")
                except Exception as e:
                    log.error(f"Couldn't parse {hotkey} -> {hotkey_definition} ({e}")
        except Exception as e:
            log.error(f"Error {e}")
        if enable_gamepad:
            GamepadState().enabled = True
            GamepadState().manager = GamepadManager()
        if enable_hotkey:
            return num_registered_keys
        else:
            return 0
