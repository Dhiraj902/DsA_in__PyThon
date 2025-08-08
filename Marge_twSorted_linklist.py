"""
Given the head of two sorted linked lists consisting of nodes respectively. The task is to merge both lists and return the head of the sorted merged list
"""





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedMerge(self, head1, head2):
        # If one list is empty, return the other
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        # Compare data of the two lists and merge recursively
        if head1.data <= head2.data:
            head1.next = self.sortedMerge(head1.next, head2)
            return head1
        else:
            head2.next = self.sortedMerge(head1, head2.next)
            return head2

# Helper function to create linked list from Python list
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print linked list
def printLinkedList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage:
head1 = createLinkedList([1, 3, 5])
head2 = createLinkedList([2, 4, 6])

sol = Solution()
merged_head = sol.sortedMerge(head1, head2)

print("Merged Linked List:")
printLinkedList(merged_head)
