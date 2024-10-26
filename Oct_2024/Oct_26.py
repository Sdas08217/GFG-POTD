# Occurence of an integer in a Linked List
class Solution:
    def count(self, head, key):
        ans = 0
        temp = head
        while temp:
            if temp.data == key:
                ans += 1
            temp = temp.next
        return ans

  #Example Usage
  # Create nodes
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)

# Instantiate Solution and count occurrences of 1
solution = Solution()
key = 1
result = solution.count(head, key)

print(f"The count of {key} in the linked list is:", result)
