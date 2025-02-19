from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # Custom comparison for heapq
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, arr):
        min_heap = []
        
        # Push the head of each linked list into the heap
        for l in arr:
            if l:
                heappush(min_heap, l)
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            node = heappop(min_heap)  # Get the smallest node
            current.next = node
            current = current.next
            
            if node.next:
                heappush(min_heap, node.next)  # Insert the next node into the heap
        
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

# Example usage
lists = [
    create_linked_list([1, 2, 3]),
    create_linked_list([4, 5]),
    create_linked_list([5, 6]),
    create_linked_list([7, 8])
]

solution = Solution()
merged_head = solution.mergeKLists(lists)
print_linked_list(merged_head)
