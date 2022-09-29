from scenarios.base_situation.base_situation import BaseSituation


class StartSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self._game_menu.add_log(self._text.INTRODUCTION, rows=3)
