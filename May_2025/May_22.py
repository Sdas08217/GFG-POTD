class Solution:
    def minDeletions(self, s: str) -> int:
        n = len(s)
        
        # Create a DP table for Longest Palindromic Subsequence (LPS)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the table for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # Minimum deletions = total length - length of longest palindromic subsequence
        return n - dp[0][n - 1]
