# Coverage of all Zeros in a Binary Matrix
class Solution:
    def FindCoverage(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        total_coverage = 0
        
        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] == 1:
                            total_coverage += 1
        
        return total_coverage

  # Example usage:
# matrix1 = [[0, 1, 0],
#            [0, 1, 1], 
#            [0, 0, 0]]
# sol = Solution()
# print(sol.FindCoverage(matrix1))  # Output: 6

# matrix2 = [[0, 1]]
# print(sol.FindCoverage(matrix2))  # Output: 1
