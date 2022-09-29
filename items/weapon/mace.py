from .weapon import Weapon


class Mace(Weapon):
    WEAPON_NAME = "Mace"
    TWO_HANDED = False
    MIN_DAMAGE = 16
    MAX_DAMAGE = 32
    CRITICAL_STRIKE_CHANCE = 0.05
    ACCURACY = 0.8
    STAMINA_CONSUMPTION = 7
    ARMOUR_PENETRATION = 0.4


class TwoHandedMace(Mace):
    WEAPON_NAME = "Two Handed Mace"
    TWO_HANDED = True
    MIN_DAMAGE = 22
    MAX_DAMAGE = 44
    ACCURACY = 0.6
    STAMINA_CONSUMPTION = 11


class DualMaces(Mace):
    WEAPON_NAME = "Dual Maces"
    TWO_HANDED = True
    MIN_DAMAGE = 32
    MAX_DAMAGE = 64
    ACCURACY = 0.6
    STAMINA_CONSUMPTION = 14
