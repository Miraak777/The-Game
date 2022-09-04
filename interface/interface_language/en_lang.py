from dataclasses import dataclass


@dataclass(frozen=True)
class CharacterMenuText:
    TITLE: str = "Character menu"
    NAME: str = "Name:"
    LEVEL: str = "Level:"
    CLASS: str = "Class:"
    BARS: str = "Bars:"
    HEALTH: str = " Health:"
    STAMINA: str = " Stamina:"
    ATTRIBUTES: str = "Attributes:"
    STRENGTH: str = " Strength:"
    AGILITY: str = " Agility:"
    VITALITY: str = " Vitality:"
    ENDURANCE: str = " Endurance:"
    STATS: str = "Stats:"
    DAMAGE: str = " Damage:"
    CRITICAL_STRIKE_CHANCE: str = " Crit. Chance:"
    CRITICAL_STRIKE_MULTIPLIER: str = " Crit. Multiplier:"
    ACCURACY: str = " Accuracy:"


@dataclass(frozen=True)
class MainMenuText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Create Character!"
    CHARACTER_NAME_PLACEHOLDER: str = "Enter your character name"
