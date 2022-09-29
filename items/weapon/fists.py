from .weapon import Weapon


class Fists(Weapon):
    WEAPON_NAME = "Fists"
    TWO_HANDED = True
    MIN_DAMAGE = 1
    MAX_DAMAGE = 2
    CRITICAL_STRIKE_CHANCE = 0.05
    ACCURACY = 0.8
    STAMINA_CONSUMPTION = 1
    ARMOUR_PENETRATION = 0
