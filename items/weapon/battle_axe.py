from .weapon import Weapon


class BattleAxe(Weapon):
    WEAPON_NAME = "Battle Axe"
    TWO_HANDED = False
    MIN_DAMAGE = 14
    MAX_DAMAGE = 28
    CRITICAL_STRIKE_CHANCE = 0.05
    ACCURACY = 0.8
    STAMINA_CONSUMPTION = 6
    ARMOUR_PENETRATION = 0.2


class TwoHandedBattleAxe(BattleAxe):
    WEAPON_NAME = "Two Handed Battle Axe"
    TWO_HANDED = True
    MIN_DAMAGE = 20
    MAX_DAMAGE = 40
    ACCURACY = 0.6
    STAMINA_CONSUMPTION = 9


class DualBattleAxes(BattleAxe):
    WEAPON_NAME = "Dual Battle Axes"
    TWO_HANDED = True
    MIN_DAMAGE = 28
    MAX_DAMAGE = 56
    ACCURACY = 0.6
    STAMINA_CONSUMPTION = 1.6
