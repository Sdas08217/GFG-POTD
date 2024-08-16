# Maximize The Cut Segments
import sys
sys.setrecursionlimit(10 ** 6)
class Solution:
    def maximizeTheCuts(self, n, x, y, z):
        def fun(num):
            if num == 0:
                return 0
            if dp[num] != -1:
                return dp[num]
            take_x = take_y = take_z = float('-inf')
            if num >= x:
                take_x = fun(num - x) + 1
            if num >= y:
                take_y = fun(num - y) + 1
            if num >= z:
                take_z = fun(num - z) + 1
            dp[num] = max(take_x, take_y, take_z)
            return dp[num]
        dp = [-1 for _ in range(n + 1)]
        result = fun(n)
        return max(0, result)

  # Example usage of the Solution class
solution = Solution()

# Example inputs
n = 7
x = 2
y = 1
z = 3

# Expected output: Maximum number of cuts that can be made
result = solution.maximizeTheCuts(n, x, y, z)
print("Maximum number of cuts:", result)
