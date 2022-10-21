from .base_consumable import BaseFood
from .texts import Text


class Apple(BaseFood):
    def __init__(self, main_menu, level):
        super().__init__(main_menu=main_menu, level=level)
        self.stats.NAME = Text[self._language].APPLE
        self.item_icon = "apple.png"
        self.heal = 10


class Steak(BaseFood):
    def __init__(self, main_menu, level):
        super().__init__(main_menu=main_menu, level=level)
        self.stats.NAME = Text[self._language].STEAK
        self.item_icon = "steak.png"
        self.heal = 25


class Pie(BaseFood):
    def __init__(self, main_menu, level):
        super().__init__(main_menu=main_menu, level=level)
        self.stats.NAME = Text[self._language].PIE
        self.item_icon = "pie.png"
        self.heal = 50
