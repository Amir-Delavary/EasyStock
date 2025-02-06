from collections.abc import Iterable


class CheckInventory:
    def __init__(self, inventory):
        self.inventory = inventory

    def check_inventory(self, product_id):
        msg = self.inventory.get_product_information(product_id)
        if isinstance(msg, Iterable):
            name, quantity, min_quantity, daily_sales = msg
            print(f"Product ID: {product_id}, Name: {name}, Quantity: {quantity}, MinQuantity: {min_quantity},"
                  f" DailySales: {daily_sales}")
        else:
            print(msg)
