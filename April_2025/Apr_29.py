class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        # Step 1: Count 0s, 1s, and 2s
        count = [0, 0, 0]
        current = head
        while current:
            count[current.data] += 1
            current = current.next

        # Step 2: Overwrite the data values in the list
        current = head
        i = 0
        while current:
            if count[i] == 0:
                i += 1
            else:
                current.data = i
                count[i] -= 1
                current = current.next
        
        return head  # Always return head in linked list problems

# Helper functions to test
def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" → " if head.next else "\n")
        head = head.next
