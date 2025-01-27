class CheckInventory:
    def __init__(self, inventory):
        self.inventory = inventory

    def check_inventory(self, product_id):
        msg = self.inventory.get_product_information(product_id)
        print(msg)
