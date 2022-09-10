import items.weapon
from typing import Dict
from core.constants.character_constants import (
    AttributesNames as an,
    BarsNames as bn,
    Classes,
    CombatStatsNames as cs,
    MainStatsNames as msn,
)
from core.stats_formulas import characters_formulas as cf
from main_character.start_parameters import (
    Attributes,
    Bars,
    ClassMultipliers,
    CombatStats,
    MainStats,
)


class MainCharacter:
    def __init__(self, character_name: str) -> None:
        self._main_stats = MainStats
        self._main_stats.NAME = character_name
        self._attributes = Attributes
        self._bars = Bars
        self._combat_stats = CombatStats
        self._class_multipliers = ClassMultipliers
        self._equipped_weapon = items.weapon.Fists
        self._attribute_map = {
            an.STRENGTH: self._attributes.STRENGTH,
            an.AGILITY: self._attributes.AGILITY,
            an.VITALITY: self._attributes.VITALITY,
            an.ENDURANCE: self._attributes.ENDURANCE,
        }

    def set_class_warrior(self) -> None:
        self._class_multipliers.HEALTH_MULTIPLIER = 2
        self._class_multipliers.STAMINA_MULTIPLIER = 1
        self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER = 0
        self._class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER = 0.5
        self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER = 1
        self._main_stats.CLASS = Classes.WARRIOR

    def set_class_assassin(self) -> None:
        self._class_multipliers.HEALTH_MULTIPLIER = 0.7
        self._class_multipliers.STAMINA_MULTIPLIER = 1.5
        self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER = 1
        self._class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER = 2
        self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER = 0
        self._main_stats.CLASS = Classes.ASSASSIN

    def set_class_peasant(self) -> None:
        self._class_multipliers.HEALTH_MULTIPLIER = 1
        self._class_multipliers.STAMINA_MULTIPLIER = 1
        self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER = 0.5
        self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER = 0.5
        self._class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER = 1
        self._main_stats.CLASS = Classes.PEASANT

    def _refresh_stats(self) -> None:
        self._bars.MAX_HEALTH = cf.health_formula(
            health_mult=self._class_multipliers.HEALTH_MULTIPLIER,
            level=self._main_stats.LEVEL,
            vitality=self._attributes.VITALITY,
        )
        self._bars.MAX_STAMINA = cf.stamina_formula(
            stamina_mult=self._class_multipliers.STAMINA_MULTIPLIER,
            level=self._main_stats.LEVEL,
            endurance=self._attributes.ENDURANCE,
        )
        self._combat_stats.MIN_DAMAGE = cf.min_damage_formula(
            min_damage=self._equipped_weapon.MIN_DAMAGE,
            strength=self._attributes.STRENGTH,
            strength_damage_multiplier=self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
            agility=self._attributes.AGILITY,
            agility_damage_multiplier=self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
        )
        self._combat_stats.MAX_DAMAGE = cf.max_damage_formula(
            max_damage=self._equipped_weapon.MAX_DAMAGE,
            strength=self._attributes.STRENGTH,
            strength_damage_multiplier=self._class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
            agility=self._attributes.AGILITY,
            agility_damage_multiplier=self._class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
        )
        self._combat_stats.CRITICAL_STRIKE_CHANCE = cf.critical_strike_formula(
            base_critical_strike_chance=self._equipped_weapon.CRITICAL_STRIKE_CHANCE,
            agility=self._attributes.AGILITY,
            critical_strike_chance_multiplier=self._class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER,
        )
        self._combat_stats.CRITICAL_STRIKE_MULTIPLIER = 1.5
        self._combat_stats.ACCURACY = cf.accuracy_formula(
            accuracy=self._equipped_weapon.ACCURACY,
            agility=self._attributes.AGILITY,
            level=self._main_stats.LEVEL,
        )

    def set_max_health(self) -> None:
        self._bars.HEALTH = self._bars.MAX_HEALTH

    def set_max_stamina(self) -> None:
        self._bars.STAMINA = self._bars.MAX_STAMINA

    def add_level(self) -> None:
        self._main_stats.LEVEL += 1
        self._attributes.ATTRIBUTE_POINTS += 3
        self._refresh_stats()
        self.set_max_health()
        self.set_max_stamina()

    def add_endurance(self) -> None:
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.ENDURANCE += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
            self._refresh_stats()

    def add_vitality(self) -> None:
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.VITALITY += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
            self._refresh_stats()

    def add_strength(self) -> None:
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.STRENGTH += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
            self._refresh_stats()

    def add_agility(self) -> None:
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.AGILITY += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
            self._refresh_stats()

    def remove_strength(self):
        if self._attributes.STRENGTH > 0:
            self._attributes.STRENGTH -= 1
            self._attributes.ATTRIBUTE_POINTS += 1
            self._refresh_stats()

    def remove_agility(self):
        if self._attributes.AGILITY > 0:
            self._attributes.AGILITY -= 1
            self._attributes.ATTRIBUTE_POINTS += 1
            self._refresh_stats()

    def remove_vitality(self):
        if self._attributes.VITALITY > 0:
            self._attributes.VITALITY -= 1
            self._attributes.ATTRIBUTE_POINTS += 1
            self._refresh_stats()

    def remove_endurance(self):
        if self._attributes.ENDURANCE > 0:
            self._attributes.ENDURANCE -= 1
            self._attributes.ATTRIBUTE_POINTS += 1
            self._refresh_stats()

    def send_attributes(self, attributes: Dict) -> None:
        attribute_count = 0
        for attribute in attributes:
            attribute_count += attributes[attribute]
        if self._attributes.ATTRIBUTE_POINTS >= attribute_count:
            self._attribute_map += attributes
            self._attributes.ATTRIBUTE_POINTS -= attribute_count
            self._refresh_stats()

    def get_stats(self) -> Dict:
        self._refresh_stats()
        stats = {
            msn.NAME: self._main_stats.NAME,
            msn.LEVEL: self._main_stats.LEVEL,
            msn.CLASS: self._main_stats.CLASS,
            bn.MAX_HEALTH: self._bars.MAX_HEALTH,
            bn.HEALTH: self._bars.HEALTH,
            bn.MAX_STAMINA: self._bars.MAX_STAMINA,
            bn.STAMINA: self._bars.STAMINA,
            an.STRENGTH: self._attributes.STRENGTH,
            an.AGILITY: self._attributes.AGILITY,
            an.VITALITY: self._attributes.VITALITY,
            an.ENDURANCE: self._attributes.ENDURANCE,
            an.ATTRIBUTE_POINTS: self._attributes.ATTRIBUTE_POINTS,
            cs.MIN_DAMAGE: self._combat_stats.MIN_DAMAGE,
            cs.MAX_DAMAGE: self._combat_stats.MAX_DAMAGE,
            cs.ACCURACY: self._combat_stats.ACCURACY,
            cs.CRITICAL_STRIKE_CHANCE: self._combat_stats.CRITICAL_STRIKE_CHANCE,
            cs.CRITICAL_STRIKE_MULTIPLIER: self._combat_stats.CRITICAL_STRIKE_MULTIPLIER,
        }
        return stats
