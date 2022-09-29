from core.constants.actions_constants import ActionButtons
from .texts import EnglishText


class BaseSituation:
    def __init__(self, main_menu, text=EnglishText) -> None:
        self._main_menu = main_menu
        self._game_menu = main_menu.game_menu
        self._text = text
        self._events = {
            ActionButtons.FIRST_ACTION: self._event_first_action,
            ActionButtons.SECOND_ACTION: self._event_second_action,
            ActionButtons.THIRD_ACTION: self._event_third_action,
            ActionButtons.FOURTH_ACTION: self._event_fourth_action,
        }
        self._texts = {
            ActionButtons.FIRST_ACTION: self._text.FIRST_ACTION,
            ActionButtons.SECOND_ACTION: self._text.SECOND_ACTION,
            ActionButtons.THIRD_ACTION: self._text.THIRD_ACTION,
            ActionButtons.FOURTH_ACTION: self._text.FOURTH_ACTION,
        }
        self._refresh_buttons()

    def _refresh_buttons(self):
        self._game_menu.set_action_buttons(self._events, self._texts)

    def _event_first_action(self) -> None:
        pass

    def _event_second_action(self) -> None:
        pass

    def _event_third_action(self) -> None:
        pass

    def _event_fourth_action(self) -> None:
        pass
