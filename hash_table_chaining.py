class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

# Test and Performance Analysis
def main():
    hash_table = HashTableChaining(100)
    keys = [f"key{i}" for i in range(50)]
    values = [i * 2 for i in range(50)]

    print("Inserting key-value pairs...")
    for k, v in zip(keys, values):
        hash_table.insert(k, v)

    print("Testing search operation...")
    for k in keys:
        print(f"Search {k}: {hash_table.search(k)}")

    print("Deleting some keys...")
    for k in keys[:10]:
        hash_table.delete(k)

    print("Re-testing search after deletion...")
    for k in keys[:10]:
        print(f"Search {k}: {hash_table.search(k)}")

    print("Hash table operation completed.")

if __name__ == "__main__":
    main()
