#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from ts4lib.utils.singleton import Singleton


class GamepadState(metaclass=Singleton):
    def __init__(self):
        self._enabled = False
        self._manager = None  # GamepadManager
        self._gamepad_id = 0
        self._poll_delay = 0.03  # Wait n seconds before polling the gamepad again. Lower this value to poll more often. Polling itself also takes some time. FPS games may poll with 144 Hz or more.
        self._button_repeat_rate = 0.5  # Wait n seconds before sending another 'keyDown' event is a button is held down. Pressing a button faster is possible to send more 'keyDown' notifications.
        self._verbose_log = True  # Write logs, this will delay all input!

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, do_enable: bool):
        self._enabled = bool(do_enable)

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, gamepad_maanger):
        self._manager = gamepad_maanger

    @property
    def gamepad_id(self) -> int:
        return self._gamepad_id

    @gamepad_id.setter
    def gamepad_id(self, gp_id: int):
        self._gamepad_id = int(gp_id)

    @property
    def poll_delay(self) -> float:
        return self._poll_delay

    @poll_delay.setter
    def poll_delay(self, execution_delay: float):
        self._poll_delay = float(execution_delay)

    @property
    def button_repeat_rate(self) -> float:
        return self._button_repeat_rate

    @button_repeat_rate.setter
    def button_repeat_rate(self, repeat_rate: float):
        self._button_repeat_rate = float(repeat_rate)

    @property
    def verbose_log(self) -> float:
        return self._verbose_log

    @verbose_log.setter
    def verbose_log(self, enabled: bool):
        self._verbose_log = bool(enabled)


GamepadState()
