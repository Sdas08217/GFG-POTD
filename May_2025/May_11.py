import heapq
from typing import List

class Solution:
    def kthLargest(self, arr: List[int], k: int) -> int:
        """
        Return the k-th largest sum among all contiguous subarrays of arr.
        Uses a min-heap of size k to track the k largest sums in O(n^2 log k).
        """
        n = len(arr)
        min_heap = []  # will contain at most k largest sums, min-heap

        # Enumerate all subarrays by start i and end j
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += arr[j]
                if len(min_heap) < k:
                    # still room, just push
                    heapq.heappush(min_heap, curr)
                else:
                    # if this sum is larger than the smallest in the heap, replace it
                    if curr > min_heap[0]:
                        heapq.heapreplace(min_heap, curr)

        # the root of the min-heap is the k-th largest sum
        return min_heap[0]
