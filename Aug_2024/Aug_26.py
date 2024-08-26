# Wildcard Pattern Matching
class Solution:
    def wildCard(self, pattern, string):
        n = len(string)
        m = len(pattern)
        
        # Create a 2D DP array
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # Base case: an empty pattern can match an empty string
        dp[0][0] = True
        
        # Handle patterns that start with '*'
        for j in range(1, m + 1):
            if pattern[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if pattern[j - 1] == '*':
                    # '*' can match zero or more characters
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif pattern[j - 1] == '?' or string[i - 1] == pattern[j - 1]:
                    # '?' matches any single character, or exact character match
                    dp[i][j] = dp[i - 1][j - 1]
        
        # The result is in dp[n][m]
        return 1 if dp[n][m] else 0
# Example usage
solution = Solution()
print(solution.wildCard("?*?", "b"))   # Output: 0
print(solution.wildCard("ba*a?", "baaabab"))  # Output: 1
print(solution.wildCard("a*ab", "baaabab"))   # Output: 0
