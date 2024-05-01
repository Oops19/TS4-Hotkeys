#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from typing import Dict, Set

from o19_hotkeys.hk.key_definition import KeyDefinition
from ts4lib.utils.singleton import Singleton


class HotkeyStore(object, metaclass=Singleton):
    """
    To be used only by KeyboardMain()
    """
    def __init__(self):
        self._key_codes: Set[int] = set()  # (full_key_code, ...) - All registered key_codes with Ctrl+Shift+Alt
        self._definitions: Dict[int, KeyDefinition] = {}  # {full_key_code: key_definition, ...

    @property
    def key_codes(self) -> Set[int]:
        return self._key_codes.copy()

    @property
    def definitions(self) -> Dict[int, KeyDefinition]:
        return self._definitions.copy()

    def contains(self, full_key_code: int) -> bool:
        if full_key_code in self._key_codes:
            return True
        else:
            return False

    def get_key_definition(self, full_key_code: int) -> KeyDefinition:
        return self._definitions.get(full_key_code).copy()

    def register_key(self, key_definition: KeyDefinition):
        """
        callback to the method which is registering the key.
        If the key combination already exists it will be replaced.
        """
        full_key_code = key_definition.full_key_code
        self._key_codes.add(full_key_code)
        self._definitions.update({full_key_code: key_definition})

    def un_register_key(self, key_definition: KeyDefinition):
        full_key_code = key_definition.full_key_code
        # noinspection PyBroadException
        try:
            self._key_codes.remove(full_key_code)
            self._definitions.pop(full_key_code)
        except:
            pass

    def register_key_press(self, full_key_code: int, set_counter_to: float = None):
        kd: KeyDefinition = self._definitions.get(full_key_code)
        if not kd:
            return
        if set_counter_to is None:
            counter = kd.counter + 1
        else:
            counter = set_counter_to
        kd.counter = counter

        self._definitions.update({full_key_code: kd})

    def register_hint_displayed(self, full_key_code: int, set_counter_to: float = None):
        kd: KeyDefinition = self._definitions.get(full_key_code)
        if not kd:
            return
        if set_counter_to is None:
            hint_counter = kd.hint_counter + 1
        else:
            hint_counter = set_counter_to
        kd.hint_counter = hint_counter

        self._definitions.update({full_key_code: kd})
