from .constants import Paths, Path, ResourcesConstants
from flask import Flask
from flask_cors import CORS
from yaml import safe_load

cors = CORS()


def load_file(file_name: str) -> bytes:
    with open(str(Path(Paths.PATH_TO_RESOURCES, file_name)), "rb") as file:
        file_data = file.read()
        return file_data


def get_config() -> dict[str, any]:
    with open(Paths.PATH_TO_CONFIG, "r") as config_file:
        configs = safe_load(config_file)
        return configs


def get_resources_list() -> dict[str, list[str]]:
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


def get_app() -> Flask:
    app = Flask("game-server")
    cors.init_app(app)
    return app

get_resources_list()