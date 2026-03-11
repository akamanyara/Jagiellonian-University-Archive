class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            pair = bucket[i]
            if pair[0] == key:
                bucket[i] = [key, value]
                return

        bucket.append([key, value])

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None
    
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return True
        return False

    # do testow i wizualizacji
    def display(self):
        for i in range(len(self.table)):
            print(f"Index {i}: {self.table[i]}")

# Przykład użycia
ht = HashTable(size=5)

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)

ht.display()
print("\nSearch for 'banana':", ht.search("banana"))

ht.delete("apple")

print()
ht.display()
