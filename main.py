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
    add = AddProduct(inventory)
    update = UpdateInventory(inventory)
    check = CheckInventory(inventory)
    low_stock = LowStockList(inventory)
    predict_stock = PredictInventory(inventory)
    while True:
        if user_input == 0:
            return
        elif user_input == 1:
            product_id, *product_information = input("Enter product_info(Product_id, name, quantity, min_quantity,"
                                                     " daily_sales): ").split()
            product_information = list(map(lambda x: int(x) if x.isnumeric() else x, product_information))
            product_id = int(product_id)
            add.add_product(product_id, product_information)
        elif user_input == 2:
            product_id, quantity_change = list(map(int, input("Enter product_id and quantity for changing: ").split()))
            update.update_inventory(product_id, quantity_change)
        elif user_input == 3:
            product_id = int(input("Enter product_id: "))
            check.check_inventory(product_id)
        elif user_input == 4:
            low_stock.low_stock_list()
        elif user_input == 5:
            product_id = int(input("Enter product_id: "))
            predict_stock.predict_inventory(product_id)
        else:
            print("Wrong option selected!")
            main_menu()
        user_input = main_menu()
        print("-"*30)


if __name__ == "__main__":
    main()
