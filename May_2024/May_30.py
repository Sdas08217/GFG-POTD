# String Subsequence
class Solution:
    def countWays(self, s1: str, s2: str) -> int:
        MOD = int(1e9 + 7)
        n, m = len(s1), len(s2)
        
        # Initialize the DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # If s2 is an empty string, there's exactly one subsequence of s1 matching it (the empty subsequence)
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n][m]
# Example usage:
solution = Solution()
s1 = "geeksforgeeks"
s2 = "gks"
print(solution.countWays(s1, s2))  # Output: 4

s1 = "problemoftheday"
s2 = "geek"
print(solution.countWays(s1, s2))  # Output: 0
