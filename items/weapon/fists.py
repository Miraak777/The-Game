from .base_weapon import BaseWeapon


class Fists(BaseWeapon):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = "Fists"
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 1
        self.stats.MAX_DAMAGE = 2
        self.stats.CRITICAL_STRIKE_CHANCE = 0.05
        self.stats.ACCURACY = 0.8
        self.stats.STAMINA_CONSUMPTION = 1
        self.stats.ARMOUR_PENETRATION = 0
        self._calculate_damage()

