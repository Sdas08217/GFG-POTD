# Delete node in Doubly Linked List
class Solution:
    def delete_node(self, head, x):
        if not head:
            return None

        # If the head is to be removed
        if x == 1:
            next_node = head.next
            if next_node:
                next_node.prev = None
            return next_node

        current = head
        for _ in range(x - 1):
            current = current.next
            if not current:
                return head

        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

        return head

  # Example usage
# LinkedList = 1 <--> 3 <--> 4, x = 3
head = Node(1)
second = Node(3)
third = Node(4)
head.next = second
second.prev = head
second.next = third
third.prev = second

print("Original list:")
print_list(head)

sol = Solution()
head = sol.delete_node(head, 3)

print("\nModified list:")
print_list(head)

# LinkedList = 1 <--> 5 <--> 2 <--> 9, x = 1
head = Node(1)
second = Node(5)
third = Node(2)
fourth = Node(9)
head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third

print("\nOriginal list:")
print_list(head)

head = sol.delete_node(head, 1)

print("\nModified list:")
print_list(head)
