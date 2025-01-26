class Node:
    def __init__(self, product_id, product_information):
        self.key = product_id
        self.value = product_information
        self.right = None
        self.left = None
        self.height = 1


# Functions we need for AVL Tree
def get_height(node):
    if not node:
        return 0
    return node.height


def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


def right_rotation(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node

    # Update heights
    node.height = 1 + max(get_height(node.right), get_height(node.left))
    new_root = 1 + max(get_height(new_root.right), get_height(new_root.left))
    return new_root


def left_rotation(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node

    # Update heights
    node.height = 1 + max(get_height(node.right), get_height(node.left))
    new_root.height = 1 + max(get_height(new_root.left), get_balance(new_root.right))
    return new_root


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, product_id, product_information):
        if root is None:
            return Node(product_id, product_information)
        elif product_id < root.key:
            root.left = self.insert(root.left, product_id, product_information)
        elif product_id > root.key:
            root.right = self.insert(root.right, product_id, product_information)

        root.height = 1 + max(get_height(root.left), get_balance(root.right))

        balance_check = get_balance(root)

        # R rotate
        if balance_check > 1 and product_id < root.left.key:
            return right_rotation(root)

        # L rotate
        if balance_check < -1 and product_id > root.right.key:
            return left_rotation(root)

        # LR rotate
        if balance_check > 1 and product_id > root.left.key:
            root.left = left_rotation(root.left)
            return right_rotation(root)

        # RL rotate
        if balance_check < -1 and product_id < root.right.key:
            root.right = right_rotation(root.right)
            return left_rotation(root)

        return root

    # Function we need for delete method
    def get_min_node(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min_node(node.left)

    def delete(self, root, product_id):
        # Step 1: Perform the normal BST delete
        if root is None:
            return root
        elif product_id < root.key:
            self.delete(root.left, product_id)
        elif product_id > root.key:
            self.delete(root.right, product_id)
        else:
            # Case 1: Node with only one child or no child
            if root.left is None or root.right is None:
                temp = root.left if root.left is not None else root.right
                if temp is None:
                    temp = root
                    root = None
                else:
                    root = temp

            # Case 2: Node with two children: get the inorder successor (smallest in the right subtree)
            else:
                temp = self.get_min_node(root.right)
                root.key = temp.key
                root.value = temp.value
                root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        # Step 2: Update the height of the current node
        root.height = 1 + max(get_height(root.right), get_height(root.left))

        # Step 3: Get the balance factor of this node to check whether it became unbalanced
        balance_check = get_balance(root)

        # Step 4: If the node became unbalanced, then there are 4 cases

        # R rotate
        if balance_check > 1 and get_balance(root.left) >= 0:
            return right_rotation(root)

        # L rotate
        if balance_check < -1 and get_balance(root.right) <= 0:
            return left_rotation(root)

        # LR rotate
        if balance_check > 1 and get_balance(root.left) < 0:
            root.left = left_rotation(root.left)
            return right_rotation(root)

        # RL rotate
        if balance_check < -1 and get_balance(root.right) > 0:
            root.right = right_rotation(root.right)
            return left_rotation(root)

        return root

    def search(self, root, product_id):
        if root is None or product_id == root.key:
            return root
        elif product_id > root.key:
            return self.search(root.right, product_id)

        return self.search(root.left, product_id)
