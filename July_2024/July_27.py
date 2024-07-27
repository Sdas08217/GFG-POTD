# Form a palindrome
class Solution:
    def countMin(self, s):
        dp = [[0] * len(s) for _ in range(len(s))]
        maxLen = 0
        for i in reversed(range(len(s))):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 2)
                maxLen = max(dp[i][j], maxLen)

        return len(s) - maxLen

  # Example usage:
sol = Solution()
example_string = "abca"
result = sol.countMin(example_string)
print(f"The minimum number of insertions to make '{example_string}' a palindrome is: {result}")
