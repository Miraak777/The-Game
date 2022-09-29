from scenarios.base_situation.base_situation import BaseSituation


class DebugSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        self._main_menu.main_character.send_experience(1000)
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_second_action(self) -> None:
        self._main_menu.main_character.set_class_peasant()
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_third_action(self) -> None:
        self._main_menu.main_character.set_class_warrior()
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_fourth_action(self) -> None:
        self._main_menu.main_character.set_class_assassin()
        self._main_menu.character_menu.set_actual_character_stats()

