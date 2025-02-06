class AddProduct:
    def __init__(self, inventory):
        self.inventory = inventory

    def add_product(self, product_id, product_information):
        msg = self.inventory.set_product(product_id, product_information)
        print(msg)
