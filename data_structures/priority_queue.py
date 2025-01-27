import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, product_id, product_information):
        priority = abs(product_information[1] - product_information[2])
        heapq.heappush(self.queue, (priority, product_id, product_information))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]

    def get_all(self):
        return sorted(self.queue)

    def remove(self, product_id):
        for index, (priority, key, value) in enumerate(self.queue):
            if key == product_id:
                del self.queue[index]
                heapq.heapify(self.queue)
                return None

    def heapify(self):
        heapq.heapify(self.queue)

    def get_low_stock_products(self):
        low_stock_products = []
        for _, product_id, product_information in self.queue:
            if product_information[1] <= product_information[2]:
                low_stock_products.append((product_id, product_information))
        return low_stock_products
