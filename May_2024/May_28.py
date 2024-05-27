# Minimum cost to fill given weight in a bag
from typing import List

class Solution:
    def minimumCost(self, n: int, w: int, cost: List[int]) -> int:
        # Create a dp array to store the minimum cost to buy exactly j kg of oranges
        dp = [float('inf')] * (w + 1)
        dp[0] = 0  # Base case: cost to buy 0 kg is 0

        # Fill the dp array
        for j in range(1, w + 1):
            for i in range(1, n + 1):
                if i <= j and cost[i - 1] != -1:
                    dp[j] = min(dp[j], dp[j - i] + cost[i - 1])

        # If dp[w] is still infinity, return -1, else return dp[w]
        return -1 if dp[w] == float('inf') else dp[w]
      # Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 5
    cost1 = [20, 10, 4, 50, 100]
    w1 = 5
    print(sol.minimumCost(n1, cost1, w1))  # Output: 14

    # Example 2
    n2 = 5
    cost2 = [-1, -1, 4, 3, -1]
    w2 = 5
    print(sol.minimumCost(n2, cost2, w2))  # Output: -1
