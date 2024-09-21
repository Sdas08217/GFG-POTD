# Clone a linked list with next and random pointer
class Solution:
    def copyList(self, head):
        
        if not head:
            return None
        d = {}
        curr = head
        
        while curr:
            d[curr] = Node(curr.data)
            curr = curr.next
        curr = head
        while curr:
            d[curr].next = d.get(curr.next)
            d[curr].random = d.get(curr.random)
            curr = curr.next
            
        return d[head]

  # Example usage
def print_list(head):
    curr = head
    while curr:
        random_data = curr.random.data if curr.random else None
        print(f"Node data: {curr.data}, Random points to: {random_data}")
        curr = curr.next

# Create an example linked list
head = Node(1)
second = Node(2)
third = Node(3)

head.next = second
second.next = third

head.random = third  # 1 -> random points to 3
second.random = head  # 2 -> random points to 1
third.random = second  # 3 -> random points to 2

solution = Solution()
copied_head = solution.copyList(head)

print("Original list:")
print_list(head)

print("\nCopied list:")
print_list(copied_head)
