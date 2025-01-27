class PredictInventory:
    def __init__(self, inventory):
        self.inventory = inventory

    def predict_inventory(self, product_id):
        msg = self.inventory.get_predict_stock_depletion(product_id)
        if msg[0]:
            print(f"{msg[1]} Days left")
            if msg[1] <= 7:
                print(f"This product will expire in {msg[1]} days.")
        else:
            print(msg)
