# Doubly Linked List

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class Dll:
    def __init__(self, start=None):
        self.start = start

    def insert_at_first(self, data):
        new_node = Node(None, data)
        if self.start is None:
            self.start = new_node
        else:
            new_node.next = self.start
            self.start.prev = new_node
            self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(None, data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def traversal(self):
        if self.start is None:
            print("DLL is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print()

    def insert_at_mid(self, afterdata, data):
        if self.start is not None:
            temp = self.start
            while temp is not None:
                if temp.item == afterdata:
                    new_node = Node(temp, data, temp.next)
                    if temp.next is not None:
                        temp.next.prev = new_node
                    temp.next = new_node
                    break
                temp = temp.next

    def del_at_first(self):
        if self.start is not None and self.start.next is not None:
            temp = self.start
            self.start = self.start.next
            self.start.prev = None
            temp.next = None
        else:
            self.start = None

    def del_at_last(self):
        if self.start is not None and self.start.next is not None:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
        else:
            self.start = None

    def del_at_mid(self, data):
        if self.start is not None:
            if self.start.item == data:
                self.start = self.start.next
                if self.start is not None:
                    self.start.prev = None
            else:
                temp = self.start
                while temp is not None:
                    if temp.item == data:
                        temp.prev.next = temp.next
                        if temp.next is not None:
                            temp.next.prev = temp.prev
                        temp = None
                        break
                    temp = temp.next

if __name__ == "__main__":
    dll = Dll()
    while True:
        print(""" ____Operation Menu_____\n:
            1. Insert at first
            2. Insert at last
            3. Insert at middle
            4. Delete at first
            5. Delete at last
            6. Delete at middle
            7. Traverse
            8. Exit \n""")
       
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            dll.insert_at_first(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            dll.insert_at_last(data)
        elif choice == 3:
            afterdata = int(input("Enter node value after which to insert: "))
            data = int(input("Enter data: "))
            dll.insert_at_mid(afterdata, data)
        elif choice == 4:
            dll.del_at_first()
        elif choice == 5:
            dll.del_at_last()
        elif choice == 6:
            data = int(input("Enter data to delete: "))
            dll.del_at_mid(data)
        elif choice == 7:
            dll.traversal()
        elif choice == 8:
            break
        else:
            print("Invalid choice! Please try again.")
            break
