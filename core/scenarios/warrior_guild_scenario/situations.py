from core.constants.actions_constants import ActionButtons
from core.enemies import Enemy
from core.main_character.classes import WarriorClass
from core.scenarios import BaseSituation, BattleSituation, ChillScenario


class MeetSituation(BaseSituation):
    def __init__(self, main_menu, text, scenario) -> None:
        super().__init__(main_menu, text)

        self._scenario = scenario
        self._texts = {
            ActionButtons.FIRST_ACTION: self._text.IM_FROM_VILLAGE,
            ActionButtons.SECOND_ACTION: self._text.IM_NOT_FROM_VILLAGE,
            ActionButtons.THIRD_ACTION: self._text.ATTACK,
            ActionButtons.FOURTH_ACTION: self._text.LEAVE,
        }
        self._log(self._text.INTRODUCTION)
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        self._log("")
        self._log(self._text.IM_FROM_VILLAGE_LOG)
        self._log(self._text.IM_FROM_VILLAGE_ANSWER)
        AskToJoin(self._main_menu, self._text, self._scenario)

    def _event_second_action(self) -> None:
        self._log("")
        self._log(self._text.IM_NOT_FROM_VILLAGE_LOG)
        self._log(self._text.IM_NOT_FROM_VILLAGE_ANSWER)
        AskToJoin(self._main_menu, self._text, self._scenario)

    def _event_third_action(self) -> None:
        self._log("")
        sentry = Enemy(
            main_menu=self._main_menu,
            level=self._main_menu.main_character.main_stats.level + 10,
            enemy_file_name="human_with_sword",
        )
        sentry.name = self._text.SENTRY
        BattleSituation(self._main_menu, sentry)

    def _event_fourth_action(self) -> None:
        ChillScenario(self._main_menu)


class AskToJoin(BaseSituation):
    def __init__(self, main_menu, text, scenario):
        super().__init__(main_menu, text)
        self._scenario = scenario
        self._texts = {
            ActionButtons.FIRST_ACTION: self._text.ASK_FOR_JOIN,
            ActionButtons.SECOND_ACTION: self._text.SECOND_ACTION,
            ActionButtons.THIRD_ACTION: self._text.THIRD_ACTION,
            ActionButtons.FOURTH_ACTION: self._text.LEAVE,
        }
        self.refresh_buttons()

    def _event_first_action(self) -> None:
        self._log("")
        self._log(self._text.ASK_FOR_JOIN_LOG)
        self._log(self._text.ASK_FOR_JOIN_ANSWER)
        self._scenario.main_character_weapon = self._main_menu.main_character.unequip_weapon()
        DerickBattleSituation(self._main_menu, self._scenario, self._text)

    def _event_fourth_action(self) -> None:
        ChillScenario(self._main_menu)


class DerickBattleSituation(BattleSituation):
    def __init__(self, main_menu, scenario, text):
        self._won_text = text.WON
        self._scenario = scenario
        derick = Enemy(main_menu.main_character.main_stats.LEVEL, main_menu, "human.yml")
        derick.name = text.DERICK
        super().__init__(main_menu=main_menu, enemy=derick)
        self._texts[ActionButtons.FOURTH_ACTION] = ""
        self.refresh_buttons()

    def _event_fourth_action(self) -> None:
        pass

    def _generate_reward(self):
        self._log(self._won_text)
        self._main_menu.main_character.equip_weapon(self._scenario.main_character_weapon)
        self._main_menu.main_character.set_class(WarriorClass)
        self._main_menu.main_character.send_experience(2500)
        ChillScenario(self._main_menu)
