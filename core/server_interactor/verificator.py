from .interactor import get_server_resources_list
from core.constants.server_constants import ResourcesConstants
from core.constants.path_constants import Paths


def get_client_resources_list() -> dict[str, list[str]]:
    resources_list = {
        ResourcesConstants.WEAPONS: [],
        ResourcesConstants.CONSUMABLES: [],
        ResourcesConstants.ENEMIES: [],
        ResourcesConstants.SCENARIOS: [],
    }
    for weapon_file in Paths.PATH_TO_WEAPONS.iterdir():
        resources_list[ResourcesConstants.WEAPONS].append(weapon_file.name)
    for consumables_file in Paths.PATH_TO_CONSUMABLES.iterdir():
        resources_list[ResourcesConstants.CONSUMABLES].append(consumables_file.name)
    for enemy_file in Paths.PATH_TO_ENEMIES.iterdir():
        resources_list[ResourcesConstants.ENEMIES].append(enemy_file.name)
    for scenarios_file in Paths.PATH_TO_SCENARIOS.iterdir():
        resources_list[ResourcesConstants.SCENARIOS].append(scenarios_file.name)
    return resources_list


def verify_resources_lists() -> bool:
    client_resources_list = get_client_resources_list()
    server_resources_list = get_server_resources_list()
    return client_resources_list == server_resources_list
