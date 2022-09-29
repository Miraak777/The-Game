from scenarios.base_situation.base_situation import BaseSituation
from core.constants.actions_constants import ActionButtons
from main_character.character import MainCharacter
from core.constants.character_constants import CommonConstants as cc


class BattleSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self._main_character: MainCharacter = main_menu.main_character
        predicted_attack_params = {
            cc.LIGHT_ATTACK: self._main_character.light_attack_prediction(),
            cc.MEDIUM_ATTACK: self._main_character.medium_attack_prediction(),
            cc.HEAVY_ATTACK: self._main_character.heavy_attack_prediction(),
        }
        self._texts = {
            ActionButtons.FIRST_ACTION: (self._text.FIRST_ACTION + " " +
                                         self._text.DAMAGE + str(predicted_attack_params[cc.LIGHT_ATTACK][cc.DAMAGE]) +
                                         " " + self._text.STAMINA_CONSUMPTION +
                                         str(predicted_attack_params[cc.LIGHT_ATTACK][cc.STAMINA_CONSUMPTION])),
            ActionButtons.SECOND_ACTION: (self._text.SECOND_ACTION + " " +
                                          self._text.DAMAGE + str(predicted_attack_params[cc.MEDIUM_ATTACK][cc.DAMAGE])
                                          + " " + self._text.STAMINA_CONSUMPTION +
                                          str(predicted_attack_params[cc.LIGHT_ATTACK][cc.STAMINA_CONSUMPTION])),
            ActionButtons.THIRD_ACTION: (self._text.THIRD_ACTION + " " +
                                         self._text.DAMAGE + str(predicted_attack_params[cc.HEAVY_ATTACK][cc.DAMAGE]) +
                                         " " + self._text.STAMINA_CONSUMPTION +
                                         str(predicted_attack_params[cc.LIGHT_ATTACK][cc.STAMINA_CONSUMPTION])),
            ActionButtons.FOURTH_ACTION: self._text.FOURTH_ACTION,
        }
        self._refresh_buttons()

    def _event_first_action(self) -> None:
        pass

    def _event_second_action(self) -> None:
        pass

    def _event_third_action(self) -> None:
        pass

    def _event_fourth_action(self) -> None:
        pass
