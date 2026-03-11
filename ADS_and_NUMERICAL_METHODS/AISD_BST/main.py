class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):

        if self.root is None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if key < current.key:
                    if current.left is None:
                        current.left = Node(key)
                        break
                    else:
                        current = current.left
                elif key > current.key:
                    if current.right is None:
                        current.right = Node(key)
                        break
                    else:
                        current = current.right
                else:
                    break

    def contains(self, key):

        current = self.root
        while current:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, key):

        parent = None
        current = self.root

        # find node we want to delete
        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        # case: node wasn't found
        if current is None:
            return

        # delete the node ( 3 cases )

        # case 1: node without children
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # case 2: node with one child
        elif current.left is None or current.right is None:
            child = current.left if current.left else current.right
            if current == self.root:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

        # case 3: node with both children
        else:
            # suc - successor node for our deleted one ( minimum from the right )
            suc_parent = current
            suc = current.right
            while suc.left:
                suc_parent = suc
                suc = suc.left
            
            # set current as found successor 
            current.key = suc.key

            # delete the successor node
            if suc_parent.left == suc:
                suc_parent.left = suc.right
            else:
                suc_parent.right = suc.right

    # for testing 
    def printing_inorder(self):
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.key)
                inorder(node.right)
        inorder(self.root)
        return result

# Example usage
bst = BST()
bst.insert(8)
bst.insert(2)
bst.insert(23)
bst.insert(1)
print(bst.contains(10))
print(bst.contains(23))
bst.delete(10)
bst.delete(1)
print(bst.contains(1))
print(bst.printing_inorder())