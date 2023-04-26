def selection_sort(numbers: list):
    n = len(numbers)
    for i in range(n-1, 0, -1):
        max_index = i
        for j in range(i):
            if numbers[j] > numbers[max_index]:
                max_index = j
        numbers[max_index], numbers[i] = numbers[i], numbers[max_index]

numbers = [5, 2, 8, 3, 9, 1]
selection_sort(numbers)
print(numbers)

#2

def binary_search(text: list, target: str) -> str:
    """Searches for a word in a sorted list of words using binary search.

    Args:
        text (list): A sorted list of words.
        target (str): The word to search for.

    Returns:
        The word if found in the list, or None if not found.
    """
    low, high = 0, len(text) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = text[mid]
        if guess == target:
            return guess
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

text = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "orange"]
target = "banana"
result = binary_search(text, target)

if result is not None:
    print(f"{target} found in the list!")
else:
    print(f"{target} not found in the list.")

#3
class HashTable:
    def __init__(self, size):
        """Initializes a hash table with the given size.

        Args:
            size (int): The size of the hash table.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """Hashes the given key to an index in the hash table.

        Args:
            key (str): The key to be hashed.

        Returns:
            The index in the hash table.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table.

        Args:
            key (str): The key to be inserted.
            value (any): The value to be inserted.
        """
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def find(self, key):
        """Finds the value associated with the given key in the hash table.

        Args:
            key (str): The key to be searched.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Deletes the key-value pair associated with the given key in the hash table.

        Args:
            key (str): The key to be deleted.
        """
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return


ht = HashTable(10)
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)

print(ht.find("apple"))  # Output: 1
ht.delete("banana")
print(ht.find("banana"))  # Output: None

#4

class HashTable:
    def __init__(self, size):
        """Initializes a hash table with the given size.

        Args:
            size (int): The size of the hash table.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):
        """Hashes the given key to an index in the hash table.

        Args:
            key (str/int): The key to be hashed.

        Returns:
            The index in the hash table.
        """
        if isinstance(key, str):
            return len(key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            raise TypeError("Unsupported key type")

    def insert(self, key, value):
        """Inserts a key-value pair into the hash table.

        Args:
            key (str/int): The key to be inserted.
            value (any): The value to be inserted.
        """
        index = self.__my_hash(key)
        self.table[index].append((key, value))

    def find(self, key):
        """Finds the value associated with the given key in the hash table.

        Args:
            key (str/int): The key to be searched.

        Returns:
            The value associated with the key, or None if the key is not found.
        """
        index = self.__my_hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Deletes the key-value pair associated with the given key in the hash table.

        Args:
            key (str/int): The key to be deleted.
        """
        index = self.__my_hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return


ht = HashTable(10)
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)
ht.insert(100, 4)

print(ht.find("apple"))
print(ht.find(100))
ht.delete("banana")
print(ht.find("banana"))

#5

class HashTable:
    def __init__(self, size):
        """Initializes a hash table with the given size.

        Args:
            size (int): The size of the hash table.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):
        """Hashes the given key to an index in the hash table.

        Args:
            key (str/int): The key to be hashed.

        Returns:
            The index in the hash table.
        """
        if isinstance(key, str):
            return len(key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            raise TypeError("Unsupported key type")

    def put(self, key, data):
        """Inserts a key-value pair into the hash table.

        Args:
            key (str/int): The key to be inserted.
            data (any): The data to be inserted.
        """
        index = self.__my_hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, data)
                return
        bucket.append((key, data))


ht = HashTable(10)
ht.put("apple", 1)
ht.put("banana", 2)
ht.put("orange", 3)
ht.put(100, 4)

print(ht.table)
