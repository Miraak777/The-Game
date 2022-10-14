from random import randrange

from core.enemies.enemies_map import enemies_1_lvl, enemies_3_lvl, enemies_5_lvl, enemies_10_lvl

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

    def spawn_enemy(self, character_level):
        if character_level < 3:
            enemy_map = enemies_1_lvl
        if character_level >= 3:
            enemy_map = enemies_3_lvl
        if character_level >= 5:
            enemy_map = enemies_5_lvl
        if character_level >= 10:
            enemy_map = enemies_10_lvl
        enemy = enemy_map[randrange(0, len(enemy_map))](
            level=character_level,
            main_menu=self.main_menu,
        )
        return enemy
