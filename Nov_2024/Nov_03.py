# Is Linked List Length Even?
class Solution:
    def isLengthEven(self, head):
        # Initialize a counter
        count = 0
        # Traverse the list
        current = head
        while current:
            count += 1
            current = current.next
        # Check if the count is even or odd
        return count % 2 == 0

  # Example usage
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
