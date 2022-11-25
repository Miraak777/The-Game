from random import randrange

from core.items.tables import get_weapon_table
from core.items.weapon import Weapon
from core.main_character.classes import AssassinClass, WarriorClass
from core.scenarios import BaseSituation


class DebugSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        scenario = self._main_menu.random_scenario.get_random_scenario()
        scenario(self._main_menu)

    def _event_second_action(self) -> None:
        weapon_list = get_weapon_table()
        for weapon in weapon_list:
            if weapon != "fists.yml":
                self._main_menu.inventory_menu.add_item(
                    Weapon(self._main_menu, self._main_menu.main_character.level, weapon, randrange(0, 8))
                )

    def _event_third_action(self) -> None:
        self._main_menu.main_character.set_class(WarriorClass)
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_fourth_action(self) -> None:
        self._main_menu.main_character.set_class(AssassinClass)
        self._main_menu.character_menu.set_actual_character_stats()
