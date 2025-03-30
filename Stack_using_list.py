 # Stack using List 



class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nChoose an operation:")
        print("""
        1. Push
        2. Pop
        3. Display Stack
        4. Peek at Top Element
        5. Exit \n""")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            data = int(input("Enter data to push: "))
            stack.push(data)
            print(f"{data} has been pushed onto the stack.")
        elif choice == '2':
            popped = stack.pop()
            if popped is not None:
                print(f"Popped item: {popped}")
        elif choice == '3':
            if stack.is_empty():
                print("Stack is empty!")
            else:
                print("Stack elements:", stack.items)
        elif choice == '4':
            top_item = stack.peek()
            if top_item is not None:
                print(f"Top item: {top_item}")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
