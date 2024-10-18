# from graph_vertex import DSAVertex
# from stack import Stack
# from queue_implementation import Queue
# from singly_linked_list import SinglyLinkedList
import numpy as np


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_prev(self):
        return self.prev

    def set_prev(self, new_value):
        self.prev = new_value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class DSAVertex:
    def __init__(self, label, value):
        self.label = label
        self.value = value
        self.adjacent = SinglyLinkedList()
        self.visited = False

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value

    def getAdjacent(self):
        # print all the adjacent vertices
        return self.adjacent

    def getAdjacentEdge(self):
        # return edges
        return self.adjacent.traverse()

    def addEdge(self, label):
        # add edge between two vertices
        self.adjacent.insert_last(label)

    def removeEdge(self, label):
        self.adjacent.remove_by_value(label)

    def setVisited(self):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def getVisited(self):
        return self.visited

    def __str__(self):
        return f"Label: {self.label}, Value: {self.value}, Visited: {self.visited}"


class Stack:
    def __init__(self, size):
        self.size = size  # this is the size of the stack
        self.array = np.empty(self.size, dtype=object)
        self.count = 0

    def push(self, value):
        # can push only if array has space
        if not self.isfull():
            self.array[self.count] = value
            self.count += 1

        else:
            print("The array is full")

    def pop(self):
        # can only pop if not empty
        if not self.isempty():
            # remove from the array
            value_to_remove = self.array[self.count]
            self.array[self.count-1] = None
            self.count -= 1
            return value_to_remove
        else:
            print("Array is empty")

    def peek(self):
        # can only peek if array is not empty
        if not self.isempty():
            return self.array[self.count - 1]

    def isempty(self):
        # return True or false depending on whether array has been filled or not
        return self.count == 0

    def isfull(self):
        # has space if size of teh stack is greater than the length of the element
        return self.size == self.count

    def printArray(self):
        print("Here is your stack: ", self.array)


class Queue:
    def __init__(self, size):
        self.size = size
        self.array = np.empty(self.size, dtype=object)
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if self.isfull():
            print("queue is full")
        else:

            if self.isempty():
                self.front = 0
                self.rear = 0
            else:
                self.rear += 1
            self.array[self.rear] = value
        # print("Your array after enqueue", self.array)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        # only one element, remove it from the front
        elif self.front == self.rear:
            remove_value = self.array[self.front]
            self.array[self.front] = None
            self.front = self.rear = -1
            # print("Value removed from the queue is", remove_value)
            return remove_value

        else:
            remove_value = self.array[self.front]
            self.array[self.front] = None
            self.front += 1
            # print("Value removed from the queue is", remove_value)
            return remove_value

        # print("Your array after deque is: ", self.array)

    def peek(self):
        if self.isempty():
            print("empty queue")
        else:
            peek = self.array[self.front]
            print("You peeked at ", peek)

    def isfull(self):
        return self.rear == self.size-1

    def isempty(self):
        return self.rear == -1


class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def insert_first(self, value):
        # insert at the beginning of the list

        # creating a new node
        new_node = Node(value)

        # is empty
        if self.is_empty():
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def insert_last(self, value):
        # insert after tail

        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def insert_at_middle(self, value):
        node_to_insert = Node(value)

        if self.is_empty():
            node_to_insert.set_next(self.head)
            self.head = node_to_insert
        else:
            length = 0
            current = self.head
            while current is not None:
                current = current.get_next()
                length += 1

            count = (length / 2) if (length % 2 == 0) else (length+1)/2

            current = self.head
            while count > 1:
                current = current.get_next()
                count -= 1
            node_to_insert.set_next(current.get_next())
            current.set_next(node_to_insert)

    def remove_first(self):
        if self.is_empty():
            return "Empty linked list, cannot remove"

        # if only one element
        elif not self.head.get_next():
            current_head = self.head
            self.head = None
            return current_head.get_value()
        else:
            current_head = self.head
            self.head = current_head.get_next()
            return current_head.get_value()

    def remove_last(self):
        if self.is_empty():
            return "Empty linked list, cannot remove"
            # just one element
        elif self.head.get_next() is None:
            current_head = self.head
            self.head = None
            return current_head.get_value()

        # implementing using fast and slow pointer
        current = self.head
        while current.get_next().get_next():
            current = current.get_next()
        current.set_next(None)
        return current.get_value()

    def remove_at_middle(self):
        if self.is_empty():
            return "Empty linked list, cannot remove"

        else:
            count = 0
            current = self.head
            while current is not None:
                current = current.get_next()
                count += 1
            middle = (count/2) if (count % 2 == 0) else (count+1)/2

            current = self.head
            while middle > 1:
                current = current.get_next()
                middle -= 1
            current.set_next(current.get_next().get_next())

    def remove_by_value(self, value):
        if self.head is None:
            return "Empty list"

        if self.head.value == value:
            return self.remove_first()

        prev = self.head
        current = prev.get_next()

        while current is not None:
            if current.get_value() == value:
                prev.set_next(current.get_next())
                return value
            prev = current
            current = current.get_next()
        return None

    def remove_at_index(self, index):
        if self.is_empty():
            return "Empty list"

        if index == 0:
            return self.remove_first()

        current = self.head
        count = 0
        while current is not None and count < index - 1:
            current = current.get_next()
            count += 1

        if current is None or current.get_next() is None:
            return "Index out of bounds"

        value = current.get_next().get_value()
        current.set_next(current.get_next().get_next())
        return value

    def peek_first(self):
        if self.is_empty():
            return "Empty linked list"
        else:
            return self.head.get_value()

    def peek_last(self):
        if self.is_empty():
            return "Empty linked list"
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            return current.get_value()

    def traverse(self):
        node = []
        current = self.head
        while current is not None:
            # print(current.get_value())
            node.append(current.get_value())
            current = current.get_next()
        return node

    def is_empty(self):
        return self.head == None


class DSAGraph:
    def __init__(self, directed=False):
        self.directed = directed
        self.vertices = SinglyLinkedList()  # Use a singly linked list to store vertices
        # Array to store vertex labels
        self.vertex_labels = np.array([], dtype=object)

    def addVertex(self, label, value=None):
        if not self.hasVertex(label):  # Check if vertex already exists
            new_vertex = DSAVertex(label, value)
            self.vertices.insert_last(new_vertex)
            self.vertex_labels = np.append(self.vertex_labels, label)

    def removeVertex(self, label):
        vertex = self.getVertex(label)
        if vertex:
            self.vertices.remove_by_value(vertex)
            self.vertex_labels = np.delete(
                self.vertex_labels, np.where(self.vertex_labels == label))

            # Remove edges for directed graphs
            for v_label in self.vertex_labels:
                self.removeEdges(v_label, label)

            # Remove edges for undirected graphs
            if not self.directed:
                self.removeEdges(label, v_label)
        else:
            print("Vertex not found")

    def addEdges(self, label1, label2):
        if self.hasVertex(label1) and self.hasVertex(label2):
            vertex1 = self.getVertex(label1)
            vertex2 = self.getVertex(label2)
            vertex1.addEdge(label2)
            # If undirected, add in both directions
            if not self.directed:
                vertex2.addEdge(label1)

    def removeEdges(self, label1, label2):
        if self.hasVertex(label1) and self.hasVertex(label2):
            vertex1 = self.getVertex(label1)
            vertex2 = self.getVertex(label2)
            vertex1.removeEdge(label2)  # Remove edge from vertex1 to vertex2

            # For undirected graphs, remove the edge in both directions
            if not self.directed and label1 in vertex2.getAdjacent():
                # Remove edge from vertex2 to vertex1
                vertex2.removeEdge(label1)

    def getVertex(self, label):
        current = self.vertices.head
        while current:
            if current.get_value().getLabel() == label:
                return current.get_value()
            current = current.get_next()
        return None

    def hasVertex(self, label):
        current = self.vertices.head
        while current:
            if current.get_value().getLabel() == label:
                return True
            current = current.get_next()
        return False

    def isAdjacent(self, label1, label2):
        vertex1 = self.getVertex(label1)
        if vertex1:
            adjacent_vertices = vertex1.getAdjacent().traverse()
            return label2 in adjacent_vertices
        return False

    def getNeighbors(self, label):
        """Retrieve all neighboring locations (adjacent vertices) for a given location."""
        vertex = self.getVertex(label)
        if vertex:
            neighbors = vertex.getAdjacent().traverse()
            return neighbors
        else:
            print(f"Location '{label}' not found in the graph.")
            return []

    def displayGraph(self):
        """Display the graph structure showing all locations and their connections."""
        print("\nGraph Structure:")
        current_vertex = self.vertices.head
        while current_vertex:
            vertex = current_vertex.get_value()
            neighbors = vertex.getAdjacent().traverse()
            print(f"Location: {vertex.getLabel()
                               } -> Connected to: {neighbors}")
            current_vertex = current_vertex.get_next()

    def displayAsList(self):
        adj_size = len(self.vertex_labels)
        adj_matrix = [["-"] * adj_size for _ in range(adj_size)]
        for i in range(adj_size):
            for j in range(adj_size):
                label1 = self.vertex_labels[i]
                label2 = self.vertex_labels[j]
                if self.isAdjacent(label1, label2):
                    adj_matrix[i][j] = label2
        for row in adj_matrix:
            print(row)

    def displayAsMatrix(self):
        matrix_size = len(self.vertex_labels)
        matrix = [[0] * matrix_size for _ in range(matrix_size)]
        for i in range(matrix_size):
            for j in range(matrix_size):
                label1 = self.vertex_labels[i]
                label2 = self.vertex_labels[j]
                if self.isAdjacent(label1, label2):
                    matrix[i][j] = 1
        for row in matrix:
            print(row)


# class DSAGraph:
#     def __init__(self, directed=False):
#         self.directed = directed
#         self.vertices = SinglyLinkedList()  # Changed to SinglyLinkedList
#         self.vertex_labels = np.array(
#             [], dtype=object)  # Changed to numpy array

#     def addVertex(self, label, value=None):
#         if not self.hasVertex(label):  # Check if vertex already exists
#             new_vertex = DSAVertex(label, value)
#             self.vertices.insert_last(new_vertex)
#             self.vertex_labels = np.append(self.vertex_labels, label)

#     def removeVertex(self, label):
#         vertex = self.getVertex(label)
#         if vertex:
#             self.vertices.remove_by_value(vertex)
#             self.vertex_labels = np.delete(
#                 self.vertex_labels, np.where(self.vertex_labels == label))

#             # Remove edges for directed graphs
#             for v_label in self.vertex_labels:
#                 self.removeEdges(v_label, label)

#             # Remove edges for undirected graphs
#             if not self.directed:
#                 self.removeEdges(label, v_label)
#         else:
#             print("Vertex not found")

#     def addEdges(self, label1, label2):
#         if self.hasVertex(label1) and self.hasVertex(label2):
#             vertex1 = self.getVertex(label1)
#             vertex2 = self.getVertex(label2)
#             vertex1.addEdge(label2)
#             # If undirected, add in both directions
#             if not self.directed:
#                 vertex2.addEdge(label1)

#     def removeEdges(self, label1, label2):
#         if self.hasVertex(label1) and self.hasVertex(label2):
#             vertex1 = self.getVertex(label1)
#             vertex2 = self.getVertex(label2)
#             vertex1.removeEdge(label2)  # Remove edge from vertex1 to vertex2

#             # For undirected graphs, remove the edge in both directions
#             if not self.directed and label1 in vertex2.getAdjacent():
#                 # Remove edge from vertex2 to vertex1
#                 vertex2.removeEdge(label1)

#     def getVertexCount(self):
#         return self.vertices.size()

#     def getEdgeCount(self):
#         total_edges = 0
#         current_vertex = self.vertices.head
#         while current_vertex is not None:
#             total_edges += len(current_vertex.get_value().getAdjacent().traverse())
#             current_vertex = current_vertex.get_next()
#         if self.directed:
#             return total_edges
#         return total_edges // 2  # For undirected graph, divide by 2

#     def getVertex(self, label):
#         current = self.vertices.head
#         while current:
#             if current.get_value().getLabel() == label:
#                 return current.get_value()
#             current = current.get_next()
#         return None

#     def hasVertex(self, label):
#         current = self.vertices.head
#         while current:
#             if current.get_value().getLabel() == label:
#                 return True
#             current = current.get_next()
#         return False

#     def isAdjacent(self, label1, label2):
#         vertex1 = self.getVertex(label1)
#         vertex2 = self.getVertex(label2)
#         if vertex1 and vertex2:
#             adjacent_vertices = vertex1.getAdjacent()
#             current = adjacent_vertices.head
#             while current is not None:
#                 if current.get_value() == label2:
#                     return True
#                 current = current.get_next()
#         return False

#     # Sorting function
#     def sort(self, vertex):
#         # Step 1: Filter adjacent vertices and store them in a NumPy array
#         adjacents = np.array([adj for adj in vertex.getAdjacent(
#         ).traverse() if adj in self.vertex_labels], dtype=object)

#         # Step 2: Implement selection sort to manually sort the NumPy array
#         for i in range(len(adjacents)):
#             # Find the minimum element in the remaining unsorted part
#             min_index = i
#             for j in range(i + 1, len(adjacents)):
#                 if adjacents[j] < adjacents[min_index]:
#                     min_index = j
#             # Swap the found minimum element with the first element
#             adjacents[i], adjacents[min_index] = adjacents[min_index], adjacents[i]

#         return adjacents

#     def getAdjacent(self, label):
#         vertex = self.getVertex(label)
#         if vertex:
#             if self.directed:
#                 # return sorted([adj for adj in vertex.getAdjacent().traverse() if adj in self.vertex_labels])
#                 return self.sort(vertex)
#             else:
#                 # return sorted([adj for adj in vertex.getAdjacent().traverse() if adj in self.vertex_labels])
#                 return self.sort(vertex)
#         return None

#     def displayAsList(self):
#         adj_size = len(self.vertex_labels)
#         adj_matrix = [["-"] * adj_size for _ in range(adj_size)]
#         for i in range(adj_size):
#             for j in range(adj_size):
#                 label1 = self.vertex_labels[i]
#                 label2 = self.vertex_labels[j]
#                 if self.isAdjacent(label1, label2):
#                     adj_matrix[i][j] = label2
#         for row in adj_matrix:
#             print(row)

#     def displayAsMatrix(self):
#         matrix_size = len(self.vertex_labels)
#         matrix = [[0] * matrix_size for _ in range(matrix_size)]
#         for i in range(matrix_size):
#             for j in range(matrix_size):
#                 label1 = self.vertex_labels[i]
#                 label2 = self.vertex_labels[j]
#                 if self.isAdjacent(label1, label2):
#                     matrix[i][j] = 1
#         for row in matrix:
#             print(row)

#     def breathFirstSearch(self):
#         T = SinglyLinkedList()
#         Q = Queue(100)

#         # Reset visited flags for all vertices
#         current = self.vertices.head
#         while current:
#             if current.get_value() is not None:
#                 current.get_value().clearVisited()
#                 current = current.get_next()
#             else:
#                 break

#         # Perform BFS from each unvisited vertex
#         current = self.vertices.head
#         while current:
#             v = current.get_value()
#             if not v.getVisited():
#                 v.setVisited()
#                 Q.enqueue(v)
#                 while not Q.isempty():
#                     v = Q.dequeue()
#                     for adj in self.getAdjacent(v.getLabel()):
#                         w = self.getVertex(adj)
#                         if w and not w.getVisited():
#                             T.insert_last(v)  # Enqueue v to T
#                             T.insert_last(w)  # Enqueue w to T
#                             w.setVisited()
#                             Q.enqueue(w)

#                     current = current.get_next()

#         # Construct the path
#         T_path = [vertex.getLabel() for vertex in T.traverse()]
#         print("T: ", T_path)
#         path = []
#         current = T.head
#         while current:
#             vertex = current.get_value()
#             if vertex.getLabel() not in path:
#                 path.append(vertex.getLabel())
#             current = current.get_next()

#         print(path)

#     def depthFirstSearch(self):
#         T = SinglyLinkedList()
#         S = Stack(100)

#         # Reset visited flags for all vertices
#         current = self.vertices.head
#         while current:
#             if current.get_value() is not None:
#                 current.get_value().clearVisited()
#                 current = current.get_next()
#             else:
#                 break

#         # Perform DFS from each unvisited vertex
#         current = self.vertices.head
#         while current.get_next() is not None:
#             v = current.get_value()
#             if not v.getVisited():
#                 v.setVisited()
#                 S.push(v)

#                 while not S.isempty():
#                     v = S.peek()  # Get the top element
#                     w = self.getUnvisitedAdjacent(v)
#                     if w:
#                         T.insert_last(v)
#                         T.insert_last(w)
#                         w.setVisited()
#                         S.push(w)
#                         v = w

#                     else:
#                         S.pop()  # Backtrack if no unvisited adjacent vertex found

#             # Advance to the next vertex
#             current = current.get_next()

#         # Construct the path from the traversal
#         T_path = [vertex.getLabel() for vertex in T.traverse()]
#         print("T: ", T_path)
#         path = []
#         current = T.head
#         while current:
#             vertex = current.get_value()
#             if vertex.getLabel() not in path:
#                 path.append(vertex.getLabel())
#             current = current.get_next()

#         print("Path", path)

#     def getUnvisitedAdjacent(self, vertex):
#         adjacent_vertices = self.getAdjacent(vertex.getLabel())
#         for adj in adjacent_vertices:
#             if not self.getVertex(adj).getVisited():
#                 return self.getVertex(adj)
#         return None
