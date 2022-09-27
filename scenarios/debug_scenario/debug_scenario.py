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
            ActionButtons.FIRST_ACTION: self._text.GET_1000_XP,
            ActionButtons.SECOND_ACTION: self._text.BECOME_PEASANT,
            ActionButtons.THIRD_ACTION: self._text.BECOME_WARRIOR,
            ActionButtons.FOURTH_ACTION: self._text.BECOME_ASSASSIN,
        }
        self._game_menu.set_action_buttons(self._events, self._texts)

    def _event_give_some_exp(self) -> None:
        self._game_menu.add_log(text="Gained 1000 xp!")
        self._main_menu.main_character.send_experience(1000, self._main_menu)
        self._main_menu.character_menu.set_actual_character_stats()
        self._game_menu.scroll_down()

    def _event_set_class_peasant(self) -> None:
        self._game_menu.add_log(text="You're now Peasant!")
        self._main_menu.main_character.set_class_peasant()
        self._main_menu.character_menu.set_actual_character_stats()
        self._game_menu.scroll_down()

    def _event_set_class_warrior(self) -> None:
        self._game_menu.add_log(text="You're now Warrior!")
        self._main_menu.main_character.set_class_warrior()
        self._main_menu.character_menu.set_actual_character_stats()
        self._game_menu.scroll_down()

    def _event_set_class_assassin(self) -> None:
        self._game_menu.add_log(text="You're now Assassin!")
        self._main_menu.main_character.set_class_assassin()
        self._main_menu.character_menu.set_actual_character_stats()
        self._game_menu.scroll_down()

