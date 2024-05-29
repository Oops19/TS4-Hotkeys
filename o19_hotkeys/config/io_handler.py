#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import ast
import os
from typing import Dict, List, Any

from o19_hotkeys.config.helper import ConfigHelper
from o19_hotkeys.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ConfigIOHandler')
log.enable()


class ConfigIOHandler:
    """
    Class to manage the configuration files
    """
    def __init__(self, ts4lib):
        self.ts4lib = ts4lib
        self.ch = ConfigHelper()

    def read_configuration_files(self, filename: str, cb_parser: Any = None) -> Dict:
        """
        Reads the configuration file
        :param filename: Default and User configuration files
        :param cb_parser: Callback method to process and/or parse the read configuration data.
        :return: The merged configuration
        """
        configuration: Dict = {}
        default_file = self.ch.get_configuration_file(filename)
        user_files = self.ch.get_user_configuration_files(filename)
        source_files: List = [default_file, *user_files]
        for source_file in source_files:
            if os.path.isfile(source_file):
                with open(source_file, 'rt', encoding='UTF-8') as fp:
                    log.debug(f"Reading configuration file '{source_file}'.")  # Full path logged!
                    # noinspection PyBroadException
                    try:
                        cfg = ast.literal_eval(fp.read())
                        if cb_parser:
                            cfg = cb_parser(cfg)
                        configuration.update(cfg)
                    except Exception as e:
                        log.error(f"Could not parse configuration file '{source_file}' ({e}).")  # Full path logged!
            else:
                log.warn(f"Configuration file '{source_file}' not found.")  # Full path logged!
        return configuration

    def read_configuration_file(self, filename: str, read_merged: bool = True) -> Dict:
        configuration = {}
        if read_merged:
            file = self.ch.get_merged_file(filename)
        else:
            file = self.ch.get_configuration_file(filename)
        if os.path.isfile(file):
            with open(file, 'rt', encoding='UTF-8') as fp:
                log.debug(f"Reading configuration file '{file}'.")  # Full path logged!
                # noinspection PyBroadException
                try:
                    a = fp.read()
                    configuration = ast.literal_eval(a)
                except Exception as e:
                    log.error(f"Could not parse configuration file '{file}' ({e}).")  # Full path logged!
        else:
            log.warn(f"Configuration file '{file}' not found.")  # Full path logged!
        return configuration
