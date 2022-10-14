from core.scenarios import BaseSituation


class StartSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self._game_menu.add_log(self._text.INTRODUCTION)
        self.refresh_buttons()
        self._log("")

    def _event_first_action(self) -> None:
        scenario = self._main_menu.random_scenario.get_random_scenario()
        scenario(self._main_menu)

    def _event_second_action(self) -> None:
        scenario = self._main_menu.random_scenario.get_random_scenario()
        scenario(self._main_menu)

    def _event_third_action(self) -> None:
        scenario = self._main_menu.random_scenario.get_random_scenario()
        scenario(self._main_menu)

    def _event_fourth_action(self) -> None:
        scenario = self._main_menu.random_scenario.get_random_scenario()
        scenario(self._main_menu)
