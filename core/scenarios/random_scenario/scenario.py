from random import random, randrange

from core.scenarios import WarriorGuildScenario


class RandomScenario:
    def __init__(self, main_menu):
        self._main_menu = main_menu
        self._battle_scenario = self._main_menu.battle_scenario
        self._scenarios_map = [WarriorGuildScenario]
        self._battle_chance = 0.8

    def get_random_scenario(self):
        if random() < self._battle_chance:
            return self._battle_scenario.start_battle
        if len(self._scenarios_map) != 0:
            scenario_id = randrange(0, len(self._scenarios_map))
            scenario = self._scenarios_map[scenario_id]
            self._scenarios_map.pop(scenario_id)
            return scenario
        return self._battle_scenario.start_battle
