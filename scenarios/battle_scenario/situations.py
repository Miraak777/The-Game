from scenarios.base_situation.base_situation import BaseSituation
from scenarios.chill_scenario.scenario import ChillScenario
from core.constants.actions_constants import ActionButtons
from main_character.character import MainCharacter
from core.constants.character_constants import CommonConstants as cc, CombatStatsNames as cs


class BattleSituation(BaseSituation):
    def __init__(self, main_menu, enemy, battle_scenario, text) -> None:
        super().__init__(main_menu, text)
        self._battle_scenario = battle_scenario
        self._main_character: MainCharacter = main_menu.main_character
        self._enemy = enemy
        predicted_attack_params = {
            cc.LIGHT_ATTACK: self._main_character.light_attack_prediction(),
            cc.MEDIUM_ATTACK: self._main_character.medium_attack_prediction(),
            cc.HEAVY_ATTACK: self._main_character.heavy_attack_prediction(),
        }
        self._texts = {
            ActionButtons.FIRST_ACTION: (self._text.FIRST_ACTION + " " + self._text.DAMAGE +
                                         str(predicted_attack_params[cc.LIGHT_ATTACK][cs.MIN_DAMAGE]) + " - " +
                                         str(predicted_attack_params[cc.LIGHT_ATTACK][cs.MAX_DAMAGE]) + "\n" +
                                         self._text.STAMINA_CONSUMPTION +
                                         str(predicted_attack_params[cc.LIGHT_ATTACK][cc.STAMINA_CONSUMPTION])),
            ActionButtons.SECOND_ACTION: (self._text.SECOND_ACTION + " " + self._text.DAMAGE +
                                          str(predicted_attack_params[cc.MEDIUM_ATTACK][cs.MIN_DAMAGE]) + " - " +
                                          str(predicted_attack_params[cc.MEDIUM_ATTACK][cs.MAX_DAMAGE]) + "\n" +
                                          self._text.STAMINA_CONSUMPTION +
                                          str(predicted_attack_params[cc.MEDIUM_ATTACK][cc.STAMINA_CONSUMPTION])),
            ActionButtons.THIRD_ACTION: (self._text.THIRD_ACTION + " " + self._text.DAMAGE +
                                         str(predicted_attack_params[cc.HEAVY_ATTACK][cs.MIN_DAMAGE]) + " - " +
                                         str(predicted_attack_params[cc.HEAVY_ATTACK][cs.MAX_DAMAGE]) + "\n" +
                                         self._text.STAMINA_CONSUMPTION +
                                         str(predicted_attack_params[cc.HEAVY_ATTACK][cc.STAMINA_CONSUMPTION])),
            ActionButtons.FOURTH_ACTION: self._text.FOURTH_ACTION,
        }
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        character_damage = self._main_character.attack(cc.LIGHT_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.is_dead:
            self._generate_reward()
            self._main_character.set_max_stamina()
            self._main_menu.character_menu_button.setDisabled(False)
            ChillScenario(self._main_menu, self._battle_scenario)
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_second_action(self) -> None:
        character_damage = self._main_character.attack(cc.MEDIUM_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.is_dead:
            self._generate_reward()
            self._main_character.set_max_stamina()
            self._main_menu.character_menu_button.setDisabled(False)
            ChillScenario(self._main_menu, self._battle_scenario)
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_third_action(self) -> None:
        character_damage = self._main_character.attack(cc.HEAVY_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.is_dead:
            self._generate_reward()
            self._main_character.set_max_stamina()
            self._main_menu.character_menu_button.setDisabled(False)
            ChillScenario(self._main_menu, self._battle_scenario)
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_fourth_action(self) -> None:
        self._main_character.set_max_stamina()
        self._main_menu.character_menu_button.setDisabled(False)
        ChillScenario(self._main_menu, self._battle_scenario)

    def _generate_reward(self):
        self._main_character.send_experience(50 * self._enemy.level)

