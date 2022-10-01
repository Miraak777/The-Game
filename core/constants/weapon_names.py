from dataclasses import dataclass


@dataclass(frozen=True)
class WeaponNames:
    DAGGER: str = "dagger"
    DUAL_DAGGERS: str = "dual_dagger"
    SWORD: str = "sword"
    TWO_HANDED_SWORD: str = "two_handed_sword"
    DUAL_SWORDS: str = "dual_swords"
    BATTLE_AXE: str = "battle_axe"
    TWO_HANDED_BATTLE_AXE: str = "two_handed_battle_axe"
    DUAL_BATTLE_AXE: str = "dual_battle_axe"
    MACE: str = "mace"
    TWO_HANDED_MACE: str = "two_handed_mace"
    DUAL_MACES: str = "dual_maces"
