# Largest Pair Sum
from typing import List
class Solution:
    def pairsum(self, arr : List[int]) -> int:
        arr.sort()
        return arr[-1] + arr[-2]

  # Example usage
sol = Solution()
arr = [3, 5, 1, 9, 2]
result = sol.pairsum(arr)
print(f"The sum of the two largest numbers is: {result}")
