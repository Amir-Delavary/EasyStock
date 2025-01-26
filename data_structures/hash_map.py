from data_structures.avl_tree import AVLTree


class HashMap:
    def __init__(self, size=50):
        self.size = size
        self.hash_map = self.create_hash_map()

    def create_hash_map(self):
        return [[] for _ in range(self.size)]

    def hash_key(self, key):
        return hash(key) % self.size

    def set_product(self, product_id, product_information):
        hashed_key = self.hash_key(product_id)
        bucket = self.hash_map[hashed_key]
        for index, product in enumerate(bucket):
            # in every bucket of hash_map we have 2 things: key = product_id and value = product_information
            key, value = product
            if key == product_id:
                return "This product_id used before this! try with another id"
        bucket.append((product_id, product_information))

    def update_product(self, product_id, product_information):
        hashed_key = self.hash_key(product_id)
        bucket = self.hash_map[hashed_key]
        for index, product in enumerate(bucket):
            key, value = product
            if key == product_id:
                bucket[index] = (product_id, product_information)
                return "product information updated!"
        return "product_id not found"

    def get_product_information(self, product_id):
        hashed_key = self.hash_key(product_id)
        bucket = self.hash_map[hashed_key]
        for index, product in enumerate(bucket):
            key, value = product
            if key == product_id:
                return value
        return "product not found with this id"

    def delete_product(self, product_id):
        hashed_key = self.hash_key(product_id)
        bucket = self.hash_map[hashed_key]
        for index, product in enumerate(bucket):
            key, value = product
            if key == product_id:
                del (bucket[index])
                return "product_deleted"
        return "product not found with this product_id"
