from random import random, randrange
from typing import List
from ..scenarios_maps import scenarios_maps


class RandomScenario:
    def __init__(self, main_menu):
        self._main_menu = main_menu
        self._battle_scenario = self._main_menu.battle_scenario
        self._battle_chance = 0.8

    def get_random_scenario(self):
        scenarios_map = self._get_scenarios_map()
        if random() < self._battle_chance:
            return self._battle_scenario.start_battle
        if len(scenarios_map) != 0:
            scenario_id = randrange(0, len(scenarios_map))
            scenario = scenarios_map[scenario_id]
            scenarios_map.pop(scenario_id)
            return scenario
        return self._battle_scenario.start_battle

    def _get_scenarios_map(self) -> List:
        output_scenario = None
        level = self._main_menu.main_character.main_stats.LEVEL
        for i in range(len(scenarios_maps)):
            if level >= scenarios_maps[i][0]:
                output_scenario = scenarios_maps[i][1]
            else:
                output_scenario = scenarios_maps[i - 1][1]
        return output_scenario
