from .constants import InventoryMenuSizes

inventory_map = {}
for i in range(InventoryMenuSizes.ITEMS_VERTICAL_NUMBER * InventoryMenuSizes.ITEMS_HORIZONTAL_NUMBER):
    inventory_map[i] = None
