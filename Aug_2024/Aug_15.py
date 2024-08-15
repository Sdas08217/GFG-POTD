# Add 1 to a Linked List Number
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def addOne(self, head):
        number = 0
        
        # Step 1: Convert the linked list to an integer
        while head:
            number = number * 10 + head.data
            head = head.next
        
        # Step 2: Add one to the integer
        number += 1
        
        # Step 3: Convert the integer back to a linked list
        dummy = Node(0)
        current = dummy
        for digit in str(number):
            current.next = Node(int(digit))
            current = current.next
        
        # Step 4: Return the head of the new linked list
        return dummy.next

# Helper functions to create a linked list from a list and to print the linked list
def create_linked_list(lst):
    dummy = Node(0)
    current = dummy
    for num in lst:
        current.next = Node(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end="->" if current.next else "")
        current = current.next
    print()

# Example usage:
lst = [1, 3, 4, 5, 8, 5, 8, 3]
head = create_linked_list(lst)
solution = Solution()
new_head = solution.addOne(head)
print_linked_list(new_head)  # Output: 1->3->4->5->8->5->8->4
