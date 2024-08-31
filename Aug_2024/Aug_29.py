# Find length of Loop
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = fast = head
        
        # Detect the loop using Floyd's cycle detection algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If slow and fast meet, a loop is detected
            if slow == fast:
                return self.countLoopLength(slow)
        
        # No loop found
        return 0

    def countLoopLength(self, loop_node):
        current = loop_node
        count = 1
        
        # Count the number of nodes in the loop
        while current.next != loop_node:
            current = current.next
            count += 1
        
        return count

  # Example usage:
# Creating the linked list as per the example
# Example without a loop:
nodes = [ListNode(i) for i in [41, 32, 19, 3]]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]

# Test with no loop (c = 0)
solution = Solution()
print(solution.countNodesInLoop(nodes[0]))  # Output should be 0
