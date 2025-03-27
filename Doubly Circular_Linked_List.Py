#Doubly Circular Linked List in Python

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class D_CLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_first(self, data):
        if self.start is not None:
            new_node = Node(self.start.prev, data, self.start)
            self.start.prev.next = new_node
            self.start.prev = new_node
            self.start = new_node
        else:
            new_node = Node(None, data)
            new_node.prev = new_node
            new_node.next = new_node
            self.start = new_node

    def insert_at_last(self, data):
        if self.start is not None:
            new_node = Node(self.start.prev, data, self.start)
            self.start.prev.next = new_node
            self.start.prev = new_node
        else:
            new_node = Node(None, data)
            new_node.prev = new_node
            new_node.next = new_node
            self.start = new_node

    def insert_at_mid(self, afterdata, data):
        if self.start is not None:
            temp = self.start
            while temp.next is not self.start:
                if temp.item == afterdata:
                    new_node = Node(temp, data, temp.next)
                    temp.next.prev = new_node
                    temp.next = new_node
                    return
                temp = temp.next
            if temp.item == afterdata:
                new_node = Node(temp, data, temp.next)
                temp.next.prev = new_node
                temp.next = new_node

    def del_at_first(self):
        if self.start is not None:
            if self.start != self.start.next:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
            else:
                self.start = None

    def del_at_last(self):
        if self.start is not None:
            if self.start.next is not self.start:
                temp = self.start.prev
                self.start.prev = temp.prev
                temp.prev.next = self.start
            else:
                self.start = None
        else:
            print("List is empty!")

    def del_at_mid(self, data):
        if self.start is not None:
            temp = self.start
            while temp is not self.start.prev:
                if temp.item == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    if temp == self.start:
                        self.start = self.start.next
                    return
                temp = temp.next
            if temp.item == data:
                if temp == self.start:
                    self.start = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

    def traversal(self):
        if self.start is not None:
            temp = self.start
            while temp.next is not self.start:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)
        else:
            print("Doubly Circular Linked List is empty!")

if __name__ == "__main__":
    dcll = D_CLL()
    while True:
        print("\nDoubly Circular Linked List Operations:")
        print("""
        1. Insert at First
        2. Insert at Last
        3. Insert at Middle
        4. Delete First
        5. Delete Last
        6. Delete Middle
        7. Traverse
        8. Exit
        """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            dcll.insert_at_first(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            dcll.insert_at_last(data)
        elif choice == 3:
            afterdata = int(input("Enter the value after which to insert: "))
            data = int(input("Enter data: "))
            dcll.insert_at_mid(afterdata, data)
        elif choice == 4:
            dcll.del_at_first()
        elif choice == 5:
            dcll.del_at_last()
        elif choice == 6:
            data = int(input("Enter data to delete: "))
            dcll.del_at_mid(data)
        elif choice == 7:
            dcll.traversal()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
