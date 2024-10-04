# Deletion and Reverse in Circular Linked List
class Solution:
    def reverse(self, head):
        if head is None or head.next == head:
            return head
        prev = None
        current = head
        next_node = None
        
        while True:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
            
            if current == head:
                break
            
        head.next = prev
        head = prev
        
        return head
        
    def deleteNode(self, head, key):
        if head is None:
            return None
            
        if head.data == key and head.next == head:
            return None
            
        current = head
        prev = None
        
        if head.data == key:
            while current.next != head:
                current = current.next
                
            current.next = head.next
            head = current.next
            return head
            
        current = head
        while current.next != head and current.next.data != key:
            current = current.next
            
        if current.next.data == key:
            current.next = current.next.next
            
        return head

  # Example usage:
sol = Solution()

# Create a circular linked list
head = create_circular_linked_list([1, 2, 3, 4, 5])
print("Original circular linked list:")
print_circular_linked_list(head)

# Reverse the circular linked list
head = sol.reverse(head)
print("\nCircular linked list after reversal:")
print_circular_linked_list(head)

# Delete a node with value 3
head = sol.deleteNode(head, 3)
print("\nCircular linked list after deleting node with value 3:")
print_circular_linked_list(head)
