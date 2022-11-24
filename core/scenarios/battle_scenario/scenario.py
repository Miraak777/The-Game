from random import choice

from core.enemies.enemies_table import get_enemy_table
from core.enemies import Enemy


from .situations import BattleSituation
from .texts import Text


class BattleScenario:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self._text = Text[self.main_menu.language]

    def start_battle(self, main_menu) -> None:
        self.main_menu.character_menu_button.setDisabled(True)

        enemy = self.spawn_enemy(self.main_menu.main_character.main_stats.LEVEL)

        BattleSituation(main_menu=self.main_menu, enemy=enemy)

    def spawn_enemy(self, character_level: int):
        enemy_table = [enemy_name for enemy_name, enemy_min_level in get_enemy_table().items() if
                       enemy_min_level <= character_level]
        enemy = Enemy(character_level, self.main_menu, choice(enemy_table))
        return enemy

