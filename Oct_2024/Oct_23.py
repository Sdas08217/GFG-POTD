# Find the Sum of Last N nodes of the Linked List
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        # Initialize two pointers
        fast = slow = head
        # Move 'fast' n steps ahead
        for _ in range(n):
            fast = fast.next
        # Move both 'fast' and 'slow' until 'fast' reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        # Calculate the sum of the last n nodes
        total_sum = 0
        while slow:
            total_sum += slow.data
            slow = slow.next
        return total_sum

  # Define the linked list nodes
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Create an instance of the Solution class
solution = Solution()

# Set the value of n (e.g., sum of last 3 nodes)
n = 3

# Call the method and print the result
result = solution.sumOfLastN_Nodes(head, n)
print(f"The sum of the last {n} nodes is: {result}")
