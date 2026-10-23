class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: Cannot push to a full stack.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None  # Clear reference
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: No top element to peek.")
        return self.data[self.top]

    def display(self):
        if self.is_empty():
            print("Stack (top to bottom): [Empty]")
        else:
            print("Stack (top to bottom):", end=" ")
            elements = [str(self.data[i]) for i in range(self.top, -1, -1)]
            print(" -> ".join(elements))