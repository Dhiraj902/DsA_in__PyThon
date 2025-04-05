# Queue implimentation using linkedList

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.item_count += 1
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.front is None:
            print("The queue is empty!")
            return None
        removed_item = self.front.item
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.item_count -= 1
        print(f"Dequeued: {removed_item}")
        return removed_item

    def get_front(self):
        if self.front is None:
            print("The queue is empty!")
            return None
        return self.front.item

    def get_rear(self):
        if self.rear is None:
            print("The queue is empty!")
            return None
        return self.rear.item

    def size(self):
        return self.item_count

if __name__ == "__main__":
    queue = Queue()
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Get Front")
        print("4. Get Rear")
        print("5. Get Size")
        print("6. Exit")
        choice = input("Select an operation: ")

        if choice == '1':
            data = input("Enter data to enqueue: ")
            queue.enqueue(data)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            front = queue.get_front()
            if front is not None:
                print(f"Front item: {front}")
        elif choice == '4':
            rear = queue.get_rear()
            if rear is not None:
                print(f"Rear item: {rear}")
        elif choice == '5':
            print(f"Queue size: {queue.size()}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid operation.")
