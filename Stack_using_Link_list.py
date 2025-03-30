 # Stack using List 

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self, top=None):
        self.top = top
        self.count = 0

    def push_stack(self, data):
        new_node = Node(data, self.top)
        self.top = new_node
        self.count += 1

    def pop_stack(self):
        if self.top is not None:
            temp = self.top.item
            self.top = self.top.next
            self.count -= 1
            print("Deleted item from stack:", temp)
        else:
            print("Stack is empty!")

    def print_stack_element(self):
        if self.top is not None:
            temp = self.top
            print("Total number of items:", self.count)
            print("Top item in stack:", temp.item)
            while temp is not None:
                print(temp.item)
                temp = temp.next
        else:
            print("Stack is empty!")

if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Display Stack")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            data = input("Enter data to push: ")
            stack.push_stack(data)
        elif choice == '2':
            stack.pop_stack()
        elif choice == '3':
            stack.print_stack_element()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
