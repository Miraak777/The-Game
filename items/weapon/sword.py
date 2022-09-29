from .weapon import Weapon


class Sword(Weapon):
    WEAPON_NAME = "Sword"
    TWO_HANDED = False
    MIN_DAMAGE = 12
    MAX_DAMAGE = 24
    CRITICAL_STRIKE_CHANCE = 0.05
    ACCURACY = 0.8
    STAMINA_CONSUMPTION = 5
    ARMOUR_PENETRATION = 0.1


class TwoHandedSword(Sword):
    WEAPON_NAME = "Two-Handed Sword"
    TWO_HANDED = True
    MIN_DAMAGE = 18
    MAX_DAMAGE = 36
    ACCURACY = 0.6
    STAMINA_CONSUMPTION = 7


class DualSwords(Sword):
    WEAPON_NAME = "Dual Swords"
    TWO_HANDED = True
    MIN_DAMAGE = 24
    MAX_DAMAGE = 48
    ACCURACY = 0.6
    STAMINA_CONSUMPTION = 8
