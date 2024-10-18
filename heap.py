import numpy as np


class HeapEntry:
    def __init__(self, priority, value):
        # Ensure the priority is treated as an integer
        self.priority = int(priority)
        self.value = value

    def __str__(self):
        return f"{self.priority}: {self.value}"


class HEAP:
    def __init__(self, max_size):
        self.MAX_SIZE = max_size
        self.heapArr = np.empty(self.MAX_SIZE, dtype=object)
        self.count = 0

    def add(self, priority, value):
        if self.count >= self.MAX_SIZE:
            raise ValueError("Heap is full")

        new_entry = HeapEntry(priority, value)
        self.heapArr[self.count] = new_entry  # Insert the new entry at the end
        self.tickle_up(self.count)  # Re-heapify the heap by tickling up
        self.count += 1

    def remove(self):
        if self.count == 0:
            return None
        # root's return value
        root_value = self.heapArr[0].value
        # Replace root with the last element
        self.heapArr[0] = self.heapArr[self.count - 1]
        # Remove the last element
        self.heapArr[self.count - 1] = None
        self.count -= 1
        # Reheapify
        self.tickle_down(0)
        return root_value

    def tickle_up(self, index):
        parent_index = self.get_parent_index(index)

        if index > 0 and self.heapArr[index].priority > self.heapArr[parent_index].priority:
            # Swap current node with its parent if it has a higher priority
            self.heapArr[index], self.heapArr[parent_index] = self.heapArr[parent_index], self.heapArr[index]
            self.tickle_up(parent_index)

    def tickle_down(self, index):
        left_child_index = self.get_left_child_index(index)
        right_child_index = self.get_right_child_index(index)
        largest_index = index

        if (left_child_index < self.count and
                self.heapArr[left_child_index].priority > self.heapArr[largest_index].priority):
            largest_index = left_child_index

        if (right_child_index < self.count and
                self.heapArr[right_child_index].priority > self.heapArr[largest_index].priority):
            largest_index = right_child_index

        if largest_index != index:
            # Swap the node with the larger child and continue to tickle down
            self.heapArr[index], self.heapArr[largest_index] = self.heapArr[largest_index], self.heapArr[index]
            self.tickle_down(largest_index)

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def heapify(self):
        # Rearrange the array into a valid max-heap
        for i in range(self.count // 2, -1, -1):
            self.tickle_down(i)

    def heap_sort(self):

        original_count = self.count
        sorted_array = np.empty(self.count, dtype=object)

        for i in range(original_count):
            sorted_array[i] = self.remove()

        return sorted_array

    def print_heap(self):
        if self.count == 0:
            print("Heap is empty")
            return

        print("Heap elements:")
        for i in range(self.count):
            print(self.heapArr[i])


def main_menu():
    # Get max size from user
    max_size = int(
        input("Enter the maximum size of the heap(10000 to accomodate CSV): "))
    heap = HEAP(max_size)

    while True:
        print("\nHeap Operations Menu:")
        print("1. Add element to heap")
        print("2. Remove element from heap")
        print("3. Display heap")
        print("4. Sort heap")
        print("5. Load data from CSV")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            priority = input("Enter priority: ")
            value = input("Enter value: ")
            try:
                heap.add(priority, value)
                print("Element added to the heap.")
            except ValueError as e:
                print(e)

        elif choice == '2':
            removed_element = heap.remove()
            if removed_element is None:
                print("Heap is empty. Cannot remove element.")
            else:
                print(f"Removed element with value: {removed_element}")

        elif choice == '3':
            heap.print_heap()

        elif choice == '4':
            sorted_array = heap.heap_sort()
            print("\nSorted elements from the heap:")
            for entry in sorted_array:
                if entry is not None:
                    print(entry)

        elif choice == '5':
            file_path = "RandomNames7000.csv"
            try:
                read_csv(file_path, heap)
                print("Data loaded from CSV into the heap.")
            except FileNotFoundError:
                print("File not found. Please check the file path.")

        elif choice == '6':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def read_csv(file_path, heap):
    with open(file_path, "r") as file:
        for line in file:
            priority, value = line.strip().split(",")
            heap.add(priority.strip(), value.strip())


if __name__ == "__main__":
    main_menu()


'''
Sample Test Data

(20, "Task A")
(15, "Task B")
(30, "Task C")
(10, "Task D")
(25, "Task E")
(5, "Task F")
(35, "Task G")
'''
