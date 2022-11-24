from . import situations
from .texts import Text


class DeathScenario:
    def __init__(self, main_menu) -> None:
        self.main_menu = main_menu
        self.game_menu = main_menu.game_menu
        self._text = Text[self.main_menu.language]

        situations.DeathSituation(main_menu=self.main_menu, text=self._text)
