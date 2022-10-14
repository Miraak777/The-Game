class BaseItem:
    def __init__(self, main_menu):
        self._main_menu = main_menu
        self.item_type = None
        self.item_icon = None

    def use_item(self):
        pass