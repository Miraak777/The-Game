from core.constants.path_constants import Paths, Path
from core.items import Weapon, Consumable
from core.constants.item_constants import StatNames


def get_weapon_table():
    weapon_dir = Path(Paths.PATH_TO_WEAPONS)
    weapon_table = {}

    for weapon_file in weapon_dir.iterdir():
        weapon_file = weapon_file.name
        stats = Weapon.get_weapon_stats(weapon_file)
        weapon_table[weapon_file] = stats[StatNames.WEAPON_TYPE]

    return weapon_table


def get_consumables_table():
    consumable_dir = Path(Paths.PATH_TO_CONSUMABLES)
    consumable_table = {}

    for consumable_file in consumable_dir.iterdir():
        consumable_file = consumable_file.name
        stats = Consumable.get_consumable_stats(consumable_file)
        consumable_table[consumable_file] = stats[StatNames.CONSUMABLE_TYPE]

    return consumable_table

