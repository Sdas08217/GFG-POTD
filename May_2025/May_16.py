import heapq

class Solution:
    def findSmallestRange(self, arr):
        k = len(arr)
        n = len(arr[0])

        # Min-Heap to store (value, list_index, element_index)
        min_heap = []
        max_value = float('-inf')

        # Initialize the heap with the first element from each list
        for i in range(k):
            heapq.heappush(min_heap, (arr[i][0], i, 0))
            max_value = max(max_value, arr[i][0])

        min_range = float('inf')
        result = [0, 0]

        while True:
            min_value, list_index, element_index = heapq.heappop(min_heap)

            # Update the smallest range if found
            if max_value - min_value < min_range:
                min_range = max_value - min_value
                result = [min_value, max_value]

            # Move to the next element in the current list
            if element_index + 1 < n:
                next_value = arr[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                max_value = max(max_value, next_value)
            else:
                break  # One of the lists is exhausted

        return result
