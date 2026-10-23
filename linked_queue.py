class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def is_full(self):
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty linked queue.")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: No front element to peek.")
        return self.front.value

    def display(self):
        if self.is_empty():
            print("Linked Queue (front to rear): [Empty]")
        else:
            print("Linked Queue (front to rear):", end=" ")
            current = self.front
            elements = []
            while current is not None:
                elements.append(str(current.value))
                current = current.next
            print(" -> ".join(elements))