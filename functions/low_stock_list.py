class LowStockList:
    def __init__(self, inventory):
        self.inventory = inventory

    def low_stock_list(self):
        products = self.inventory.get_low_stock_products()
        for index, product in enumerate(products):
            product_id, product_information = product
            name, quantity, min_quantity, daily_sales = product_information
            print(f"Product ID: {product_id}, Name: {name}, Quantity: {quantity}, MinQuantity: {min_quantity},"
                  f" DailySales: {daily_sales}")
