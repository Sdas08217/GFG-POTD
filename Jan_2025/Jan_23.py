class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
        self.random = None

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None

        # Step 1: Insert new nodes into the original list
        current = head
        while current:
            new_node = Node(current.data)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        # Step 2: Set up the random pointers for the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Step 3: Separate the original and copied list
        original = head
        copy = head.next
        new_head = copy
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
            original = original.next
            copy = copy.next

        return new_head
