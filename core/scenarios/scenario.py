from random import random, choice
from core.enemies.enemies_table import get_enemy_table
from core.enemies.enemy import Enemy
from .event import Event
from .battle import Battle
from .constants import ScenarioStats as ss
from .scenarios_table import get_scenarios_table
from .common import read_scenario_stats
from .texts import Text


class ScenariosManager:
    def __init__(self, main_menu):
        self.scenario_chance = 0.2
        self.main_menu = main_menu

    def start_scenario(self, scenario_file_name: str) -> None:
        stats = read_scenario_stats(scenario_file_name)
        events = {}
        for event_name, event_stats in stats.items():
            events[event_name] = Event(self.main_menu, event_stats)
        for event_name in events:
            for action_next_event_index, action_next_event_name in enumerate(events[event_name].next_events):
                if action_next_event_name:
                    events[event_name].next_events[action_next_event_index] = events[action_next_event_name]
        events[ss.START].run_event()

    def start_random_scenario(self):
        scenarios_table = get_scenarios_table()
        level = self.main_menu.main_character.level
        if random() <= self.scenario_chance:
            scenarios_list = [
                scenario_name
                for scenario_level, scenario_name in scenarios_table.items()
                if scenario_level and scenario_level <= level
            ]
            if scenarios_list:
                scenario = choice(scenarios_list)
                self.start_scenario(scenario)

        enemy_list = [
            enemy_name
            for enemy_name, enemy_min_level in get_enemy_table().items()
            if enemy_min_level <= level
        ]
        enemy = Enemy(level, self.main_menu, choice(enemy_list))
        self.main_menu.game_menu.add_log(f"{Text[self.main_menu.language].BATTLE_START} {enemy.name} {Text[self.main_menu.language].LEVEL} {enemy.level}")
        Battle(enemy=enemy, main_menu=self.main_menu)
