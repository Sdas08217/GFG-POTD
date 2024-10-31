# Insert in Sorted way in a Sorted DLL
class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        # Step 1: Create the new node to be inserted
        new_node = Node(x)
        
        # Step 2: Handle the case where the list is empty
        if head is None:
            return new_node
        
        # Step 3: Insert at the beginning if x is smaller than the head's data
        if x < head.data:
            new_node.next = head
            head.prev = new_node
            return new_node
        
        # Step 4: Traverse the list to find the insertion point
        current = head
        while current.next and current.next.data < x:
            current = current.next
        
        # Step 5: Insert the new node after the current node
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        
        return head

  # Example usage
# Creating a sorted doubly linked list with values 1, 3, 4
head = Node(1)
node2 = Node(3)
node3 = Node(4)
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2

# Instantiate the Solution class
sol = Solution()

# Insert a new value into the sorted list
x = 2
head = sol.sortedInsert(head, x)

# Print the updated list
print_list(head)
