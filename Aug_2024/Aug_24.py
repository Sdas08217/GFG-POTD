# 0 - 1 Knapsack Problem
class Solution:

    def knapSack(self,W, wt, val):

        dp = [[0]*(W+1) for _ in range(len(val)+1)]
        for i in range(len(wt)):
            for w in range(1, W+1):
                dp[i+1][w] = dp[i][w]
                if wt[i] <= w:
                    dp[i+1][w] = max(dp[i+1][w], dp[i][w-wt[i]]+val[i])
        return dp[-1][W]

  # Example usage
W = 50  # Maximum weight of knapsack
wt = [10, 20, 30]  # Weights of items
val = [60, 100, 120]  # Values of items

solution = Solution()
max_value = solution.knapSack(W, wt, val)
print(f"The maximum value that can be carried in the knapsack is: {max_value}")
