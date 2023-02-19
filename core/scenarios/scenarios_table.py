from core.constants.path_constants import Path, Paths
from .common import read_scenario_stats
from .constants import ScenarioStats as ss


def get_scenarios_table() -> dict[int, str]:
    scenarios_dir = Path(Paths.PATH_TO_SCENARIOS)
    scenarios_table = {}

    for scenario_file in scenarios_dir.iterdir():
        scenario_file = scenario_file.name
        stats = read_scenario_stats(scenario_file)
        scenarios_table[stats[ss.REQUIRED_LEVEL]] = scenario_file

    return scenarios_table
