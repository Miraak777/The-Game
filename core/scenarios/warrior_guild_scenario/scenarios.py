from . import situations
from .texts import Text


class WarriorGuildScenario:
    def __init__(self, main_menu):
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self._log = self._main_menu.game_menu.add_log
        self.main_character_weapon = None

        self.meet()

    def meet(self):
        situations.MeetSituation(self._main_menu, self._text, self)
