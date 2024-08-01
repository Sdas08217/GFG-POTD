# Spirally traversing a matrix
class Solution:
    def spirallyTraverse(self, matrix):
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        result = []
        while l <= r and t <= b:
            for i in range(l, r + 1):
                result.append(matrix[t][i])
            t += 1
            for i in range(t, b + 1):
                result.append(matrix[i][r])
            r -= 1
            if t <= b:
                for i in range(r, l - 1, -1):
                    result.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    result.append(matrix[i][l])
                l += 1
        return result

  # Example usage
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

solution = Solution()
result = solution.spirallyTraverse(matrix)
print(result)
