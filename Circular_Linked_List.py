#Circular Linked List (C_ll) Operations:

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class C_ll:
    def __init__(self, last=None):
        self.last = last

    def insert_at_first(self, data):
        new_node = Node(data)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    def traversal(self):
        if self.last is None:
            print("C_link list is not found !")
        else:
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)

    def insert_at_mid(self, afterdata, data):
        if self.last is not None:
            if self.last.item == afterdata:
                new_node = Node(data, self.last.next)
                self.last.next = new_node
                self.last = new_node
            else:
                temp = self.last.next
                while temp != self.last:
                    if temp.item == afterdata:
                        new_node = Node(data, temp.next)
                        temp.next = new_node
                        break
                    temp = temp.next  

    def del_at_first(self):
        if self.last is not None:
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                self.last.next = temp.next 
                temp = None

    def del_at_last(self):
        if self.last is not None:
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_at_midd(self, data):
        if self.last is not None:
            if self.last.next.item == data:
                if self.last == self.last.next:
                    self.last = None
                else:
                    self.last.next = self.last.next.next
            else:
                temp = self.last.next
                while temp != self.last:
                    if temp.next.item == data:
                        if temp.next == self.last:
                            self.last = temp
                        temp.next = temp.next.next
                        break
                    temp = temp.next

if __name__ == "__main__":
    cll = C_ll()
    while True:
        print("\nCircular Linked List Operations:")
        print("""
        1. Insert at First")
        2. Insert at Last
        3. Insert at Middle
        4. Delete First
        5. Delete Last
        6. Delete Middle
        7. Traverse
        8. Exit\n
        """)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data: "))
            cll.insert_at_first(data)
        elif choice == 2:
            data = int(input("Enter data: "))
            cll.insert_at_last(data)
        elif choice == 3:
            afterdata = int(input("Enter the value after which to insert: "))
            data = int(input("Enter data: "))
            cll.insert_at_mid(afterdata, data)
        elif choice == 4:
            cll.del_at_first()
        elif choice == 5:
            cll.del_at_last()
        elif choice == 6:
            data = int(input("Enter data to delete: "))
            cll.delete_at_midd(data)
        elif choice == 7:
            cll.traversal()
        elif choice == 8:
            break
        else:
            print("Invalid choice! Try again.")
            break
