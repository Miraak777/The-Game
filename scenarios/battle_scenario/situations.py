from core.constants.actions_constants import ActionButtons
from core.constants.character_constants import CombatStatsNames as cs
from core.constants.character_constants import CommonConstants as cc
from main_character.character import MainCharacter
from scenarios.base_situation.base_situation import BaseSituation
from scenarios.chill_scenario.scenario import ChillScenario


class BattleSituation(BaseSituation):
    def __init__(self, main_menu, enemy, text) -> None:
        super().__init__(main_menu, text)
        self._main_character: MainCharacter = main_menu.main_character
        self._enemy = enemy
        predicted_attack_params = {
            cc.LIGHT_ATTACK: self._main_character.light_attack_prediction(),
            cc.MEDIUM_ATTACK: self._main_character.medium_attack_prediction(),
            cc.HEAVY_ATTACK: self._main_character.heavy_attack_prediction(),
        }
        self._texts = {
            ActionButtons.FIRST_ACTION: (
                self._text.FIRST_ACTION
                + " "
                + self._text.DAMAGE
                + str(predicted_attack_params[cc.LIGHT_ATTACK][cs.MIN_DAMAGE])
                + " - "
                + str(predicted_attack_params[cc.LIGHT_ATTACK][cs.MAX_DAMAGE])
                + "\n"
                + self._text.STAMINA_CONSUMPTION
                + str(predicted_attack_params[cc.LIGHT_ATTACK][cc.STAMINA_CONSUMPTION])
            ),
            ActionButtons.SECOND_ACTION: (
                self._text.SECOND_ACTION
                + " "
                + self._text.DAMAGE
                + str(predicted_attack_params[cc.MEDIUM_ATTACK][cs.MIN_DAMAGE])
                + " - "
                + str(predicted_attack_params[cc.MEDIUM_ATTACK][cs.MAX_DAMAGE])
                + "\n"
                + self._text.STAMINA_CONSUMPTION
                + str(predicted_attack_params[cc.MEDIUM_ATTACK][cc.STAMINA_CONSUMPTION])
            ),
            ActionButtons.THIRD_ACTION: (
                self._text.THIRD_ACTION
                + " "
                + self._text.DAMAGE
                + str(predicted_attack_params[cc.HEAVY_ATTACK][cs.MIN_DAMAGE])
                + " - "
                + str(predicted_attack_params[cc.HEAVY_ATTACK][cs.MAX_DAMAGE])
                + "\n"
                + self._text.STAMINA_CONSUMPTION
                + str(predicted_attack_params[cc.HEAVY_ATTACK][cc.STAMINA_CONSUMPTION])
            ),
            ActionButtons.FOURTH_ACTION: self._text.FOURTH_ACTION,
        }
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        character_damage = self._main_character.attack(cc.LIGHT_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.stats.IS_DEAD:
            self._main_character.set_max_stamina()
            self._main_menu.character_menu_button.setDisabled(False)
            self._generate_reward()
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_second_action(self) -> None:
        character_damage = self._main_character.attack(cc.MEDIUM_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.stats.IS_DEAD:
            self._main_character.set_max_stamina()
            self._main_menu.character_menu_button.setDisabled(False)
            self._generate_reward()
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_third_action(self) -> None:
        character_damage = self._main_character.attack(cc.HEAVY_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.stats.IS_DEAD:
            self._main_character.set_max_stamina()
            self._main_menu.character_menu_button.setDisabled(False)
            self._generate_reward()
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_fourth_action(self) -> None:
        self._main_character.set_max_stamina()
        self._main_menu.character_menu_button.setDisabled(False)
        ChillScenario(self._main_menu)

    def _generate_reward(self):
        self._main_character.send_experience(self._enemy.stats.EXPERIENCE_GAINED)
        reward = self._enemy.drops.drop_items()
        if reward:
            reward_level = self._enemy.stats.LEVEL
            RewardGetSituation(self._main_menu, self._text, [reward, reward_level])
        else:
            ChillScenario(self._main_menu)


class RewardGetSituation(BaseSituation):
    def __init__(self, main_menu, text, reward):
        super().__init__(main_menu, text)
        self._reward = reward
        self._reward[0] = self._reward[0][0](level=self._reward[1], main_menu=main_menu)
        self._texts = {
            ActionButtons.FIRST_ACTION: self._text.EQUIP_WEAPON,
            ActionButtons.SECOND_ACTION: self._text.QUIT_WEAPON,
            ActionButtons.THIRD_ACTION: "",
            ActionButtons.FOURTH_ACTION: "",
        }
        self._log(
            self._text.YOU_FOUNDED
            + self._reward[0].stats.NAME
            + " "
            + str(self._reward[0].stats.LEVEL)
            + " "
            + self._text.LEVEL
        )
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        self._log(self._text.YOU_EQUIPPED + self._reward[0].stats.NAME)
        self._main_menu.main_character.equip_weapon(self._reward[0])
        ChillScenario(self._main_menu)

    def _event_second_action(self) -> None:
        self._log(self._text.YOU_QUITED + self._reward[0].stats.NAME)
        ChillScenario(self._main_menu)
