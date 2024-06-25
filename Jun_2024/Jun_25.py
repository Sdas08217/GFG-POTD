# Left Rotate Matrix K times
class Solution:
    def rotateMatrix(self, k, mat):
        n = len(mat)
        k = k % len(mat[0])
        for i in range(n):
            mat[i] = mat[i][k:] + mat[i][:k]
        return mat
# Example usage:
sol = Solution()

# Example matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Number of positions to rotate
k = 2

# Rotate the matrix
rotated_matrix = sol.rotateMatrix(k, matrix)

# Output the result
for row in rotated_matrix:
    print(row)

  
