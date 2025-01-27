class UpdateInventory:
    def __init__(self, inventory):
        self.inventory = inventory

    def update_inventory(self, product_id, quantity_change):
        msg = self.inventory.update_product(product_id, quantity_change)
        print(msg)