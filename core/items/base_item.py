class BaseItem:
    def __init__(self, main_menu) -> None:
        self.main_menu = main_menu
        self._language = main_menu.language
        self.item_type = None
        self.item_icon = None
        self.item_inventory_id = None
        self.item_equipped = False
        self.description = None
        self.rarity = None

    def use_item(self) -> None:
        pass

    def get_description_stats(self) -> None:
        pass
