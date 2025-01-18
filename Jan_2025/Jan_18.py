class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the link
            prev = current  # Move prev forward
            current = next_node  # Move current forward
        
        return prev  # New head of the reversed list
