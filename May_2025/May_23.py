class Solution:
    def noOfWays(self, m, n, x):
        # Initialize a DP table where dp[i][j] is the number of ways
        # to get sum j using i dice
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # Base case: one way to reach sum 0 with 0 dice

        # Fill the DP table
        for dice in range(1, n + 1):
            for total in range(1, x + 1):
                for face in range(1, m + 1):
                    if total - face >= 0:
                        dp[dice][total] += dp[dice - 1][total - face]

        return dp[n][x]
