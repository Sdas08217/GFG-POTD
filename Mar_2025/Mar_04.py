from bisect import bisect_left

class Solution:
    def lis(self, arr):
        if not arr:
            return 0
        
        # Uncomment the approach you want to use

        # Approach 1: O(n²) Dynamic Programming
        """
        n = len(arr)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        """
        
        # Approach 2: O(n log n) Binary Search + DP
        sub = []
        for num in arr:
            pos = bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        
        return len(sub)
