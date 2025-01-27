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
    user_input = input("Select an option: ")
    return user_input


def main():
    user_input = main_menu()
    inventory = HashMap()
    add_product = AddProduct(inventory)
    update_inventory = UpdateInventory(inventory)
    check_inventory = CheckInventory(inventory)
    list_low_stock = LowStockList(inventory)
    predict_stock_depletion = PredictInventory(inventory)
    if user_input == 0:
        return
    elif user_input == 1:
        add_product.add_product()
    elif user_input == 2:
        update_inventory.
    elif user_input == 3:
        check_inventory.
    elif user_input == 4:
        list_low_stock.
    elif user_input == 5:
        predict_stock_depletion.
    else:
        print("Wrong option selected!")
        main_menu()


if __name__ == "__main__":
    main()
