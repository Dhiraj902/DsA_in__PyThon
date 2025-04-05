# Queue Data Structure Implementation in Python

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, data):
        self.items.append(data)
        return self.items[-1]

    def dequeue(self):
        if len(self.items) != 0:
            return self.items.pop(0)
        else:
            raise IndexError("Queue is underflow")

    def get_rear(self):
        if len(self.items) != 0:
            return self.items[-1]
        else:
            raise IndexError("Queue is underflow")

    def get_front(self):
        if len(self.items) != 0:
            return self.items[0]
        else:
            raise IndexError("Queue is underflow")

    def size(self):
        return len(self.items)

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
            print(f"Enqueued: {data}")
        elif choice == '2':
            try:
                data = queue.dequeue()
                print(f"Dequeued: {data}")
            except IndexError as e:
                print(e)
        elif choice == '3':
            try:
                print(f"Front item: {queue.get_front()}")
            except IndexError as e:
                print(e)
        elif choice == '4':
            try:
                print(f"Rear item: {queue.get_rear()}")
            except IndexError as e:
                print(e)
        elif choice == '5':
            print(f"Queue size: {queue.size()}")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid operation.")
            break
