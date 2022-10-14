from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FISTS: str = "Fists"
    DAGGER: str = "Dagger"
    DUAL_DAGGERS: str = "Dual Daggers"
    SWORD: str = "Sword"
    TWO_HANDED_SWORD: str = "Two handed Sword"
    DUAL_SWORDS: str = "Dual Swords"
    BATTLE_AXE: str = "Battle Axe"
    TWO_HANDED_BATTLE_AXE: str = "Two handed Battle Axe"
    DUAL_BATTLE_AXES: str = "Dual Battle Axes"
    MACE: str = "Mace"
    TWO_HANDED_MACE: str = "Two handed Mace"
    DUAL_MACES: str = "Dual Maces"


@dataclass(frozen=True)
class RussianText:
    FISTS: str = "Кулаки"
    DAGGER: str = "Кинжал"
    DUAL_DAGGERS: str = "Парные Кинжалы"
    SWORD: str = "Меч"
    TWO_HANDED_SWORD: str = "Двуручный Меч"
    DUAL_SWORDS: str = "Парные Мечи"
    BATTLE_AXE: str = "Боевой Топор"
    TWO_HANDED_BATTLE_AXE: str = "Двуручный Боевой Топор"
    DUAL_BATTLE_AXES: str = "Парные Боевые Топоры"
    MACE: str = "Булава"
    TWO_HANDED_MACE: str = "Двуручная Булава"
    DUAL_MACES: str = "Парные Булавы"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
