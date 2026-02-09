class HashTable:
    """
    Hash Table implementation using chaining for collision resolution.

    Expected Time Complexity (under simple uniform hashing):
        Insert: O(1 + α)
        Search: O(1 + α)
        Delete: O(1 + α)

    Where:
        α (load factor) = number_of_elements / table_size
    """

    def __init__(self, size=10):
        """
        Initializes the hash table.

        Parameters:
            size: number of buckets in the hash table
        """
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        """
        Hash function using Python's built-in hash.

        Returns:
            Index of the bucket
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts or updates a key-value pair.
        """
        index = self._hash(key)

        # Check if key already exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        # Otherwise, add new key-value pair
        self.table[index].append([key, value])
        self.count += 1

    def search(self, key):
        """
        Searches for a value associated with a key.

        Returns:
            Value if found, else None
        """
        index = self._hash(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table.

        Returns:
            True if deleted, False if key not found
        """
        index = self._hash(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                self.count -= 1
                return True

        return False

    def load_factor(self):
        """
        Computes the current load factor of the hash table.
        """
        return self.count / self.size
