class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue overflow: Cannot enqueue to a full queue.")
        rear = (self.front + self.size) % self.capacity
        self.data[rear] = value
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: Cannot dequeue from an empty queue.")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty: No front element to peek.")
        return self.data[self.front]

    def display(self):
        if self.is_empty():
            print("Circular Queue (front to rear): [Empty]")
        else:
            print("Circular Queue (front to rear):", end=" ")
            elements = []
            for i in range(self.size):
                idx = (self.front + i) % self.capacity
                elements.append(str(self.data[idx]))
            print(" -> ".join(elements))