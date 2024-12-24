class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Binary search initialization
        low, high = 0, n * m - 1
        
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            
            # Access the element in the matrix
            mid_value = mat[row][col]
            
            if mid_value == x:
                return True
            elif mid_value < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
