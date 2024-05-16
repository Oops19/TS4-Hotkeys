#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Dict

from o19_hotkeys.config.io_handler import ConfigIOHandler
from o19_hotkeys.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton
from ts4lib.libraries.ts4folders import TS4Folders

try:
    from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ConfigReader')
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(ModInfo.get_identity().name, 'ConfigReader', custom_file_path=None)
log.enable()
log.info(f"Starting ...")


class ConfigReader(object, metaclass=Singleton):

    def __init__(self):
        self.ts4f = TS4Folders(ModInfo.get_identity().base_namespace)
        self.cioh = ConfigIOHandler(self.ts4f)

    def read_configuration(self, configurations: Dict) -> Dict:
        """
        Merge all configuration files into one file.
        Merge "{'author': {'description': ..." into "{'author:description': ...
        Don't parse any values
        :return:
        """
        rv = {}
        try:
            x = {'hotkeys': None, }
            for configuration_filename, callback_parser in x.items():
                _cfg: Dict = self.cioh.read_configuration_files(configuration_filename, callback_parser)
                rv.update({configuration_filename: _cfg})
        except Exception as e:
            log.error(f"Could not read configuration files ({e}).", throw=True)
        return rv
