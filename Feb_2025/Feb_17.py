import heapq
from typing import List

class Solution:
    def kLargest(self, arr: List[int], k: int) -> List[int]:
        return heapq.nlargest(k, arr)

# Example usage:
obj = Solution()
print(obj.kLargest([12, 5, 787, 1, 23], 2))  # Output: [787, 23]
print(obj.kLargest([1, 23, 12, 9, 30, 2, 50], 3))  # Output: [50, 30, 23]
print(obj.kLargest([12, 23], 1))  # Output: [23]
