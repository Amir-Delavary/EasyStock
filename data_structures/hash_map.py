from data_structures.avl_tree import AVLTree
from data_structures.priority_queue import PriorityQueue


class HashMap:
    def __init__(self, size=50):
        self.size = size
        self.hash_map = self.create_hash_map()
        self.priority_queue = PriorityQueue()

    def create_hash_map(self):
        return [AVLTree() for _ in range(self.size)]

    def hash_key(self, key):
        return hash(key) % self.size

    def set_product(self, product_id, product_information):
        hashed_key = self.hash_key(product_id)
        avl_tree = self.hash_map[hashed_key]
        existing_node = avl_tree.search(avl_tree.root, product_id)
        if existing_node:
            return "This product ID already has been used."

        avl_tree.root = avl_tree.insert(avl_tree.root, product_id, product_information)
        self.priority_queue.push(product_id, product_information)

        return "Product added successfully!"

    def update_product(self, product_id, quantity):
        hashed_key = self.hash_key(product_id)
        avl_tree = self.hash_map[hashed_key]
        node = avl_tree.search(avl_tree.root, product_id)
        if node:
            node.value[1] += quantity
            self.priority_queue.heapify()
            return "Product quantity update successfully!"
        return "Product with this ID not found"

    def get_product_information(self, product_id):
        hashed_key = self.hash_key(product_id)
        avl_tree = self.hash_map[hashed_key]
        node = avl_tree.search(avl_tree.root, product_id)
        if node:
            return node.value
        return "product not found with this id"

    def delete_product(self, product_id):
        hashed_key = self.hash_key(product_id)
        avl_tree = self.hash_map[hashed_key]
        existing_node = avl_tree.search(avl_tree.root, product_id)
        if not existing_node:
            return "Product not found with this id"

        avl_tree.root = avl_tree.delete(avl_tree.root, product_id)

        self.priority_queue.remove(product_id)
        return "product deleted"

    def get_predict_stock_depletion(self, product_id):
        hashed_key = self.hash_key(product_id)
        avl_tree = self.hash_map[hashed_key]
        node = avl_tree.search(avl_tree.root, product_id)
        if node:
            name, quantity, min_quantity, daily_sales = node.value
            predict = quantity // daily_sales
            return True, predict
        return False, "product not found"

    def get_low_stock_products(self):
        return self.priority_queue.get_low_stock_products()
