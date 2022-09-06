from dataclasses import dataclass


@dataclass(frozen=True)
class CharacterMenuText:
    TITLE: str = " Меню персонажа"
    GENERAL: str = " Общие: "
    NAME: str = " Имя: "
    LEVEL: str = " Уровень: "
    CLASS: str = " Класс: "
    BARS: str = " Показатели:"
    HEALTH: str = " Здоровье: "
    STAMINA: str = " Запас сил: "
    ATTRIBUTES: str = " Атрибуты:"
    STRENGTH: str = " Сила: "
    AGILITY: str = " Ловкость: "
    VITALITY: str = " Живучесть: "
    ENDURANCE: str = " Выносливость: "
    ATTRIBUTE_POINTS: str = " Очки атрибутов: "
    STATS: str = " Параметры:"
    DAMAGE: str = " Урон: "
    CRITICAL_STRIKE_CHANCE: str = " Шанс крита: "
    CRITICAL_STRIKE_MULTIPLIER: str = " Множитель крита: "
    ACCURACY: str = " Меткость: "


@dataclass(frozen=True)
class MainMenuText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Создайте персонажа!"
    CHARACTER_NAME_PLACEHOLDER: str = "Введите имя вашего персонажа"
