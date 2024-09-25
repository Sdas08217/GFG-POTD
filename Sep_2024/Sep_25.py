# Palindrome Linked List
class Solution:
    def isPalindrome(self, head):
        ans = []
        while head :
            ans.append(head.data)
            head = head.next
        
        return ans == ans[::-1]

#Example Usage
# Example linked list: 1 -> 2 -> 2 -> 1 (palindrome)
arr = [1, 2, 2, 1]
head = create_linked_list(arr)

# Create an instance of the Solution class
sol = Solution()

# Check if the linked list is a palindrome
print(sol.isPalindrome(head))  # Output: True
