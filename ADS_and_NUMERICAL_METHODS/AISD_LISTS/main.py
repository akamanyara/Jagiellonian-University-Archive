# jednokierunkowa lista wskaznikowa
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleList: 
    def __init__(self):
        self.head = None

    def insert(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def delete(self, x):
        current = self.head
        prev = None 

        while current: 
            if current.value == x:
                if prev:
                    prev.next = current.next
                else: 
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def contains(self, x): 
        current = self.head
        while current:
            if current.value == x:
                return True
            current = current.next
        return False
    
# dwukierunkowa lista wskaznikowa
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.head = None

    def insert(self, x):
        new_node = DoubleNode(x)
        new_node.next = self.head
        if self.head: 
            self.head.prev = new_node
        self.head = new_node

    def delete(self, x):
        current = self.head

        while current: 
            if current.value == x:
                if current.prev: 
                    current.prev.next = current.next
                if current.next: 
                    current.next.prev = current.prev
                if current == self.head:
                    self.head == current.next
                return True
            current = current.next 
        return False
    
    def contains(self, x):
        current = self.head

        while current:
            if current.value == x:
                return True
            current = current.next
        return False

# lista kursorowa ( tablice przechowuja nasze wskazniki )
    
class CursorNode:
    def __init__(self, value, next_index=None):
        self.value = value
        self.next_index = next_index

class CursorList:
    def __init__(self):
        self.nodes = []  # Tablica przechowująca nodes
        self.head_index = None

    def insert(self, x):
        new_node = CursorNode(x, self.head_index)
        self.nodes.append(new_node)
        self.head_index = len(self.nodes) - 1
    
    def delete(self, x):
        current_index = self.head_index
        prev_index = None

        while current_index is not None:
            current_node = self.nodes[current_index]
            if current_node.value == x:
                if prev_index is not None:
                    self.nodes[prev_index].next_index = current_node.next_index
                else:
                    self.head_index = current_node.next_index
                return True
            prev_index = current_index
            current_index = current_node.next_index
        return False
    
    def contains(self, x):
        current_index = self.head_index
        while current_index is not None:
            current_node = self.nodes[current_index]
            if current_node.value == x:
                return True
            current_index = current_node.next_index
        return False
    

# szybkie testy do sprawdzenia dzialania 
# insert - dodajemy element
# delete - usuwamy element i dla informacji zwracamy true or false 
# contains - zwraca bool jesli element znajduje sie w liscie 
    
if __name__ == "__main__":
    print("Lista jednokierunkowa:")
    sl = SingleList()
    sl.insert(1)
    sl.insert(2)
    sl.insert(3)
    print(sl.contains(2))  # True
    print(sl.delete(2))    # True
    print(sl.contains(2))  # False

    print("\nLista dwukierunkowa:")
    dl = DoubleList()
    dl.insert(1)
    dl.insert(2)
    dl.insert(3)
    print(dl.contains(2))  # True
    print(dl.delete(2))    # True
    print(dl.contains(2))  # False

    print("\nLista kursorowa:")
    cl = CursorList()
    cl.insert(1)
    cl.insert(2)
    cl.insert(3)
    print(cl.contains(2))  # True
    print(cl.delete(2))    # True
    print(cl.contains(2))  # False