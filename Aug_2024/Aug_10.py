# Rotate a Linked List
class Solution:

    def rotate(self, head, k):

        temp  = head

        while temp and temp.next:
            temp=temp.next

        for i in range(k):
            t = head
            head=head.next
            t.next=None
            temp.next=t
            temp=temp.next

        return head

  # Example usage
lst = [1, 2, 3, 4, 5]
k = 2

head = create_linked_list(lst)
print("Original list:")
print_linked_list(head)

solution = Solution()
rotated_head = solution.rotate(head, k)

print(f"\nList after rotating by {k} positions:")
print_linked_list(rotated_head)
