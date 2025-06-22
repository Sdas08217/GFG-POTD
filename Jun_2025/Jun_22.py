class Solution:
    def largestSubset(self, arr):
        n = len(arr)
        arr.sort(reverse=True)  # For lexicographically greatest subset
        dp = [1] * n
        prev = [-1] * n

        max_len = 1
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if arr[j] % arr[i] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # Reconstruct the subset
        subset = []
        while max_idx != -1:
            subset.append(arr[max_idx])
            max_idx = prev[max_idx]

        return sorted(subset)  # Return in ascending order
