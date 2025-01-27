from itertools import product


class LowStockList:
    def __init__(self, inventory):
        self.inventory = inventory

    def low_stock_list(self):
        products = self.inventory.get_low_stock_products()
        print(products)
