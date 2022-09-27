from core.constants.actions_constants import ActionButtons
from .texts import Text


class StartSituation:
    def __init__(self, main_menu) -> None:
        self._main_menu = main_menu
        self._game_menu = main_menu.game_menu
        self._text = Text[main_menu.language]
        self._events = {
            ActionButtons.FIRST_ACTION: self._event_doing_nothing,
            ActionButtons.SECOND_ACTION: self._event_doing_nothing,
            ActionButtons.THIRD_ACTION: self._event_doing_nothing,
            ActionButtons.FOURTH_ACTION: self._event_doing_nothing,
        }
        self._texts = {
            ActionButtons.FIRST_ACTION: self._text.FIRST_ACTION,
            ActionButtons.SECOND_ACTION: self._text.SECOND_ACTION,
            ActionButtons.THIRD_ACTION: self._text.THIRD_ACTION,
            ActionButtons.FOURTH_ACTION: self._text.FOURTH_ACTION,
        }
        self._game_menu.add_log(self._text.INTRODUCTION, rows=3)
        self._game_menu.set_action_buttons(self._events, self._texts)

    def _event_doing_nothing(self) -> None:
        pass
