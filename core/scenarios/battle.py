from core.constants.character_constants import CommonConstants as ccc
from core.constants.character_constants import CombatStatsNames as cs
from .texts import Text


class Battle:
    def __init__(self, main_menu, enemy, next_event=None) -> None:
        self.main_menu = main_menu
        self.enemy = enemy
        self.next_event = next_event
        self.game_menu = main_menu.game_menu
        self.main_character = main_menu.main_character
        self.log = self.game_menu.add_log
        self.text = Text[self.main_menu.language]

        self.main_menu.inventory_menu.setDisabled(True)
        self.main_menu.character_menu.hide()

        self.predicted_attacks = {
            ccc.LIGHT_ATTACK: self.main_character.light_attack_prediction(),
            ccc.MEDIUM_ATTACK: self.main_character.medium_attack_prediction(),
            ccc.HEAVY_ATTACK: self.main_character.heavy_attack_prediction(),
        }

        self.actions = [self._event_attack,
                        self._event_attack,
                        self._event_attack,
                        self._event_escape]
        self.texts = [
            (f"{self.text.LIGHT_ATTACK} {self.text.DAMAGE}: {self.predicted_attacks[ccc.LIGHT_ATTACK][cs.MIN_DAMAGE]} -"
             f" {self.predicted_attacks[ccc.LIGHT_ATTACK][cs.MAX_DAMAGE]}\n{self.text.STAMINA_CONSUMPTION}: "
             f"{self.predicted_attacks[ccc.LIGHT_ATTACK][ccc.STAMINA_CONSUMPTION]}"),
            (f"{self.text.MEDIUM_ATTACK} {self.text.DAMAGE}: {self.predicted_attacks[ccc.MEDIUM_ATTACK][cs.MIN_DAMAGE]} -"
             f" {self.predicted_attacks[ccc.MEDIUM_ATTACK][cs.MAX_DAMAGE]}\n{self.text.STAMINA_CONSUMPTION}: "
             f"{self.predicted_attacks[ccc.MEDIUM_ATTACK][ccc.STAMINA_CONSUMPTION]}"),
            (f"{self.text.HEAVY_ATTACK} {self.text.DAMAGE}: {self.predicted_attacks[ccc.HEAVY_ATTACK][cs.MIN_DAMAGE]} -"
             f" {self.predicted_attacks[ccc.HEAVY_ATTACK][cs.MAX_DAMAGE]}\n{self.text.STAMINA_CONSUMPTION}: "
             f"{self.predicted_attacks[ccc.HEAVY_ATTACK][ccc.STAMINA_CONSUMPTION]}"),
            self.text.ESCAPE,
        ]
        self.game_menu.refresh_enemy_bar(self.enemy)
        self.game_menu.set_action_buttons(self.actions, self.texts)

    def generate_reward(self) -> None:
        reward = self.enemy.calculate_drop()
        for item in reward:
            self.log(f"{self.text.YOU_FOUNDED} {item.name}")
            self.main_menu.inventory_menu.add_item(item)
        self.main_character.send_experience(self.enemy.experience_gained)
        if self.next_event:
            self.next_event.run_event()
        self.main_menu.chill_event.run_event()

    def _event_attack(self, action_number: int) -> None:
        attacks_map = {
            0: ccc.LIGHT_ATTACK,
            1: ccc.MEDIUM_ATTACK,
            2: ccc.HEAVY_ATTACK
        }
        character_damage = self.main_character.attack(attacks_map[action_number])
        self.enemy.take_damage(character_damage)
        if self.enemy.is_dead:
            self.main_character.set_max_stamina()
            self.game_menu.refresh_character_bars()
            self.main_menu.character_menu_button.setDisabled(False)
            self.main_menu.inventory_menu.setDisabled(False)
            self.generate_reward()
        else:
            enemy_damage = self.enemy.attack()
            self.main_character.take_damage(enemy_damage)

    def _event_escape(self, action_number: int) -> None:
        self.main_menu.character_menu_button.setDisabled(False)
        self.main_menu.inventory_menu.setDisabled(False)
        self.main_character.set_max_stamina()
        self.main_menu.chill_event.run_event()
