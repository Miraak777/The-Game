import items.weapon
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from typing import Dict, Any
from core.constants.character_constants import (
    AttributesNames as an,
    BarsNames as bn,
    Classes,
    CombatStatsNames as cs,
    MainStatsNames as msn,
    StatsNames as sn
)
from core.stats_formulas import characters_formulas as cf
from interface.game_menu.stylesheets import label_stylesheet
from main_character import classes
from main_character.start_parameters import (
    Attributes,
    Bars,
    ClassMultipliers,
    CombatStats,
    MainStats,
)


class MainCharacter:
    def __init__(self, character_name: str, main_menu) -> None:
        self._main_menu = main_menu
        self._main_stats = MainStats()
        self._main_stats.NAME = character_name
        self._attributes = Attributes()
        self._bars = Bars()
        self._combat_stats = CombatStats()
        self._class_multipliers = ClassMultipliers()
        self._equipped_weapon = items.weapon.Fists

    def set_class_peasant(self) -> None:
        self._class_multipliers = classes.PeasantClass
        self._main_stats.CLASS = Classes.PEASANT
        self._main_menu.game_menu.add_log(self._main_menu.text.BECOME_PEASANT)

    def set_class_warrior(self) -> None:
        self._class_multipliers = classes.WarriorClass
        self._main_stats.CLASS = Classes.WARRIOR
        self._main_menu.game_menu.add_log(self._main_menu.text.BECOME_WARRIOR)

    def set_class_assassin(self) -> None:
        self._class_multipliers = classes.AssassinClass
        self._main_stats.CLASS = Classes.ASSASSIN
        self._main_menu.game_menu.add_log(self._main_menu.text.BECOME_ASSASSIN)

    @staticmethod
    def calculate_character_stats(attributes, main_stats, class_multipliers, equipped_weapon) -> Dict[str, Any]:
        calculated_stats = {
            bn.MAX_HEALTH: cf.health_formula(
                health_mult=class_multipliers.HEALTH_MULTIPLIER,
                level=main_stats.LEVEL,
                vitality=attributes.VITALITY,
            ),
            bn.MAX_STAMINA: cf.stamina_formula(
                stamina_mult=class_multipliers.STAMINA_MULTIPLIER,
                level=main_stats.LEVEL,
                endurance=attributes.ENDURANCE,
            ),
            cs.MIN_DAMAGE: cf.min_damage_formula(
                min_damage=equipped_weapon.MIN_DAMAGE,
                strength=attributes.STRENGTH,
                strength_damage_multiplier=class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
                agility=attributes.AGILITY,
                agility_damage_multiplier=class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
            ),
            cs.MAX_DAMAGE: cf.max_damage_formula(
                max_damage=equipped_weapon.MAX_DAMAGE,
                strength=attributes.STRENGTH,
                strength_damage_multiplier=class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
                agility=attributes.AGILITY,
                agility_damage_multiplier=class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
            ),
            cs.CRITICAL_STRIKE_CHANCE: cf.critical_strike_formula(
                base_critical_strike_chance=equipped_weapon.CRITICAL_STRIKE_CHANCE,
                agility=attributes.AGILITY,
                critical_strike_chance_multiplier=class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER,
            ),
            cs.CRITICAL_STRIKE_MULTIPLIER: 1.5,
            cs.ACCURACY: cf.accuracy_formula(
                accuracy=equipped_weapon.ACCURACY,
                agility=attributes.AGILITY,
                level=main_stats.LEVEL,
            )
        }
        return calculated_stats

    def _refresh_stats(self) -> None:
        stats = self.calculate_character_stats(self._attributes,
                                               self._main_stats,
                                               self._class_multipliers,
                                               self._equipped_weapon)
        self._bars.MAX_HEALTH = stats[bn.MAX_HEALTH]
        self._bars.MAX_STAMINA = stats[bn.MAX_STAMINA]
        self._combat_stats.MAX_DAMAGE = stats[cs.MAX_DAMAGE]
        self._combat_stats.MIN_DAMAGE = stats[cs.MIN_DAMAGE]
        self._combat_stats.ACCURACY = stats[cs.ACCURACY]
        self._combat_stats.CRITICAL_STRIKE_CHANCE = stats[cs.CRITICAL_STRIKE_CHANCE]
        self._combat_stats.CRITICAL_STRIKE_MULTIPLIER = stats[cs.CRITICAL_STRIKE_MULTIPLIER]

    def set_max_health(self) -> None:
        self._bars.HEALTH = self._bars.MAX_HEALTH

    def set_max_stamina(self) -> None:
        self._bars.STAMINA = self._bars.MAX_STAMINA

    def _add_level(self) -> None:
        self._main_stats.LEVEL += 1
        self._main_stats.MAX_EXPERIENCE = self._main_stats.LEVEL * 100
        self._attributes.ATTRIBUTE_POINTS += 3
        self._refresh_stats()
        self.set_max_health()
        self.set_max_stamina()

    def send_attributes(self, attributes: Dict[str, int]) -> None:
        attribute_count = self._attributes.ATTRIBUTE_POINTS - attributes[an.ATTRIBUTE_POINTS]
        if self._attributes.ATTRIBUTE_POINTS >= attribute_count:
            self._attributes.STRENGTH = attributes[an.STRENGTH]
            self._attributes.AGILITY = attributes[an.AGILITY]
            self._attributes.VITALITY = attributes[an.VITALITY]
            self._attributes.ENDURANCE = attributes[an.ENDURANCE]
            self._attributes.ATTRIBUTE_POINTS = attributes[an.ATTRIBUTE_POINTS]
            self._refresh_stats()

    def send_experience(self, experience: int):
        self._main_stats.EXPERIENCE += experience
        if experience != 0:
            self._main_menu.game_menu.add_log(self._main_menu.text.GAINED_EXPERIENCE + str(experience))
        if self._main_stats.EXPERIENCE >= self._main_stats.MAX_EXPERIENCE:
            self._main_stats.EXPERIENCE -= self._main_stats.MAX_EXPERIENCE
            self._add_level()
            self._main_menu.game_menu.add_log(self._main_menu.text.LEVEL_UP)
            self.send_experience(0)

    def get_stats_for_calculation(self) -> Dict[str, Any]:
        output_stats = {
            sn.ATTRIBUTES: self._attributes,
            sn.MAIN_STATS: self._main_stats,
            sn.CLASS_MULTIPLIERS: self._class_multipliers,
            sn.EQUIPPED_WEAPON: self._equipped_weapon
        }
        return output_stats

    def get_stats(self) -> Dict:
        self._refresh_stats()
        stats = {
            msn.NAME: self._main_stats.NAME,
            msn.LEVEL: self._main_stats.LEVEL,
            msn.MAX_EXPERIENCE: self._main_stats.MAX_EXPERIENCE,
            msn.EXPERIENCE: self._main_stats.EXPERIENCE,
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
