from core.constants.actions_constants import ActionButtons
from core.constants.character_constants import BarsNames as bn
from core.constants.character_constants import CombatStatsNames as cs
from core.constants.character_constants import CommonConstants as cc
from core.constants.item_constants import ItemTypes
from core.main_character.character import MainCharacter
from core.scenarios import BaseSituation
from core.scenarios.chill_scenario.scenario import ChillScenario

from .texts import Text


class BattleSituation(BaseSituation):
    def __init__(self, main_menu, enemy) -> None:
        text = Text[main_menu.language]
        super().__init__(main_menu, text)
        self._main_menu.character_menu.hide()
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
        self._game_menu.add_log(
            self._text.BATTLE_START + " " + enemy.name + " " + str(enemy.level) + " " + self._text.LEVEL
        )
        self._game_menu.refresh_enemy_bar(enemy)
        self._log("")

    def _event_first_action(self) -> None:
        self._log("")
        character_damage = self._main_character.attack(cc.LIGHT_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.is_dead:
            self._main_character.set_max_stamina()
            self._game_menu.refresh_character_bars()
            self._main_menu.character_menu_button.setDisabled(False)
            self._generate_reward()
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_second_action(self) -> None:
        self._log("")
        character_damage = self._main_character.attack(cc.MEDIUM_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.is_dead:
            self._main_character.set_max_stamina()
            self._main_menu.character_menu_button.setDisabled(False)
            self._generate_reward()
        else:
            enemy_damage = self._enemy.attack()
            self._main_character.take_damage(enemy_damage)

    def _event_third_action(self) -> None:
        self._log("")
        character_damage = self._main_character.attack(cc.HEAVY_ATTACK)
        self._enemy.take_damage(character_damage)
        if self._enemy.is_dead:
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

    def _generate_reward(self) -> None:
        self._main_character.send_experience(self._enemy.experience_gained)
        reward = self._enemy.calculate_drop()
        for item in reward:
            if item.item_type == ItemTypes.WEAPON:
                self._log(f"{self._text.YOU_FOUNDED} {item.name} {item.level} {self._text.LEVEL}")
            else:
                self._log(f"{self._text.YOU_FOUNDED} {item.name}")
            self._main_menu.inventory_menu.add_item(item)
        ChillScenario(self._main_menu)
