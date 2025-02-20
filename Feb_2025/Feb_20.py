import heapq

class Solution:
    def getMedian(self, arr):
        max_heap = []  # Left half (max heap as negative values)
        min_heap = []  # Right half (min heap)
        medians = []

        for num in arr:
            # Step 1: Insert the new number
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)

            # Step 2: Balance the heaps
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # Step 3: Compute the median
            if len(max_heap) > len(min_heap):
                medians.append(float(-max_heap[0]))
            else:
                medians.append((-max_heap[0] + min_heap[0]) / 2.0)

        return medians
