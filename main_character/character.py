from main_character.character_dataclasses import Parameters, Stats, ClassMultipliers
from main_character.equipped_items_stats import EquippedWeapon
from core.constants import character_constants as cc


class MainCharacter:
    def __init__(self):
        self._parameters = Parameters
        self._stats = Stats
        self._class_multipliers = ClassMultipliers

    def set_class_warrior(self):
        self._class_multipliers.HEALTH_MULTIPLIER = 2
        self._class_multipliers.STAMINA_MULTIPLIER = 1
        self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER = 0
        self._class_multipliers.AGILITY_CRITICAL_MULTIPLIER = 0.5
        self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER = 1.2

    def set_class_assassin(self):
        self._class_multipliers.HEALTH_MULTIPLIER = 0.7
        self._class_multipliers.STAMINA_MULTIPLIER = 1.5
        self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER = 1
        self._class_multipliers.AGILITY_CRITICAL_MULTIPLIER = 2
        self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER = 0

    def _refresh_stats(self):
        self._stats.MAX_HEALTH: float = self._class_multipliers.HEALTH_MULTIPLIER * \
                                        ((self._parameters.LEVEL * 5) + (self._parameters.VITALITY * 10))
        self._stats.MAX_STAMINA: float = self._class_multipliers.STAMINA_MULTIPLIER * \
                                         ((self._parameters.LEVEL * 2.5) + (self._parameters.ENDURANCE * 5))
        self._stats.MIN_DAMAGE: float = EquippedWeapon.MIN_DAMAGE * (
                (self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER * self._parameters.AGILITY * 0.1) +
                (self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER * self._parameters.STRENGTH * 0.1)
        )
        self._stats.MAX_DAMAGE: float = EquippedWeapon.MAX_DAMAGE * (
                (self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER * self._parameters.AGILITY * 0.12) +
                (self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER * self._parameters.STRENGTH * 0.12)
        )
        self._stats.CRITICAL_STRIKE_CHANCE: float = EquippedWeapon.CRITICAL_STRIKE_CHANCE * (
                self._parameters.AGILITY * 5 * 1)
        self._stats.CRITICAL_STRIKE_MULTIPLIER: float = 1.5
        self._stats.STRIKE_CHANCE: float = EquippedWeapon.ACCURACY

    @staticmethod
    def _not_enough_points():
        print("Not enough parameters points!")

    def set_max_health(self):
        self._stats.HEALTH = self._stats.MAX_HEALTH

    def set_max_stamina(self):
        self._stats.STAMINA = self._stats.MAX_STAMINA

    def add_level(self):
        self._parameters.LEVEL += 1
        self._parameters.PARAMETERS_POINTS += 3
        self._refresh_stats()
        self.set_max_health()
        self.set_max_stamina()

    def add_endurance(self):
        if self._parameters.PARAMETERS_POINTS >= 1:
            self._parameters.ENDURANCE += 1
            self._parameters.PARAMETERS_POINTS -= 1
            self._refresh_stats()
        else:
            self._not_enough_points()

    def add_vitality(self):
        if self._parameters.PARAMETERS_POINTS >= 1:
            self._parameters.VITALITY += 1
            self._parameters.PARAMETERS_POINTS -= 1
            self._refresh_stats()
        else:
            self._not_enough_points()

    def add_strength(self):
        if self._parameters.PARAMETERS_POINTS >= 1:
            self._parameters.STRENGTH += 1
            self._parameters.PARAMETERS_POINTS -= 1
            self._refresh_stats()
        else:
            self._not_enough_points()

    def add_agility(self):
        if self._parameters.PARAMETERS_POINTS >= 1:
            self._parameters.AGILITY += 1
            self._parameters.PARAMETERS_POINTS -= 1
            self._refresh_stats()
        else:
            self._not_enough_points()

    def get_level(self):
        return self._parameters.LEVEL

    def get_stats(self):
        stats = {
            cc.HEALTH: (self._stats.MAX_HEALTH, self._stats.HEALTH),
            cc.STAMINA: (self._stats.MAX_STAMINA, self._stats.STAMINA),
        }
        return stats

    def get_parameters(self):
        parameters = {
            cc.STRENGTH: self._parameters.STRENGTH,
            cc.AGILITY: self._parameters.AGILITY,
            cc.VITALITY: self._parameters.VITALITY,
            cc.ENDURANCE: self._parameters.ENDURANCE,
        }
        return parameters
