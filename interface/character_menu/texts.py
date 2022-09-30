from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    GENERAL: str = "General: "
    NAME: str = " Name: "
    LEVEL: str = " Level: "
    CLASS: str = " Class: "
    BARS: str = "Bars:"
    HEALTH: str = " Health: "
    STAMINA: str = " Stamina: "
    ATTRIBUTES: str = "Attributes:"
    STRENGTH: str = " Strength: "
    AGILITY: str = " Agility: "
    VITALITY: str = " Vitality: "
    ENDURANCE: str = " Endurance: "
    ATTRIBUTE_POINTS: str = " Attribute Points: "
    STATS: str = "Stats:"
    DAMAGE: str = " Damage: "
    CRITICAL_STRIKE_CHANCE: str = " Crit. Chance: "
    CRITICAL_STRIKE_MULTIPLIER: str = " Crit. Multiplier: "
    ACCURACY: str = " Accuracy: "
    ACCEPT: str = "Accept"
    PEASANT: str = "Peasant"
    WARRIOR: str = "Warrior"
    ASSASSIN: str = "Assassin"


@dataclass(frozen=True)
class RussianText:
    GENERAL: str = "Общие: "
    NAME: str = " Имя: "
    LEVEL: str = " Уровень: "
    CLASS: str = " Класс: "
    BARS: str = "Показатели:"
    HEALTH: str = " Здоровье: "
    STAMINA: str = " Запас сил: "
    ATTRIBUTES: str = "Атрибуты:"
    STRENGTH: str = " Сила: "
    AGILITY: str = " Ловкость: "
    VITALITY: str = " Живучесть: "
    ENDURANCE: str = " Выносливость: "
    ATTRIBUTE_POINTS: str = " Очки атрибутов: "
    STATS: str = "Параметры:"
    DAMAGE: str = " Урон: "
    CRITICAL_STRIKE_CHANCE: str = " Шанс крита: "
    CRITICAL_STRIKE_MULTIPLIER: str = " Множитель крита: "
    ACCURACY: str = " Меткость: "
    ACCEPT: str = "Принять"
    PEASANT: str = "Крестьянин"
    WARRIOR: str = "Воин"
    ASSASSIN: str = "Убийца"


Text = {Language.EN: EnglishText, Language.RU: RussianText}
