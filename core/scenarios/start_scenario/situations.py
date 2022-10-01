from core.scenarios import BaseSituation


class StartSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self._game_menu.add_log(self._text.INTRODUCTION, rows=3)
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        self._main_menu.battle_scenario.start_battle()

    def _event_second_action(self) -> None:
        self._main_menu.battle_scenario.start_battle()

    def _event_third_action(self) -> None:
        self._main_menu.battle_scenario.start_battle()

    def _event_fourth_action(self) -> None:
        self._main_menu.battle_scenario.start_battle()
