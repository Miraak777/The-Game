from .weapon_stats import WeaponStats


class BaseWeapon:
    def __init__(self, main_menu,  level=1):
        self._language = main_menu.language
        self.stats = WeaponStats()
        self.stats.LEVEL = level
        self._calculate_damage()

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = self.stats.MAX_DAMAGE * (1 + self.stats.LEVEL * self.stats.LEVEL_DAMAGE_MULTIPLIER)
        self.stats.MIN_DAMAGE = self.stats.MIN_DAMAGE * (1 + self.stats.LEVEL * self.stats.LEVEL_DAMAGE_MULTIPLIER)