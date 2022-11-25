from typing import Dict

from core.constants.item_constants import StatNames
from core.constants.path_constants import Path, Paths
from core.enemies import Enemy


def get_enemy_table() -> Dict[str, int]:
    enemies_dir = Path(Paths.PATH_TO_ENEMIES)
    enemies_table = {}

    for enemy_file in enemies_dir.iterdir():
        enemy_file = enemy_file.name
        stats = Enemy.get_enemy_stats(enemy_file)
        enemies_table[enemy_file] = stats[StatNames.MIN_LEVEL]

    return enemies_table
