from core.scenarios import BaseSituation
from core.items.weapon import (
    Dagger, DualDaggers, Sword, TwoHandedSword, DualSwords, BattleAxe, DualBattleAxes, TwoHandedBattleAxe,
    Mace, TwoHandedMace, DualMaces
)


class DebugSituation(BaseSituation):
    def __init__(self, main_menu, text) -> None:
        super().__init__(main_menu, text)
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        self._main_menu.main_character.send_experience(1000)
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_second_action(self) -> None:
        self._main_menu.inventory_menu.add_item(Dagger(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(DualDaggers(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(Sword(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(TwoHandedSword(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(DualSwords(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(BattleAxe(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(TwoHandedBattleAxe(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(DualBattleAxes(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(Mace(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(TwoHandedMace(1, self._main_menu))
        self._main_menu.inventory_menu.add_item(DualMaces(1, self._main_menu))

    def _event_third_action(self) -> None:
        self._main_menu.main_character.set_class_warrior()
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_fourth_action(self) -> None:
        self._main_menu.main_character.set_class_assassin()
        self._main_menu.character_menu.set_actual_character_stats()
