from random import random
from typing import List

import core.items as items
from core.constants.weapon_names import WeaponNames as wn, ConsumableNames as cn


class BaseDropRate:
    def __init__(self):
        self._droppable_items = {
            wn.DAGGER: [0, items.weapon.Dagger],
            wn.DUAL_DAGGERS: [0, items.weapon.DualDaggers],
            wn.SWORD: [0, items.weapon.Sword],
            wn.TWO_HANDED_SWORD: [0, items.weapon.TwoHandedSword],
            wn.DUAL_SWORDS: [0, items.weapon.DualSwords],
            wn.BATTLE_AXE: [0, items.weapon.BattleAxe],
            wn.TWO_HANDED_BATTLE_AXE: [0, items.weapon.TwoHandedBattleAxe],
            wn.DUAL_BATTLE_AXE: [0, items.weapon.DualBattleAxes],
            wn.MACE: [0, items.weapon.Mace],
            wn.TWO_HANDED_MACE: [0, items.weapon.TwoHandedMace],
            wn.DUAL_MACES: [0, items.weapon.DualMaces],
            cn.APPLE: [0, items.consumables.Apple],
            cn.STEAK: [0, items.consumables.Steak],
            cn.PIE: [0, items.consumables.Pie]
        }

    def set_drop_rate(self, weapon, drop_rate: float) -> None:
        self._droppable_items[weapon][0] = drop_rate

    def drop_items(self) -> List:
        dropped_items = []
        for item in self._droppable_items:
            if random() < self._droppable_items[item][0]:
                dropped_items.append(self._droppable_items[item][1])
        return dropped_items
