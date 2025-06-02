class Solution:
    def uniquePaths(self, grid):
        n = len(grid)
        m = len(grid[0])

        # If start or end is blocked, return 0
        if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
            return 0

        # Initialize DP table
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1  # Start cell

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[i][j] = 0  # Blocked cell
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]

        return dp[n - 1][m - 1]
