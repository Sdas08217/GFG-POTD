class Solution:
    # Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x):
        for row in mat:
            # Apply binary search on each row
            low, high = 0, len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == x:
                    return True  # Element found
                elif row[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
        return False  # Element not found
