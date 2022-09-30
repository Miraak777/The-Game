from random import random
from typing import List

import items


class BaseDropRate:
    def __init__(self):
        self._droppable_items = {
            "Dagger": [0, items.weapon.Dagger],
            "DualDaggers": [0, items.weapon.DualDaggers],
            "Sword": [0, items.weapon.Sword],
            "TwoHandedSword": [0, items.weapon.TwoHandedSword],
            "DualSwords": [0, items.weapon.DualSwords],
            "BattleAxe": [0, items.weapon.BattleAxe],
            "TwoHandedBattleAxe": [0, items.weapon.TwoHandedBattleAxe],
            "DualBattleAxes": [0, items.weapon.DualBattleAxes],
            "Mace": [0, items.weapon.Mace],
            "TwoHandedMace": [0, items.weapon.TwoHandedMace],
            "DualMaces": [0, items.weapon.DualMaces],
        }

    def set_drop_rate(self, weapon, drop_rate: float) -> None:
        self._droppable_items[weapon][0] = drop_rate

    def drop_items(self) -> List:
        dropped_items = []
        for item in self._droppable_items:
            if random() < self._droppable_items[item][0]:
                dropped_items.append(self._droppable_items[item][1])
        return dropped_items
