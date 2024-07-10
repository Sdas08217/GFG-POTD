# Largest square formed in a matrix
from typing import List

class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        memo = {}
        def dp(i,j):
            if i >= n or j >= m:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if mat[i][j] == 1:
                ans = min(dp(i+1,j), dp(i,j+1), dp(i+1,j+1)) + 1
                memo[(i,j)] = ans
                return ans
            memo[(i,j)] = 0
            return 0
            
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dp(i,j))

        return ans

  # Example usage
solution = Solution()
matrix = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]
n = len(matrix)
m = len(matrix[0])

result = solution.maxSquare(n, m, matrix)
print(f"The size of the largest square sub-matrix with all 1s is: {result}")
