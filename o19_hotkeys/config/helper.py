#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import os
import re
from typing import Dict, List

from o19_hotkeys.modinfo import ModInfo
from ts4lib.libraries.file_utils import FileUtils
from ts4lib.libraries.ts4folders import TS4Folders

try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ConfigHelper')
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(ModInfo.get_identity().name, 'ConfigHelper', custom_file_path=None)


class ConfigHelper:
    def __init__(self):
        self.ts4f = TS4Folders(ModInfo.get_identity().base_namespace)
        self.ts4fu = FileUtils(self.ts4f.ts4_folder_mods)

    def get_configuration_file(self, filename: str) -> str:
        return os.path.join(self.ts4f.data_folder, f"{filename}.txt")

    def get_user_configuration_files(self, filename: str) -> List[str]:
        r'''
        files: List[str] = []
        filenames = self.ts4fu.find_files(rf'^{filename}\..*\.txt')
        for _filename in filenames:
            files.append(_filename)
        return files
        '''
        return self.ts4fu.find_files(rf'^{filename}\..*\.txt')

    def get_user_configuration_file(self, filename: str):
        author = ''
        author_file = self.get_author_file()
        if os.path.isfile(author_file):
            # noinspection PyBroadException
            try:
                with open(author_file, 'rt', encoding='UTF-8') as fp:
                    author = fp.read()
                    author = re.sub(r'[^a-zA-Z0-9_]', '', author)
                    author = re.sub(r'(^_*|_*$)', '', author)
                    author = author[0:8]
            except:
                author = ''
        if author == '':
            author = 'anonymous'
        return os.path.join(self.ts4f.data_folder, f"{filename}.{author}.txt")

    def get_merged_file(self, filename: str):
        return os.path.join(self.ts4f.data_folder, f"_{filename}.bin")

    def get_author_file(self):
        return os.path.join(self.ts4f.data_folder, f"author.txt")

    @staticmethod
    def add_author_simple(data: Dict) -> Dict:
        rv: Dict = {}
        for author, _data in data.items():
            for k, v in _data.items():
                rv.update({f"{author}:{k}": v})
        return rv

    @staticmethod
    def add_author(data: Dict) -> Dict:
        rv: Dict = {}
        for author, outfit_configurations in data.items():
            new_outfit_configurations = {}
            for group_name, group_definitions in outfit_configurations.items():
                new_group_definitions = {}
                for _id, outfit_definitions in group_definitions.items():
                    for outfit_name, outfit_values in outfit_definitions.items():
                        if ':' in group_name:
                            new_group_definitions.update({outfit_name: outfit_values})
                        else:
                            new_group_definitions.update({f"{author}:{outfit_name}": outfit_values})
                    new_outfit_configurations.update({_id: new_group_definitions})

                if ':' in group_name:
                    rv.update({group_name: new_outfit_configurations})
                else:
                    rv.update({f"{author}:{group_name}": new_outfit_configurations})
        return rv
