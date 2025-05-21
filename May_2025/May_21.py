class Solution(object):
    def kthSmallest(self, m, n, k):
        # Ensure m <= n to minimize the number of rows iterated
        if m > n:
            m, n = n, m
        low = 1
        high = m * n
        
        while low < high:
            mid = (low + high) // 2
            count = 0
            # Iterate through each row i from 1 to m
            for i in range(1, m + 1):
                temp = mid // i
                if temp == 0:
                    break  # No more contributions from subsequent rows
                count += min(temp, n)
            
            if count < k:
                low = mid + 1
            else:
                high = mid
        
        return low
