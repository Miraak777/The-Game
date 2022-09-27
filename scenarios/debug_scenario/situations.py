from core.constants.actions_constants import ActionButtons
from .texts import Text


class DebugSituation:
    def __init__(self, main_menu) -> None:
        self._main_menu = main_menu
        self._game_menu = main_menu.game_menu
        self._text = Text[self._main_menu.language]
        self._events = {
            ActionButtons.FIRST_ACTION: self._event_give_some_exp,
            ActionButtons.SECOND_ACTION: self._event_set_class_peasant,
            ActionButtons.THIRD_ACTION: self._event_set_class_warrior,
            ActionButtons.FOURTH_ACTION: self._event_set_class_assassin,
        }
        self._texts = {
            ActionButtons.FIRST_ACTION: self._text.FIRST_ACTION,
            ActionButtons.SECOND_ACTION: self._text.SECOND_ACTION,
            ActionButtons.THIRD_ACTION: self._text.THIRD_ACTION,
            ActionButtons.FOURTH_ACTION: self._text.FOURTH_ACTION,
        }
        self._game_menu.set_action_buttons(self._events, self._texts)

    def _event_give_some_exp(self) -> None:
        self._main_menu.main_character.send_experience(1000)
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_set_class_peasant(self) -> None:
        self._main_menu.main_character.set_class_peasant()
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_set_class_warrior(self) -> None:
        self._main_menu.main_character.set_class_warrior()
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_set_class_assassin(self) -> None:
        self._main_menu.main_character.set_class_assassin()
        self._main_menu.character_menu.set_actual_character_stats()

