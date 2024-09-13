# Middle of a Linked List
class Solution:
    def getMiddle(self, head):
        l1 = []
        while head:
            l1.append(head.data)
            head = head.next
        return l1[len(l1) // 2]

  # Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
values = [1, 2, 3, 4, 5]
head = createLinkedList(values)

# Find the middle element of the linked list
sol = Solution()
middle_element = sol.getMiddle(head)
print(f"The middle element is: {middle_element}")
