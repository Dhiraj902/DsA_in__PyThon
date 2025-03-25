#Singly linked list 
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Sll:
    def __init__(self, start=None):
        self.start = start

    def insert_at_first(self, data):
        new_node = Node(data, self.start)
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def insert_at_mid(self, afterdata, data):
        if self.start is not None:
            temp = self.start
            while temp is not None:
                if temp.item == afterdata:
                    n = Node(data, temp.next)
                    temp.next = n
                    break
                temp = temp.next
        else:
            print("The Node is Empty")

    def del_at_first(self):
        if self.start is None:
            print("SLL is empty")
        else:
            temp = self.start
            self.start = self.start.next
            temp.next = None

    def del_at_last(self):
        if self.start is not None:
            temp = self.start
            if temp.next is None:
                self.start = None
            else:
                while temp.next is not None:
                    if temp.next.next is None:
                        temp.next = None
                        break
                    temp = temp.next

    def del_at_mid(self, data):
        if self.start and self.start.item == data:
            temp = self.start
            self.start = self.start.next
            temp.next = None
        elif self.start is not None:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next = temp.next.next
                    break
                temp = temp.next
        else:
            self.start = None

    def traversal(self):
        if self.start is None:
            print("SLL is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.item, end=" ")
                temp = temp.next
            print()

if __name__ == "__main__":
    sll = Sll()
    while True:
        print( """Operation Menu\n:
        1. Insert at first
        2. Insert at last
        3. Insert at middle
        4. Delete at first
        5. Delete at last
        6. Delete at middle
        7. Traverse
        8. Exit\n""" )
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            sll.insert_at_first(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            sll.insert_at_last(data)
        elif choice == 3:
            afterdata = int(input("Enter node value after which to insert: "))
            data = int(input("Enter data: "))
            sll.insert_at_mid(afterdata, data)
        elif choice == 4:
            sll.del_at_first()
        elif choice == 5:
            sll.del_at_last()
        elif choice == 6:
            data = int(input("Enter data to delete: "))
            sll.del_at_mid(data)
        elif choice == 7:
            sll.traversal()
        elif choice == 8:
            break
        else:
            print("Invalid choice! Please try again.")
            break
