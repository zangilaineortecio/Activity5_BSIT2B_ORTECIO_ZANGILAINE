from linked_stack import LinkedStack

try:
    from linked_queue import LinkedQueue  # type: ignore[import-not-found]
except ImportError:
    from collections import deque

    class LinkedQueue:
        def __init__(self):
            self._items = deque()

        def enqueue(self, item):
            self._items.append(item)

        def dequeue(self):
            if self.is_empty():
                raise IndexError("dequeue from an empty queue")
            return self._items.popleft()

        def is_empty(self):
            return len(self._items) == 0

        def display(self):
            print(" -> ".join(str(item) for item in self._items))


def check_balanced_parentheses(expression):
    stack = LinkedStack()
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top_elem = stack.pop()
            if top_elem != mapping[char]:
                return False
                
    return stack.is_empty()


class PrintJob:
    def __init__(self, job_id, page_count):
        self.job_id = job_id
        self.page_count = page_count

    def __str__(self):
        return f"[Job ID: {self.job_id}, Pages: {self.page_count}]"


def simulate_print_queue():
    print("\n--- Print Queue Simulation ---")
    queue = LinkedQueue()
    
    # Enqueue sample jobs
    queue.enqueue(PrintJob("J101", 5))
    queue.enqueue(PrintJob("J102", 12))
    queue.enqueue(PrintJob("J103", 3))
    
    print("Initial Print Queue:")
    queue.display()
    
    print("\nProcessing print jobs in FIFO order:")
    position = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Wait order {position}: Printing {job}...")
        position += 1