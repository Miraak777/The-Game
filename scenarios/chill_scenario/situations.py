from scenarios.base_situation.base_situation import BaseSituation


class ChillSituation(BaseSituation):
    def __init__(self, main_menu, battle_scenario, text) -> None:
        super().__init__(main_menu, text)
        self._game_menu.add_log(self._text.CHILL)
        self._battle_scenario = battle_scenario

    def _event_first_action(self) -> None:
        self._battle_scenario.start_battle()

    def _event_second_action(self) -> None:
        pass

    def _event_third_action(self) -> None:
        pass

    def _event_fourth_action(self) -> None:
        pass
