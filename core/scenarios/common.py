from yaml import safe_load
from core.constants.path_constants import Path, Paths


def read_scenario_stats(scenario_file_name: str) -> dict[str, any]:
    with open(str(Path(Paths.PATH_TO_SCENARIOS, scenario_file_name)), "r", encoding="utf-8") as scenario_file:
        stats = safe_load(scenario_file)
        return stats
