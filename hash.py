import csv
import numpy as np

'''
HashEntry:
key -> String 
value -> Object
state -> int (0-never used, 1=used, -1=formely used)
'''


class DSAHashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.state = 1

# Hash Table Definition


class DSAHashTable:
    def __init__(self, size):
        self.size = size
        self.hashArray = np.empty(size, dtype=object)
        self.count = 0
        self.loadFactorUpper = 0.75
        self.loadFactorLower = 0.25

    def hash(self, key):
        # Hash function
        hashIndex = 0
        for char in key:
            hashIndex = (33 * hashIndex + ord(char)) % len(self.hashArray)
        return hashIndex

    # checks whether the size of the hash table is a prime number

    def find_next_prime(self, n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n

    # resize function
    def resize(self, new_size):
        oldArray = self.hashArray
        self.hashArray = np.full(new_size, None)
        self.count = 0

        for entry in oldArray:
            if entry is not None and entry.state == 1:
                self.put(entry.key, entry.value)

    # put function
    def put(self, key, value):
        if self.count / len(self.hashArray) >= self.loadFactorUpper:
            new_size = self.find_next_prime(2 * len(self.hashArray))
            self.resize(new_size)

        index = self.hash(key)
        start_index = index

        while self.hashArray[index] is not None and self.hashArray[index].state == 1:
            if self.hashArray[index].key == key:
                self.hashArray[index].value = value
                return
            index = (index + 1) % len(self.hashArray)
            if index == start_index:
                raise Exception("Hash table is full!")

        self.hashArray[index] = DSAHashEntry(key, value)
        self.count += 1

    # get function

    def get(self, key):
        index = self.hash(key)
        start_index = index
        while self.hashArray[index] is not None:
            if self.hashArray[index].key == key and self.hashArray[index].state == 1:
                return self.hashArray[index].value
            index = (index + 1) % len(self.hashArray)
            if index == start_index:
                break
        raise KeyError(f"Key '{key}' not found")

    # hasKey function
    def hasKey(self, key):
        index = self.hash(key)
        start_index = index
        while self.hashArray[index] is not None:
            if self.hashArray[index].key == key and self.hashArray[index].state == 1:
                return True
            index = (index + 1) % len(self.hashArray)
            if index == start_index:
                break
        return False

    # remove function
    def remove(self, key):
        index = self.hash(key)
        start_index = index
        while self.hashArray[index] is not None:
            if self.hashArray[index].key == key and self.hashArray[index].state == 1:
                self.hashArray[index].state = -1
                self.count -= 1
                if self.count / len(self.hashArray) <= self.loadFactorLower:
                    new_size = self.find_next_prime(len(self.hashArray) // 2)
                    self.resize(new_size)
                return
            index = (index + 1) % len(self.hashArray)
            if index == start_index:
                break
        print(f"Removal Unsuccessful! Key not found.")

    # find function
    def find(self, key):
        index = self.hash(key)
        while self.hashArray[index] is not None:
            if self.hashArray[index].key == key and self.hashArray[index].state == 1:
                return index
            index = (index + 1) % self.size
        raise KeyError(f"Key '{key}' not found in the hash table")

    # display function
    def display(self):
        print("\nHash Table:")
        for i, entry in enumerate(self.hashArray):
            if entry and entry.state == 1:
                print(f"{i}: Key = {entry.key}, Value = {entry.value}")
            else:
                print(f"{i}: Empty")

    # save hash table
    def save_hash_table(self, filename):
        with open(filename, 'w') as file:
            for entry in self.hashArray:
                if entry is not None and entry.state == 1:
                    file.write(f"{entry.key},{entry.value}\n")

    # insert values into hash table
    def insert_values_into_hashtable(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key = row[0]
                value = row[1] if len(row) > 1 else ""
                self.put(key, value)


def main():
    size = int(input("Enter the size of the hash table: "))
    hash_table = DSAHashTable(size)

    while True:
        print("\nMenu:")
        print("1. Insert key-value pair")
        print("2. Retrieve value by key")
        print("3. Check if key exists")
        print("4. Remove key")
        print("5. Display hash table")
        print("6. Load data from CSV")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = input("Enter value: ")
            hash_table.put(key, value)
            print(f"Key '{key}' with value '{value}' inserted.")
        elif choice == "2":
            key = input("Enter key: ")
            try:
                value = hash_table.get(key)
                print(f"Value for key '{key}': {value}")
            except KeyError as e:
                print(e)
        elif choice == "3":
            key = input("Enter key: ")
            if hash_table.hasKey(key):
                print(f"Key '{key}' exists in the hash table.")
            else:
                print(f"Key '{key}' does not exist in the hash table.")
        elif choice == "4":
            key = input("Enter key: ")
            try:
                hash_table.remove(key)
                print(f"Key '{key}' removed from the hash table.")
            except KeyError as e:
                print(e)
        elif choice == "5":
            hash_table.display()
        elif choice == "6":
            file_path = "RandomNames7000.csv"
            hash_table.insert_values_into_hashtable(file_path)
            print("Data loaded from CSV.")
            hash_table.save_hash_table("hash_table_output.csv")

        elif choice == "7":
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
