#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from typing import Union, Callable

from sims4communitylib.enums.common_key import CommonKey

"""
Extend this class with self.definition, self.callback, self.counter to have everything in one object
Simplify the store to store only {full_key_code: key_definition}

"""


class KeyDefinition:
    # Constants for hotkey modifiers
    MOD_ALT = 0x0001
    MOD_CONTROL = 0x0002
    MOD_SHIFT = 0x0004
    MOD_WIN = 0x0008
    """
    Define a key with shift/ctrl/alt/win pressed
    """

    def __init__(self, key_code: Union[CommonKey, int], shift: bool = False, ctrl: bool = False, alt: bool = False, win: bool = False,
                 callback: Callable = None, parameter: str = '', synchronized: bool = True,
                 description: str = '', counter: float = 0.0, hint_counter: int = 0):
        """
        _key_code = [KEY_0 ... KEY_Z]
        """
        self._key_code = int(key_code)
        self._shift = shift
        self._ctrl = ctrl
        self._alt = alt
        self._win = win

        _fs_modifiers = 0
        _full_key_code = int(key_code)
        if shift:
            _full_key_code += 2 ** 8
            _fs_modifiers = _fs_modifiers | KeyDefinition.MOD_SHIFT
        if ctrl:
            _full_key_code += 2 ** 9
            _fs_modifiers = _fs_modifiers | KeyDefinition.MOD_CONTROL
        if alt:
            _full_key_code += 2 ** 10
            _fs_modifiers = _fs_modifiers | KeyDefinition.MOD_ALT
        if win:
            _full_key_code += 2 ** 11
            _fs_modifiers = _fs_modifiers | KeyDefinition.MOD_WIN
        self._full_key_code = _full_key_code
        self._fs_modifiers = _fs_modifiers

        self._callback = callback
        self._parameter: str = parameter
        self._synchronized: bool = synchronized
        self._description = description
        self._counter: float = counter
        self._hint_counter: int = hint_counter

    @property
    def full_key_code(self) -> int:
        return self._full_key_code

    @property
    def key_code(self) -> int:
        return self._key_code

    @property
    def fs_modifiers(self) -> int:
        return self._fs_modifiers

    @property
    def callback(self) -> Callable:
        return self._callback

    @callback.setter
    def callback(self, callback: Callable):
        self._callback = callback

    @property
    def synchronized(self) -> bool:
        return self._synchronized

    @synchronized.setter
    def synchronized(self, synchronized: bool):
        self._synchronized = synchronized

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def counter(self) -> float:
        return self._counter

    @counter.setter
    def counter(self, counter: float):
        self._counter = counter

    @property
    def hint_counter(self) -> int:
        return self.hint_counter

    @hint_counter.setter
    def hint_counter(self, hint_counter: int):
        self.hint_counter = hint_counter

    @property
    def parameter(self) -> str:
        return self._parameter

    @parameter.setter
    def parameter(self, parameter: Callable):
        self._parameter = parameter

    def __repr__(self):
        rv = ''
        if self._shift:
            rv = f'Shift+'
        if self._ctrl:
            rv = f'{rv}Ctrl+'
        if self._alt:
            rv = f'{rv}Alt+'
        if self._win:
            rv = f'{rv}Win+'
        if CommonKey.KEY_0 <= self._key_code <= CommonKey.KEY_Z:
            rv = f'{rv}{chr(self._key_code)}'
        elif rv and self._key_code in (CommonKey.SHIFT, CommonKey.SHIFT_LEFT, CommonKey.SHIFT_RIGHT,
                                       CommonKey.CTRL, CommonKey.CTRL_LEFT, CommonKey.CTRL_RIGHT,
                                       CommonKey.ALT, CommonKey.ALT_LEFT, CommonKey.ALT_RIGHT,
                                       CommonKey.WINDOWS_LEFT, CommonKey.WINDOWS_RIGHT, CommonKey.APPLICATIONS):
            rv = rv[:-1]
        else:
            rv = f'{rv}_ ({self._key_code})'
        return rv

    def copy(self):
        kd = KeyDefinition(self._key_code, shift=self._shift, ctrl=self._ctrl, alt=self._alt, win=self._win,
                           callback=self._callback, parameter=self._parameter, description=self._description,
                           counter=self._counter, hint_counter=self._hint_counter)
        return kd
