from core.scenarios import BaseSituation


class DeathSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self.refresh_buttons()
        self._log("")

    def _event_first_action(self) -> None:
        self._main_menu.exit()

    def _event_second_action(self) -> None:
        pass

    def _event_third_action(self) -> None:
        pass

    def _event_fourth_action(self) -> None:
        pass
