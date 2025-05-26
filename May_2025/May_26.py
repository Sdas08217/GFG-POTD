class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node

        curr = head

        while True:
            # Case 2: Insert between curr and curr.next
            if curr.data <= data <= curr.next.data:
                break

            # Case 3: Insertion point at the boundary (max -> min)
            if curr.data > curr.next.data:
                if data >= curr.data or data <= curr.next.data:
                    break

            curr = curr.next

            # If we have traversed the whole list
            if curr == head:
                break

        # Insert the new_node between curr and curr.next
        new_node.next = curr.next
        curr.next = new_node

        # Return the correct head (if new node becomes new head)
        return head if head.data <= data else new_node
