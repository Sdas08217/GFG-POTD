class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Helper function to count the number of nodes in loop
    def count_loop_length(self, meeting_point):
        count = 1
        current = meeting_point.next
        while current != meeting_point:
            count += 1
            current = current.next
        return count

    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.count_loop_length(slow)

        return 0

# Helper to create a linked list with a loop
def create_linked_list_with_loop(values, c):
    if not values:
        return None

    head = Node(values[0])
    current = head
    loop_entry = head if c == 0 else None

    for index in range(1, len(values)):
        new_node = Node(values[index])
        current.next = new_node
        current = new_node
        if index == c:
            loop_entry = current

    if c != 0:
        current.next = loop_entry

    return head
