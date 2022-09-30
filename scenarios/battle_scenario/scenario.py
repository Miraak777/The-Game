from random import randrange

from enemies.enemies_map import enemies_map
from interface.game_menu.game_menu import GameMenu

from .situations import BattleSituation
from .texts import Text


class BattleScenario:
    def __init__(self, main_menu):
        self.main_menu = main_menu
        self.game_menu: GameMenu = main_menu.game_menu
        self._text = Text[self.main_menu.language]

    def start_battle(self):
        self.main_menu.character_menu_button.setDisabled(True)
        enemy = enemies_map[randrange(0, 3)](
            self.main_menu.main_character.main_stats.LEVEL,
            self.main_menu,
            self.main_menu.language,
        )

        self.game_menu.add_log(
            self._text.BATTLE_START
            + " "
            + enemy.stats.NAME
            + " "
            + str(enemy.stats.LEVEL)
            + " "
            + self._text.LEVEL
            + " "
            + self._text.HEALTH
            + str(enemy.stats.MAX_HEALTH)
            + "/"
            + str(enemy.stats.HEALTH)
        )
        BattleSituation(main_menu=self.main_menu, enemy=enemy, text=self._text)
