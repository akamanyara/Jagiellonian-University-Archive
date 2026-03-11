def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    return x

def rotate_left(x):
    y = x.right
    x.right = y.left
    y.left = x
    return y

class SplayTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def splay(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            if not root.left:
                return root

            if key < root.left.key:
                root.left.left = self.splay(root.left.left, key)
                root = rotate_right(root)
            elif key > root.left.key:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right:
                    root.left = rotate_left(root.left)

            return rotate_right(root) if root.left else root

        else:
            if not root.right:
                return root

            if key > root.right.key:
                root.right.right = self.splay(root.right.right, key)
                root = rotate_left(root)
            elif key < root.right.key:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = rotate_right(root.right)

            return rotate_left(root) if root.right else root

    def search(self, key):
        self.root = self.splay(self.root, key)
        return self.root.key if self.root and self.root.key == key else None

    def insert(self, key):
        if not self.root:
            self.root = SplayTreeNode(key)
            return

        self.root = self.splay(self.root, key)

        if self.root.key == key:
            return

        new_node = SplayTreeNode(key)
        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def delete(self, key):
        if not self.root:
            return

        self.root = self.splay(self.root, key)

        if self.root.key != key:
            return

        if not self.root.left:
            self.root = self.root.right
        else:
            temp = self.root.right
            self.root = self.splay(self.root.left, key)
            self.root.right = temp

# example usage:
st = SplayTree()
st.insert(10)
st.insert(20)
st.insert(5)
print(st.search(10))  # 10
st.delete(10)
print(st.search(10))  # None
