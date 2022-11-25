import random
from typing import Any, Dict

from core.constants.character_constants import AttributesNames as an
from core.constants.character_constants import BarsNames as bn
from core.constants.character_constants import CombatStatsNames as cs
from core.constants.character_constants import CommonConstants as cc
from core.constants.character_constants import MainStatsNames as msn
from core.items import Weapon
from core.scenarios.death_scenario.scenario import DeathScenario

from . import characters_formulas as cf
from . import classes
from .texts import Text


class MainCharacter:
    def __init__(self, character_name: str, main_menu) -> None:
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self._add_log = self._main_menu.game_menu.add_log
        self._refresh_bars = self._main_menu.game_menu.refresh_character_bars
        self.name = character_name
        self._init_start_parameters()

    def attack(self, attack_type: str) -> float:
        attack_map = {
            cc.LIGHT_ATTACK: self.light_attack_prediction,
            cc.MEDIUM_ATTACK: self.medium_attack_prediction,
            cc.HEAVY_ATTACK: self.heavy_attack_prediction,
        }
        attack_params = attack_map[attack_type]()
        if random.random() < self.critical_strike_chance:
            self._add_log(self._text.CRITICAL_STRIKE)
            critical_multiplier = self.critical_strike_multiplier
        else:
            critical_multiplier = 1
        if self.stamina < attack_params[cc.STAMINA_CONSUMPTION]:
            self._add_log(self._text.NOT_ENOUGH_STAMINA)
            return 0
        self.stamina = round(self.stamina - attack_params[cc.STAMINA_CONSUMPTION], 1)
        if random.random() < self.accuracy:
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
            cc.STAMINA_CONSUMPTION: round(self._equipped_weapon.stamina_consumption * 0.7, 1),
        }
        return output

    def medium_attack_prediction(self) -> Dict[str, float]:
        damage = self._calculate_damage(1)
        output = {
            cs.MAX_DAMAGE: damage[cs.MAX_DAMAGE],
            cs.MIN_DAMAGE: damage[cs.MIN_DAMAGE],
            cc.STAMINA_CONSUMPTION: round(self._equipped_weapon.stamina_consumption * 1, 1),
        }
        return output

    def heavy_attack_prediction(self) -> Dict[str, float]:
        damage = self._calculate_damage(1.2)
        output = {
            cs.MAX_DAMAGE: damage[cs.MAX_DAMAGE],
            cs.MIN_DAMAGE: damage[cs.MIN_DAMAGE],
            cc.STAMINA_CONSUMPTION: round(self._equipped_weapon.stamina_consumption * 1.4, 1),
        }
        return output

    def take_damage(self, damage: float) -> None:
        if self.health <= damage:
            self._add_log(self._text.DEATH)
            DeathScenario(self._main_menu)
        self.health = round(self.health - damage, 2)
        self._refresh_bars()

    def equip_weapon(self, weapon: Weapon) -> None:
        self._equipped_weapon = weapon
        weapon.item_equipped = True
        self._add_log(self._text.EQUIPPED_WEAPON + weapon.name)
        self._no_weapon = False
        self.refresh_stats()
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()

    def unequip_weapon(self) -> Weapon:
        weapon = self._equipped_weapon
        weapon.item_equipped = False
        self._equipped_weapon = Weapon(self._main_menu, self.level, "fists.yml")
        self._no_weapon = True
        self.refresh_stats()
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()
        return weapon

    def set_class(self, chosen_class) -> None:
        self.character_class = chosen_class.CLASS_NAME
        self.health_multiplier = chosen_class.HEALTH_MULTIPLIER
        self.stamina_multiplier = chosen_class.STAMINA_MULTIPLIER
        self.agility_damage_multiplier = chosen_class.AGILITY_DAMAGE_MULTIPLIER
        self.strength_damage_multiplier = chosen_class.STRENGTH_DAMAGE_MULTIPLIER
        self.critical_strike_chance_multiplier = chosen_class.CRITICAL_STRIKE_CHANCE_MULTIPLIER
        self.critical_strike_multiplier = chosen_class.CRITICAL_DAMAGE_MULTIPLIER
        self.refresh_stats()
        if self.health:
            self.health *= self.health_multiplier
            self.stamina *= self.stamina_multiplier
            self._main_menu.character_menu.set_actual_character_stats()
            self._main_menu.character_menu.refresh_character_menu()
            self._add_log(self._text.CHANGE_CLASS + self.character_class)
            self._refresh_bars()

    def set_max_health(self) -> None:
        self.health = self.max_health
        self._refresh_bars()

    def set_max_stamina(self) -> None:
        self.stamina = self.max_stamina
        self._refresh_bars()

    def restore_health(self, health: float) -> None:
        self.health = self.health + health
        if self.health > self.max_health:
            self.health = self.max_health

        self._refresh_bars()

    def restore_percent_health(self, health: float) -> None:
        self.health = self.health + (health * 0.01 * self.max_health)
        if self.health > self.max_health:
            self.health = self.max_health

        self._refresh_bars()

    def rest(self) -> None:
        if self.health < self.max_health / 2:
            self.health = self.max_health / 2
            self._add_log(self._text.REST)
            self._refresh_bars()
        else:
            self._add_log(self._text.CANNOT_REST)

    def restore_stamina(self, stamina: float) -> None:
        self.stamina += stamina
        if self.stamina > self.max_stamina:
            self.stamina = self.max_stamina
        self._refresh_bars()

    def send_attributes(self, attributes: Dict[str, int]) -> None:
        attribute_count = self.attribute_points - attributes[an.ATTRIBUTE_POINTS]
        if self.attribute_points >= attribute_count:
            self.strength = attributes[an.STRENGTH]
            self.agility = attributes[an.AGILITY]
            vitality_added = attributes[an.VITALITY] - self.vitality
            self.vitality = attributes[an.VITALITY]
            endurance_added = attributes[an.ENDURANCE] - self.endurance
            self.endurance = attributes[an.ENDURANCE]
            self.attribute_points = attributes[an.ATTRIBUTE_POINTS]
            self.refresh_stats()
            self.restore_health(
                cf.health_formula(
                    vitality=vitality_added,
                    level=0,
                    health_mult=self.health_multiplier,
                )
            )
            self.restore_stamina(
                cf.stamina_formula(
                    endurance=endurance_added,
                    level=0,
                    stamina_mult=self.stamina_multiplier,
                )
            )
            self._refresh_bars()

    def send_experience(self, experience: int) -> None:
        self.experience += experience
        if experience != 0:
            self._main_menu.game_menu.add_log(self._text.GAINED_EXPERIENCE + str(experience))
        if self.experience >= self.max_experience:
            self.experience -= self.max_experience
            self._add_level()
            self.send_experience(0)

    def get_stats(self) -> Dict[str, Any]:
        self.refresh_stats()
        stats = {
            msn.NAME: self.name,
            msn.LEVEL: self.level,
            msn.MAX_EXPERIENCE: self.max_experience,
            msn.EXPERIENCE: self.experience,
            msn.CLASS: self.character_class,
            bn.MAX_HEALTH: self.max_health,
            bn.HEALTH: self.health,
            bn.MAX_STAMINA: self.max_stamina,
            bn.STAMINA: self.stamina,
            an.STRENGTH: self.strength,
            an.AGILITY: self.agility,
            an.VITALITY: self.vitality,
            an.ENDURANCE: self.endurance,
            an.ATTRIBUTE_POINTS: self.attribute_points,
            cs.MAX_DAMAGE: self.max_damage,
            cs.MIN_DAMAGE: self.min_damage,
            cs.ACCURACY: self.accuracy,
            cs.CRITICAL_STRIKE_CHANCE: self.critical_strike_chance,
            cs.CRITICAL_STRIKE_MULTIPLIER: self.critical_strike_multiplier,
        }
        return stats

    def calculate_character_stats(self) -> Dict[str, Any]:
        calculated_stats = {
            bn.MAX_HEALTH: cf.health_formula(
                health_mult=self.health_multiplier,
                level=self.level,
                vitality=self.vitality,
            ),
            bn.MAX_STAMINA: cf.stamina_formula(
                stamina_mult=self.stamina_multiplier,
                level=self.level,
                endurance=self.endurance,
            ),
            cs.MIN_DAMAGE: cf.min_damage_formula(
                min_damage=self._equipped_weapon.min_damage,
                strength=self.strength,
                strength_damage_multiplier=self.strength_damage_multiplier,
                agility=self.agility,
                agility_damage_multiplier=self.agility_damage_multiplier,
            ),
            cs.MAX_DAMAGE: cf.max_damage_formula(
                max_damage=self._equipped_weapon.max_damage,
                strength=self.strength,
                strength_damage_multiplier=self.strength_damage_multiplier,
                agility=self.agility,
                agility_damage_multiplier=self.agility_damage_multiplier,
            ),
            cs.CRITICAL_STRIKE_CHANCE: cf.critical_strike_formula(
                base_critical_strike_chance=self._equipped_weapon.critical_strike_chance,
                agility=self.agility,
                critical_strike_chance_multiplier=self.critical_strike_chance_multiplier,
            ),
            cs.ACCURACY: cf.accuracy_formula(
                accuracy=self._equipped_weapon.accuracy,
                agility=self.agility,
                level=self.level,
            ),
        }
        return calculated_stats

    def refresh_stats(self) -> None:
        stats = self.calculate_character_stats()
        self.max_health = stats[bn.MAX_HEALTH]
        self.max_stamina = stats[bn.MAX_STAMINA]
        self.max_damage = stats[cs.MAX_DAMAGE]
        self.min_damage = stats[cs.MIN_DAMAGE]
        self.accuracy = stats[cs.ACCURACY]
        self.critical_strike_chance = stats[cs.CRITICAL_STRIKE_CHANCE]

    def _init_start_parameters(self) -> None:
        self._equipped_weapon = Weapon(self._main_menu, 1, "fists.yml")
        self._no_weapon = True
        self.level = 1
        self.max_experience = 100
        self.experience = 0
        self.attribute_points = 3
        self.strength = 0
        self.agility = 0
        self.vitality = 0
        self.endurance = 0
        self.max_health = None
        self.health = None
        self.max_stamina = None
        self.stamina = None
        self.max_damage = None
        self.min_damage = None
        self.accuracy = None
        self.critical_strike_chance = None
        self.character_class = None
        self.health_multiplier = None
        self.stamina_multiplier = None
        self.agility_damage_multiplier = None
        self.strength_damage_multiplier = None
        self.critical_strike_chance_multiplier = None
        self.critical_strike_multiplier = None
        self.set_class(classes.PeasantClass)
        self.refresh_stats()
        self.health = self.max_health
        self.stamina = self.max_stamina

    def _calculate_damage(self, attack_type_damage_multiplier: float) -> Dict[str, float]:
        self.refresh_stats()
        max_damage = round(self.max_health * attack_type_damage_multiplier, 1)
        min_damage = round(self.min_damage * attack_type_damage_multiplier, 1)
        return {cs.MAX_DAMAGE: max_damage, cs.MIN_DAMAGE: min_damage}

    def _add_level(self) -> None:
        self.level += 1
        self.max_experience.MAX_EXPERIENCE = cf.max_experience_formula(level=self.level)
        self.attribute_points += 3
        if self._no_weapon:
            self._equipped_weapon = Weapon(self._main_menu, self.level, "fists.yml")
        self.refresh_stats()
        self.set_max_health()
        self.set_max_stamina()
        self._main_menu.character_menu.set_actual_character_stats()
        self._main_menu.character_menu.refresh_character_menu()
        self._add_log(self._text.LEVEL_UP)
        self._refresh_bars()
