class Solution:
    def sortedMerge(self, head1, head2):
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode(0)
        current = dummy

        # Traverse both lists and choose the smaller value at each step
        while head1 and head2:
            if head1.data <= head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next

        # If there are remaining elements in either list, append them
        if head1:
            current.next = head1
        elif head2:
            current.next = head2

        # Return the merged list starting from the next node after dummy
        return dummy.next

# Helper class for defining the linked list node
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Helper function to print a linked list
def print_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    print(" -> ".join(result))

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
