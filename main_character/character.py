from main_character.character_dataclasses import Parameters, Stats, ClassMultipliers
import items.weapon
from core.constants import character_constants as cc
from core.stats_formulas import characters_formulas as cf


class MainCharacter:
    def __init__(self):
        self._parameters = Parameters
        self._stats = Stats
        self._class_multipliers = ClassMultipliers
        self._equipped_weapon = items.weapon.Fists

    def set_class_warrior(self):
        self._class_multipliers.HEALTH_MULTIPLIER = 2
        self._class_multipliers.STAMINA_MULTIPLIER = 1
        self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER = 0
        self._class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER = 0.5
        self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER = 1

    def set_class_assassin(self):
        self._class_multipliers.HEALTH_MULTIPLIER = 0.7
        self._class_multipliers.STAMINA_MULTIPLIER = 1.5
        self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER = 1
        self._class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER = 2
        self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER = 0

    def _refresh_stats(self):
        self._stats.MAX_HEALTH = cf.health_formula(
            health_mult=self._class_multipliers.HEALTH_MULTIPLIER,
            level=self._parameters.LEVEL,
            vitality=self._parameters.VITALITY
        )
        self._stats.MAX_STAMINA = cf.stamina_formula(
            stamina_mult=self._class_multipliers.STAMINA_MULTIPLIER,
            level=self._parameters.LEVEL,
            endurance=self._parameters.ENDURANCE,
        )
        self._stats.MIN_DAMAGE = cf.min_damage_formula(
            min_damage=self._equipped_weapon.MIN_DAMAGE,
            strength=self._parameters.STRENGTH,
            strength_damage_multiplier=self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
            agility=self._parameters.AGILITY,
            agility_damage_multiplier=self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
        )
        self._stats.MAX_DAMAGE = cf.max_damage_formula(
            max_damage=self._equipped_weapon.MAX_DAMAGE,
            strength=self._parameters.STRENGTH,
            strength_damage_multiplier=self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
            agility=self._parameters.AGILITY,
            agility_damage_multiplier=self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
        )
        self._stats.CRITICAL_STRIKE_CHANCE = cf.critical_strike_formula(
            base_critical_strike_chance=self._equipped_weapon.CRITICAL_STRIKE_CHANCE,
            agility=self._parameters.AGILITY,
            critical_strike_chance_multiplier=self._class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER
        )
        self._stats.CRITICAL_STRIKE_MULTIPLIER = 1.5
        self._stats.ACCURACY = self._equipped_weapon.ACCURACY

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

    def get_bars(self):
        bars = {
            cc.HEALTH: (self._stats.MAX_HEALTH, self._stats.HEALTH),
            cc.STAMINA: (self._stats.MAX_STAMINA, self._stats.STAMINA),
        }
        return bars

    def get_parameters(self):
        parameters = {
            cc.STRENGTH: self._parameters.STRENGTH,
            cc.AGILITY: self._parameters.AGILITY,
            cc.VITALITY: self._parameters.VITALITY,
            cc.ENDURANCE: self._parameters.ENDURANCE,
        }
        return parameters

    def get_combat_stats(self):
        combat_stats = {
            cc.MIN_DAMAGE: self._stats.MIN_DAMAGE,
            cc.MAX_DAMAGE: self._stats.MAX_DAMAGE,
            cc.ACCURACY: self._stats.ACCURACY,
            cc.CRITICAL_STRIKE_CHANCE: self._stats.CRITICAL_STRIKE_CHANCE,
            cc.CRITICAL_STRIKE_MULTIPLIER: self._stats.CRITICAL_STRIKE_MULTIPLIER
        }
        return combat_stats
