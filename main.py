from data_structures.hash_map import HashMap
from functions.add_product import AddProduct
from functions.update_inventory import UpdateInventory
from functions.check_inventory import CheckInventory
from functions.low_stock_list import LowStockList
from functions.predict_inventory import PredictInventory


def main_menu():
    print("[0] Exit")
    print("[1] Add product")
    print("[2] Update inventory")
    print("[3] check_inventory")
    print("[4] List low stock")
    print("[5] Predict stock depletion")
    user_input = int(input("Select an option: "))
    return user_input


def main():
    user_input = main_menu()
    inventory = HashMap()
    add_product = AddProduct(inventory)
    update_inventory = UpdateInventory(inventory)
    check_inventory = CheckInventory(inventory)
    list_low_stock = LowStockList(inventory)
    predict_stock_depletion = PredictInventory(inventory)
    while True:
        if user_input == 0:
            return
        elif user_input == 1:
            product_id, *product_information = input("Enter product_info(Product_id, name, quantity, min_quantity,"
                                                     " daily_sales): ").split()
            product_information = list(map(lambda x: int(x) if x.isnumeric() else x, product_information))
            product_id = int(product_id)
            add_product.add_product(product_id, product_information)
        # elif user_input == 2:
        #     update_inventory.
        elif user_input == 3:
            product_id = int(input("Enter product_id: "))
            check_inventory.check_inventory(product_id)
        # elif user_input == 4:
        #     list_low_stock.
        # elif user_input == 5:
        #     predict_stock_depletion.
        else:
            print("Wrong option selected!")
            main_menu()
        user_input = main_menu()


if __name__ == "__main__":
    main()
