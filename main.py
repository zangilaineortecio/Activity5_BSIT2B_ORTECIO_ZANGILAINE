from array_stack import ArrayStack
from linked_stack import LinkedStack

class ArrayQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Queue capacity must be greater than zero")
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value):
        if self.size == self.capacity:
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = value
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        value = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    def peek_front(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self.items[self.front]

    def display(self):
        values = []
        index = self.front
        for _ in range(self.size):
            values.append(str(self.items[index]))
            index = (index + 1) % self.capacity
        print("Queue: " + (" <- ".join(values) if values else "[empty]"))

class LinkedQueue:
        def __init__(self):
            self.front = None
            self.rear = None

        def enqueue(self, value):
            node = {"value": value, "next": None}
            if self.rear is None:
                self.front = node
                self.rear = node
            else:
                self.rear["next"] = node
                self.rear = node

        def dequeue(self):
            if self.front is None:
                raise Exception("Queue is empty")
            value = self.front["value"]
            self.front = self.front["next"]
            if self.front is None:
                self.rear = None
            return value

        def peek_front(self):
            if self.front is None:
                raise Exception("Queue is empty")
            return self.front["value"]

        def display(self):
            values = []
            current = self.front
            while current is not None:
                values.append(str(current["value"]))
                current = current["next"]
            print("Queue: " + (" <- ".join(values) if values else "[empty]"))


def check_balanced_parentheses(expression):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []

    for character in expression:
        if character in '([{':
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False

    return not stack


def simulate_print_queue():
    print_queue = LinkedQueue()

    while True:
        print("\n-- Print Queue Simulation --")
        print("1. Add print job | 2. Process job | 3. Display queue | 4. Back")
        choice = input("Choose: ")

        try:
            if choice == '1':
                print_queue.enqueue(input("Document name: "))
                print_queue.display()
            elif choice == '2':
                print(f"Printing: {print_queue.dequeue()}")
                print_queue.display()
            elif choice == '3':
                print_queue.display()
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
        except Exception as error:
            print(f"Error: {error}")

def main():
    while True:
        print("\n==============================")
        print(" MODULE 5: DATA STRUCTURES LAB")
        print("==============================")
        print("1. Test Array Stack")
        print("2. Test Linked Stack")
        print("3. Test Circular Array Queue")
        print("4. Test Linked Queue")
        print("5. Run Application: Balanced Parentheses Checker")
        print("6. Run Application: Print Queue Simulation")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            cap = int(input("Enter stack capacity: "))
            stack = ArrayStack(cap)
            while True:
                print("\n-- Array Stack Menu --")
                print("1. Push | 2. Pop | 3. Peek | 4. Display | 5. Back")
                sub = input("Choose: ")
                try:
                    if sub == '1':
                        val = input("Value to push: ")
                        stack.push(val)
                        stack.display()
                    elif sub == '2':
                        print(f"Popped: {stack.pop()}")
                        stack.display()
                    elif sub == '3':
                        print(f"Top element: {stack.peek()}")
                    elif sub == '4':
                        stack.display()
                    elif sub == '5':
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    
        elif choice == '2':
            stack = LinkedStack()
            while True:
                print("\n-- Linked Stack Menu --")
                print("1. Push | 2. Pop | 3. Peek | 4. Display | 5. Back")
                sub = input("Choose: ")
                try:
                    if sub == '1':
                        val = input("Value to push: ")
                        stack.push(val)
                        stack.display()
                    elif sub == '2':
                        print(f"Popped: {stack.pop()}")
                        stack.display()
                    elif sub == '3':
                        print(f"Top element: {stack.peek()}")
                    elif sub == '4':
                        stack.display()
                    elif sub == '5':
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    
        elif choice == '3':
            cap = int(input("Enter queue capacity: "))
            queue = ArrayQueue(cap)
            while True:
                print("\n-- Circular Array Queue Menu (Demonstrates Wrap-Around) --")
                print("1. Enqueue | 2. Dequeue | 3. Peek Front | 4. Display | 5. Back")
                sub = input("Choose: ")
                try:
                    if sub == '1':
                        val = input("Value to enqueue: ")
                        queue.enqueue(val)
                        queue.display()
                    elif sub == '2':
                        print(f"Dequeued: {queue.dequeue()}")
                        queue.display()
                    elif sub == '3':
                        print(f"Front element: {queue.peek_front()}")
                    elif sub == '4':
                        queue.display()
                    elif sub == '5':
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    
        elif choice == '4':
            queue = LinkedQueue()
            while True:
                print("\n-- Linked Queue Menu --")
                print("1. Push/Enqueue | 2. Dequeue | 3. Peek Front | 4. Display | 5. Back")
                sub = input("Choose: ")
                try:
                    if sub == '1':
                        val = input("Value to enqueue: ")
                        queue.enqueue(val)
                        queue.display()
                    elif sub == '2':
                        print(f"Dequeued: {queue.dequeue()}")
                        queue.display()
                    elif sub == '3':
                        print(f"Front element: {queue.peek_front()}")
                    elif sub == '4':
                        queue.display()
                    elif sub == '5':
                        break
                except Exception as e:
                    print(f"Error: {e}")
                    
        elif choice == '5':
            expr = input("Enter parentheses string to test (e.g. {[()]}): ")
            if check_balanced_parentheses(expr):
                print("Result: Parentheses are BALANCED.")
            else:
                print("Result: Parentheses are NOT balanced.")
                
        elif choice == '6':
            simulate_print_queue()
            
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 7.")

if __name__ == "__main__":
    main()