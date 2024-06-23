# Summed Matrix
class Solution:
    def sumMatrix(self, n, q):
        if q < 2 or q > 2 * n:
            return 0
        else:
            if q <= n + 1:
                return q - 1
            else:
                return 2 * n - q + 1


      # Example usage:
sol = Solution()
print(sol.sumMatrix(4, 7))  # Output: 2
print(sol.sumMatrix(5, 4))  # Output: 3
