# Multiply two linked lists
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class Solution:
    def multiply_two_lists(self, first: ListNode, second: ListNode) -> int:
        MOD = 10**9 + 7
        
        # Function to extract the number from the linked list
        def linked_list_to_number(node):
            num = 0
            while node:
                num = (num * 10 + node.data) % MOD
                node = node.next
            return num
        
        # Get the two numbers from the linked lists
        num1 = linked_list_to_number(first)
        num2 = linked_list_to_number(second)
        
        # Return the multiplication result modulo 10^9 + 7
        return (num1 * num2) % MOD
# Example usage
first_list = [3, 4, 2]   # represents the number 342
second_list = [5, 6]     # represents the number 56

# Create linked lists from the arrays
first_linked_list = create_linked_list(first_list)
second_linked_list = create_linked_list(second_list)

# Create a solution object
sol = Solution()

# Multiply the two linked lists and print the result
result = sol.multiply_two_lists(first_linked_list, second_linked_list)
print(result)  # Expected output: (342 * 56) % (10**9 + 7) = 19152
