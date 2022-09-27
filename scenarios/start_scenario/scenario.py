from . import situations
from .texts import Text


class StartScenario:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.game_menu = main_menu.game_menu
        self._text = Text[self.main_menu.language]

        situations.ExampleSituation(main_menu)
