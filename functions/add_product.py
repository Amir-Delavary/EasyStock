class AddProduct:
    def __init__(self, inventory):
        self.inventory = inventory

    def add_product(self, product_id, name, quantity, min_quantity, daily_sales):
        product_information = [name, min_quantity, quantity, daily_sales]
        self.inventory.set_product(product_id, product_information)
