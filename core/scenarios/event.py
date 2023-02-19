from .constants import ScenarioStats as ss
from .battle import Battle
from .texts import Text
from core.enemies.enemy import Enemy
from core.items import Weapon


class Event:
    def __init__(self, main_menu, stats) -> None:
        self.main_menu = main_menu
        self.game_menu = main_menu.game_menu
        self.log = self.game_menu.add_log
        self.text = stats[ss.TEXTS][self.main_menu.language]
        self.action_stats_map = {
            0: stats[ss.ACTIONS][ss.ACTION_1],
            1: stats[ss.ACTIONS][ss.ACTION_2],
            2: stats[ss.ACTIONS][ss.ACTION_3],
            3: stats[ss.ACTIONS][ss.ACTION_4],
        }
        self.action_type_map = {
            ss.DIALOG: self.dialog_action,
            ss.LEAVE: self.leave_action,
            ss.BATTLE: self.battle_action,
            ss.REWARD: self.reward_action,
            ss.RANDOM: self.random_action,
        }
        self.texts = [self.action_stats_map[i][ss.ACTION_NAMES][self.main_menu.language] if
                      self.action_stats_map[i] else "" for i in range(4)]
        self.next_events = [self.action_stats_map[i][ss.NEXT_EVENT] if self.action_stats_map[i] else None for i in
                            range(4)]
        self.actions = [self.action_type_map[self.action_stats_map[i][ss.ACTION_TYPE]] if self.action_stats_map[i]
                        else self._no_action for i in range(4)]
        self.action_enemies = [
            self.action_stats_map[i][ss.ENEMY_INFO] if self.actions[i] == self.battle_action else None for i in range(4)
        ]

    def run_event(self) -> None:
        self.log(self.text)
        self.game_menu.set_action_buttons(self.actions, self.texts)

    def _no_action(self, action_number: int) -> None:
        pass

    def dialog_action(self, action_number: int) -> None:
        self.log(self.action_stats_map[action_number][ss.TEXTS][self.main_menu.language])
        self.next_events[action_number].run_event()

    def leave_action(self, action_number: int) -> None:
        self.log(self.action_stats_map[action_number][ss.TEXTS][self.main_menu.language])
        self.main_menu.main_character.set_max_stamina()
        self.main_menu.chill_event.run_event()

    def battle_action(self, action_number: int) -> None:
        self.log(self.action_stats_map[action_number][ss.TEXTS][self.main_menu.language])
        enemy_stats = self.action_enemies[action_number]
        level_map = {
            ss.CHARACTER_LEVEL: self.main_menu.main_character.level,
        }
        enemy = Enemy(
            level=level_map[enemy_stats[ss.LEVEL]] + enemy_stats[ss.ADDED_LEVEL],
            main_menu=self.main_menu,
            enemy_file_name=enemy_stats[ss.ENEMY_TYPE]
        )
        weapon = Weapon(
            main_menu=self.main_menu,
            level=enemy.level,
            rarity=enemy.item_quality,
            weapon_file_name=enemy_stats[ss.WEAPON]
        )
        enemy.name = enemy_stats[ss.NAMES][self.main_menu.language]
        enemy.set_weapon(weapon)
        self.log(f"{Text[self.main_menu.language].BATTLE_START} {enemy.name} {Text[self.main_menu.language].LEVEL} {enemy.level}")
        Battle(self.main_menu, next_event=self.next_events[action_number], enemy=enemy)

    def reward_action(self, action_number: int):
        self.log(self.action_stats_map[action_number][ss.TEXTS][self.main_menu.language])
        self.main_menu.chill_event.run_event()
    #     TODO Доделать получение наград за ивенты

    def random_action(self, action_number: int):
        self.main_menu.scenarios_manager.start_random_scenario()
