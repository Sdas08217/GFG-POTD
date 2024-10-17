# Split Linked List Alternatingly
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def alternatingSplitList(self, head):
        # Create two dummy nodes to ease the splitting process
        list1_dummy = Node(0)  # Dummy node for the first list
        list2_dummy = Node(0)  # Dummy node for the second list
        
        # Pointers to build the two lists
        current1 = list1_dummy
        current2 = list2_dummy
        
        # Traverse the list alternately
        current = head
        index = 0
        while current:
            if index % 2 == 0:  # Even index goes to list1
                current1.next = current
                current1 = current1.next
            else:               # Odd index goes to list2
                current2.next = current
                current2 = current2.next
            # Move to the next node
            current = current.next
            index += 1
        
        # End the two lists
        current1.next = None
        current2.next = None
        
        # Return the heads of the two lists (without dummy nodes)
        return [list1_dummy.next, list2_dummy.next]
# Example usage
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    head = createLinkedList([1, 2, 3, 4, 5, 6])
    
    # Initialize the Solution class
    solution = Solution()
    
    # Perform the alternating split
    list1_head, list2_head = solution.alternatingSplitList(head)
    
    # Print the two lists
    print("List 1:")
    printList(list1_head)  # Output: 1 -> 3 -> 5 -> None
    
    print("List 2:")
    printList(list2_head)  # Output: 2 -> 4 -> 6 -> None
