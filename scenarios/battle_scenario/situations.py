from scenarios.base_situation.base_situation import BaseSituation


class BattleSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)

    def _event_first_action(self) -> None:
        pass

    def _event_second_action(self) -> None:
        pass

    def _event_third_action(self) -> None:
        pass

    def _event_fourth_action(self) -> None:
        pass
