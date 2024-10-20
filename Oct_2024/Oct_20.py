# Sort a k sorted doubly linked list
from heapq import heappush, heappop
class Solution:
    def sortAKSortedDLL(self, head, k):
        p = q = head
        h = []
        while q:
            heappush(h, q.data)
            if len(h) >= k + 1:
                p.data = heappop(h)
                p = p.next
            q = q.next
        while h:
            p.data = heappop(h)
            p = p.next
        return head

  # Example usage
if __name__ == "__main__":
    arr = [3, 6, 2, 12, 56, 8]
    k = 2
    head = create_dll(arr)
    print("Original list:")
    print_dll(head)

    sol = Solution()
    sorted_head = sol.sortAKSortedDLL(head, k)

    print("Sorted list:")
    print_dll(sorted_head)
