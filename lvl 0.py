class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert a node at the head
    def insert_head(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, the new node becomes both head and tail
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # Point new node's next to the current head
            self.head.prev = new_node  # Point current head's prev to the new node
            self.head = new_node  # Move head to the new node

    # Insert a node at the tail
    def insert_tail(self, data):
        new_node = Node(data)
        if not self.tail:  # If the list is empty, the new node becomes both head and tail
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail  # Point new node's prev to the current tail
            self.tail.next = new_node  # Point current tail's next to the new node
            self.tail = new_node  # Move tail to the new node

    # Traverse the list from head to tail
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Traverse the list from tail to head
    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Usage Example
dll = DoublyLinkedList()
dll.insert_head(1)
dll.insert_tail(2)
dll.insert_tail(3)
dll.insert_head(0)
dll.traverse_forward()  # Expected Output: 0 <-> 1 <-> 2 <-> 3 <-> None
dll.traverse_backward()  # Expected Output: 3 <-> 2 <-> 1 <-> 0 <-> None
