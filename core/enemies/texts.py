from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    HUMAN: str = "Human"
    HUMAN_WITH_DAGGER: str = "Assassin"
    HUMAN_WITH_SWORD: str = "Swordsmen"
    GOBLIN: str = "Goblin"
    GOBLIN_WITH_DAGGER: str = "Goblin with a Dagger"
    TROLL: str = "Troll"
    ARMED_TROLL: str = "Armed Troll"
    TAKEN: str = "took"
    DEAL: str = "dealt"
    DAMAGE: str = "damage"
    DIED: str = "died"


@dataclass(frozen=True)
class RussianText:
    HUMAN: str = "Человек"
    HUMAN_WITH_DAGGER: str = "Убийца"
    HUMAN_WITH_SWORD: str = "Мечник"
    GOBLIN: str = "Гоблин"
    GOBLIN_WITH_DAGGER: str = "Гоблин с Кинжалом"
    TROLL: str = "Тролль"
    ARMED_TROLL: str = "Вооруженный Тролль"
    TAKEN: str = "получил"
    DEAL: str = "нанёс"
    DAMAGE: str = "единиц урона"
    DIED: str = "умер"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
