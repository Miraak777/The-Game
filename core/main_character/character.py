import random
from typing import Any, Dict

from core.constants.character_constants import AttributesNames as an
from core.constants.character_constants import BarsNames as bn
from core.constants.character_constants import Classes
from core.constants.character_constants import CombatStatsNames as cs
from core.constants.character_constants import CommonConstants as cc
from core.constants.character_constants import MainStatsNames as msn
from core.constants.character_constants import StatsNames as sn
from core.items.weapon import Fists
from core.scenarios.death_scenario.scenario import DeathScenario
from core.stats_formulas import characters_formulas as cf

from . import classes
from .start_parameters import Attributes, Bars, CombatStats, MainStats
from .texts import Text


class MainCharacter:
    def __init__(self, character_name: str, main_menu) -> None:
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self._add_log = self._main_menu.game_menu.add_log
        self.main_stats = MainStats()
        self.main_stats.NAME = character_name
        self._attributes = Attributes()
        self._bars = Bars()
        self._combat_stats = CombatStats()
        self._class_multipliers = classes.PeasantClass()
        self._equipped_weapon = Fists(level=self.main_stats.LEVEL, main_menu=self._main_menu)
        self._no_weapon = True
        self._refresh_stats()

    def attack(self, attack_type: str) -> float:
        attack_map = {
            cc.LIGHT_ATTACK: self.light_attack_prediction,
            cc.MEDIUM_ATTACK: self.medium_attack_prediction,
            cc.HEAVY_ATTACK: self.heavy_attack_prediction,
        }
        attack_params = attack_map[attack_type]()
        if random.random() < self._combat_stats.CRITICAL_STRIKE_CHANCE:
            self._add_log(self._text.CRITICAL_STRIKE)
            critical_multiplier = self._class_multipliers.CRITICAL_DAMAGE_MULTIPLIER
        else:
            critical_multiplier = 1
        if self._bars.STAMINA < attack_params[cc.STAMINA_CONSUMPTION]:
            self._add_log(self._text.NOT_ENOUGH_STAMINA)
            return 0
        self._bars.STAMINA = round(self._bars.STAMINA - attack_params[cc.STAMINA_CONSUMPTION], 1)
        if random.random() < self._combat_stats.ACCURACY:
            damage = random.uniform(attack_params[cs.MAX_DAMAGE], attack_params[cs.MIN_DAMAGE])
            damage *= critical_multiplier
            return round(damage, 2)
        else:
            self._add_log(self._text.MISS)
            return 0

    def light_attack_prediction(self) -> Dict[str, float]:
        damage = self._calculate_damage(0.8)
        output = {
            cs.MAX_DAMAGE: damage[cs.MAX_DAMAGE],
            cs.MIN_DAMAGE: damage[cs.MIN_DAMAGE],
            cc.STAMINA_CONSUMPTION: round(self._equipped_weapon.stats.STAMINA_CONSUMPTION * 0.7, 1),
        }
        return output

    def medium_attack_prediction(self) -> Dict[str, float]:
        damage = self._calculate_damage(1)
        output = {
            cs.MAX_DAMAGE: damage[cs.MAX_DAMAGE],
            cs.MIN_DAMAGE: damage[cs.MIN_DAMAGE],
            cc.STAMINA_CONSUMPTION: round(self._equipped_weapon.stats.STAMINA_CONSUMPTION * 1, 1),
        }
        return output

    def heavy_attack_prediction(self) -> Dict[str, float]:
        damage = self._calculate_damage(1.2)
        output = {
            cs.MAX_DAMAGE: damage[cs.MAX_DAMAGE],
            cs.MIN_DAMAGE: damage[cs.MIN_DAMAGE],
            cc.STAMINA_CONSUMPTION: round(self._equipped_weapon.stats.STAMINA_CONSUMPTION * 1.4, 1),
        }
        return output

    def take_damage(self, damage: float) -> None:
        if self._bars.HEALTH <= damage:
            self._add_log(self._text.DEATH)
            DeathScenario(self._main_menu)
        self._bars.HEALTH = round(self._bars.HEALTH - damage, 2)

    def equip_weapon(self, weapon):
        self._equipped_weapon = weapon
        self._add_log(self._text.EQUIPPED_WEAPON + weapon.stats.NAME)
        self._no_weapon = False
        self._refresh_stats()
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()

    def unequip_weapon(self):
        weapon = self._equipped_weapon
        self._equipped_weapon = Fists(level=self.main_stats.LEVEL, main_menu=self._main_menu)
        self._no_weapon = True
        self._refresh_stats()
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()
        return weapon

    def set_class_peasant(self) -> None:
        self._class_multipliers = classes.PeasantClass
        self.main_stats.CLASS = Classes.PEASANT
        self._refresh_stats()
        self._bars.HEALTH *= self._class_multipliers.HEALTH_MULTIPLIER
        self._bars.STAMINA *= self._class_multipliers.STAMINA_MULTIPLIER
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()
        self._add_log(self._text.BECOME_PEASANT)

    def set_class_warrior(self) -> None:
        self._class_multipliers = classes.WarriorClass
        self.main_stats.CLASS = Classes.WARRIOR
        self._refresh_stats()
        self._bars.HEALTH *= self._class_multipliers.HEALTH_MULTIPLIER
        self._bars.STAMINA *= self._class_multipliers.STAMINA_MULTIPLIER
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()
        self._add_log(self._text.BECOME_WARRIOR)

    def set_class_assassin(self) -> None:
        self._class_multipliers = classes.AssassinClass
        self.main_stats.CLASS = Classes.ASSASSIN
        self._refresh_stats()
        self._bars.HEALTH *= self._class_multipliers.HEALTH_MULTIPLIER
        self._bars.STAMINA *= self._class_multipliers.STAMINA_MULTIPLIER
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()
        self._add_log(self._text.BECOME_ASSASSIN)

    def set_max_health(self) -> None:
        self._bars.HEALTH = self._bars.MAX_HEALTH

    def set_max_stamina(self) -> None:
        self._bars.STAMINA = self._bars.MAX_STAMINA

    def restore_health(self, health):
        self._bars.HEALTH += health
        if self._bars.HEALTH > self._bars.MAX_HEALTH:
            self._bars.HEALTH = self._bars.MAX_HEALTH

    def rest(self) -> None:
        if self._bars.HEALTH < self._bars.MAX_HEALTH:
            self._bars.HEALTH = self._bars.MAX_HEALTH
            self._add_log(self._text.REST)
        else:
            self._add_log(self._text.CANNOT_REST)

    def restore_stamina(self, stamina) -> None:
        self._bars.STAMINA += stamina
        if self._bars.STAMINA > self._bars.MAX_STAMINA:
            self._bars.STAMINA = self._bars.MAX_STAMINA

    def send_attributes(self, attributes: Dict[str, int]) -> None:
        attribute_count = self._attributes.ATTRIBUTE_POINTS - attributes[an.ATTRIBUTE_POINTS]
        if self._attributes.ATTRIBUTE_POINTS >= attribute_count:
            self._attributes.STRENGTH = attributes[an.STRENGTH]
            self._attributes.AGILITY = attributes[an.AGILITY]
            vitality_added = attributes[an.VITALITY] - self._attributes.VITALITY
            self._attributes.VITALITY = attributes[an.VITALITY]
            endurance_added = attributes[an.ENDURANCE] - self._attributes.ENDURANCE
            self._attributes.ENDURANCE = attributes[an.ENDURANCE]
            self._attributes.ATTRIBUTE_POINTS = attributes[an.ATTRIBUTE_POINTS]
            self._refresh_stats()
            self.restore_health(
                cf.health_formula(
                    vitality=vitality_added,
                    level=0,
                    health_mult=self._class_multipliers.HEALTH_MULTIPLIER,
                )
            )
            self.restore_stamina(
                cf.stamina_formula(
                    endurance=endurance_added,
                    level=0,
                    stamina_mult=self._class_multipliers.STAMINA_MULTIPLIER,
                )
            )

    def send_experience(self, experience: int):
        self.main_stats.EXPERIENCE += experience
        if experience != 0:
            self._main_menu.game_menu.add_log(self._text.GAINED_EXPERIENCE + str(experience))
        if self.main_stats.EXPERIENCE >= self.main_stats.MAX_EXPERIENCE:
            self.main_stats.EXPERIENCE -= self.main_stats.MAX_EXPERIENCE
            self._add_level()
            self.send_experience(0)

    def get_stats_for_calculation(self) -> Dict[str, Any]:
        output_stats = {
            sn.ATTRIBUTES: self._attributes,
            sn.MAIN_STATS: self.main_stats,
            sn.CLASS_MULTIPLIERS: self._class_multipliers,
            sn.EQUIPPED_WEAPON: self._equipped_weapon,
        }
        return output_stats

    def get_stats(self) -> Dict:
        self._refresh_stats()
        stats = {
            msn.NAME: self.main_stats.NAME,
            msn.LEVEL: self.main_stats.LEVEL,
            msn.MAX_EXPERIENCE: self.main_stats.MAX_EXPERIENCE,
            msn.EXPERIENCE: self.main_stats.EXPERIENCE,
            msn.CLASS: self.main_stats.CLASS,
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
            cs.CRITICAL_STRIKE_MULTIPLIER: self._class_multipliers.CRITICAL_DAMAGE_MULTIPLIER,
        }
        return stats

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
                min_damage=equipped_weapon.stats.MIN_DAMAGE,
                strength=attributes.STRENGTH,
                strength_damage_multiplier=class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
                agility=attributes.AGILITY,
                agility_damage_multiplier=class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
            ),
            cs.MAX_DAMAGE: cf.max_damage_formula(
                max_damage=equipped_weapon.stats.MAX_DAMAGE,
                strength=attributes.STRENGTH,
                strength_damage_multiplier=class_multipliers.STRENGTH_DAMAGE_MULTIPLIER,
                agility=attributes.AGILITY,
                agility_damage_multiplier=class_multipliers.AGILITY_DAMAGE_MULTIPLIER,
            ),
            cs.CRITICAL_STRIKE_CHANCE: cf.critical_strike_formula(
                base_critical_strike_chance=equipped_weapon.stats.CRITICAL_STRIKE_CHANCE,
                agility=attributes.AGILITY,
                critical_strike_chance_multiplier=class_multipliers.CRITICAL_STRIKE_CHANCE_MULTIPLIER,
            ),
            cs.ACCURACY: cf.accuracy_formula(
                accuracy=equipped_weapon.stats.ACCURACY,
                agility=attributes.AGILITY,
                level=main_stats.LEVEL,
            ),
        }
        return calculated_stats

    def _calculate_damage(self, attack_type_damage_multiplier: float) -> Dict[str, float]:
        self._refresh_stats()
        max_damage = round(self._combat_stats.MAX_DAMAGE * attack_type_damage_multiplier, 1)
        min_damage = round(self._combat_stats.MIN_DAMAGE * attack_type_damage_multiplier, 1)
        return {cs.MAX_DAMAGE: max_damage, cs.MIN_DAMAGE: min_damage}

    def _refresh_stats(self) -> None:
        stats = self.calculate_character_stats(
            self._attributes,
            self.main_stats,
            self._class_multipliers,
            self._equipped_weapon,
        )
        self._bars.MAX_HEALTH = stats[bn.MAX_HEALTH]
        self._bars.MAX_STAMINA = stats[bn.MAX_STAMINA]
        self._combat_stats.MAX_DAMAGE = stats[cs.MAX_DAMAGE]
        self._combat_stats.MIN_DAMAGE = stats[cs.MIN_DAMAGE]
        self._combat_stats.ACCURACY = stats[cs.ACCURACY]
        self._combat_stats.CRITICAL_STRIKE_CHANCE = stats[cs.CRITICAL_STRIKE_CHANCE]

    def _add_level(self) -> None:
        self.main_stats.LEVEL += 1
        self.main_stats.MAX_EXPERIENCE = cf.max_experience_formula(level=self.main_stats.LEVEL)
        self._attributes.ATTRIBUTE_POINTS += 3
        if self._no_weapon:
            self._equipped_weapon = Fists(level=self.main_stats.LEVEL, main_menu=self._main_menu)
        self._refresh_stats()
        self.set_max_health()
        self.set_max_stamina()
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()
        self._main_menu.game_menu.add_log(self._text.LEVEL_UP)
