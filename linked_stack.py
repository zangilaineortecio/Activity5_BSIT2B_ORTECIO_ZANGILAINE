class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # Linked structures do not have a fixed capacity (limited only by memory)
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty linked stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: No top element to peek.")
        return self.top.value

    def display(self):
        if self.is_empty():
            print("Linked Stack (top to bottom): [Empty]")
        else:
            print("Linked Stack (top to bottom):", end=" ")
            current = self.top
            elements = []
            while current is not None:
                elements.append(str(current.value))
                current = current.next
            print(" -> ".join(elements))