# Toeplitz matrix
def isToepliz(mat):
    n = len(mat)
    m = len(mat[0])
    
    # Check each element (except those in the last row and last column)
    for i in range(n - 1):
        for j in range(m - 1):
            if mat[i][j] != mat[i + 1][j + 1]:
                return 0
    
    return 1

# Example usage:
mat1 = [
    [6, 7, 8],
    [4, 6, 7],
    [1, 4, 6]
]
print(isToepliz(mat1))  # Output: 1

mat2 = [
    [1, 2, 3],
    [4, 5, 6]
]
print(isToepliz(mat2))  # Output: 0
