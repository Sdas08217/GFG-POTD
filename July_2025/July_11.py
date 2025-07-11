class Solution:
    def countConsec(self, n: int) -> int:
        # Total number of binary strings of length n
        total = 2 ** n

        # dp[i] will store number of binary strings of length i without consecutive 1s
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string
        dp[1] = 2  # "0" and "1"

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # Subtract number of strings without consecutive 1s from total
        return total - dp[n]
