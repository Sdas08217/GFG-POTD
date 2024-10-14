# Count Linked List Nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head: Node) -> int:
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
