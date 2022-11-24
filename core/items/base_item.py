class BaseItem:
    def __init__(self, main_menu):
        self._main_menu = main_menu
        self._language = main_menu.language
        self.item_type = None
        self.item_icon = None
        self.item_inventory_id = None
        self.item_equipped = False
        self.description = None

    def use_item(self):
        pass

    def get_description_stats(self):
        pass
