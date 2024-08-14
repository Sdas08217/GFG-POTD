# Square root of a number
from math import floor

class Solution:
    def floorSqrt(self, n):
        return floor(pow(n, 0.5))

  # Example usage
solution = Solution()
result = solution.floorSqrt(16)
print(result)  # Output will be 4

result = solution.floorSqrt(20)
print(result)  # Output will be 4

result = solution.floorSqrt(25)
print(result)  # Output will be 5
