from .weapon import Weapon


class Dagger(Weapon):
    WEAPON_NAME = "Dagger"
    TWO_HANDED = False
    MIN_DAMAGE = 4
    MAX_DAMAGE = 12
    CRITICAL_STRIKE_CHANCE = 0.1
    ACCURACY = 0.8
    STAMINA_CONSUMPTION = 3
    ARMOUR_PENETRATION = 0.5


class DualDaggers(Dagger):
    WEAPON_NAME = "Dual Daggers"
    TWO_HANDED = True
    MIN_DAMAGE = 8
    MAX_DAMAGE = 24
    STAMINA_CONSUMPTION = 5
