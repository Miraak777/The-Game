from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = "Light Attack"
    SECOND_ACTION: str = "Medium Attack"
    THIRD_ACTION: str = "Heavy Attack"
    FOURTH_ACTION: str = "Retreat"
    DAMAGE: str = "Damage: "
    STAMINA_CONSUMPTION: str = "Stamina consumption: "
    BATTLE_START: str = "You've been attacked by"
    HEALTH: str = "Health: "
    YOUR_HEALTH: str = "Your health: "
    YOUR_STAMINA: str = "Your stamina: "
    LEVEL: str = "Lvl"
    YOU_FOUNDED: str = "You founded "
    EQUIP_WEAPON: str = "Equip weapon"
    QUIT_WEAPON: str = "Quit the weapon"
    YOU_EQUIPPED: str = "You equipped "
    YOU_QUITED: str = "You quited "


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = "Лёгкая атака"
    SECOND_ACTION: str = "Средняя атака"
    THIRD_ACTION: str = "Тяжелая атака"
    FOURTH_ACTION: str = "Отступить"
    DAMAGE: str = "Урон: "
    STAMINA_CONSUMPTION: str = "Затраты запаса сил: "
    BATTLE_START: str = "На вас напал"
    HEALTH: str = "Здоровье: "
    YOUR_HEALTH: str = "Ваше здоровье: "
    YOUR_STAMINA: str = "Ваш запас сил: "
    LEVEL: str = "Ур."
    YOU_FOUNDED: str = "Вы нашли "
    EQUIP_WEAPON: str = "Использовать оружие"
    QUIT_WEAPON: str = "Выбросить оружие"
    YOU_EQUIPPED: str = "Теперь вы используете "
    YOU_QUITED: str = "Вы выбросили "


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
