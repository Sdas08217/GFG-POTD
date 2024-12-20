class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
        n, m = len(mat), len(mat[0])
        result = []
        top, left = 0, 0
        bottom, right = n - 1, m - 1
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        return result
# Example usage
solution = Solution()
matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(solution.spirallyTraverse(matrix1))  # Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
matrix2 = [[32, 44, 27, 23], [54, 28, 50, 62]]
print(solution.spirallyTraverse(matrix2))  # Output: [32, 44, 27, 23, 62, 50, 28, 54]
