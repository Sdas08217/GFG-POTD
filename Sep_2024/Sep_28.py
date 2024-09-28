# Minimal Cost
class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float ('inf')] * n
        dp[0] = 0
        for i in range(1, n):
            for j in range(max(0, i - k), i):
                dp[i] = min(dp[i], dp[j] + abs(arr[i] - arr[j]))
        return dp[n - 1]

# Example usage
sol = Solution()
k = 3
arr = [10, 30, 40, 20, 50]
result = sol.minimizeCost(k, arr)
print(f"The minimum cost to reach the last element is: {result}")

  
