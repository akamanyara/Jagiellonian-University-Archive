class AVLNode:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T = x.right

        x.right = y
        y.left = T

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T = y.left

        y.left = x
        x.right = T

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def search(self, node, key):
        if not node or node.key == key:
            return node

        if key < node.key:
            return self.search(node.left, key)

        return self.search(node.right, key)

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        if not node:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def search_key(self, key):
        return self.search(self.root, key)

#test
avl = AVLTree()

avl.insert_key(10)
avl.insert_key(20)
avl.insert_key(30)

result = avl.search_key(20)
if result:
    print(f"Found: {result.key}")
else:
    print("Key not found")

avl.delete_key(20)

result = avl.search_key(20)
if result:
    print(f"Found: {result.key}")
else:
    print("Key not found")