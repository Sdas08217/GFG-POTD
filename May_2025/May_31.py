class Solution:
    def count_less_equal(self, matrix, mid, n):
        count = 0
        row = n - 1
        col = 0
        
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += (row + 1)
                col += 1
            else:
                row -= 1
        return count

    def kthSmallest(self, matrix, k):
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        
        while low < high:
            mid = (low + high) // 2
            count = self.count_less_equal(matrix, mid, n)
            
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
