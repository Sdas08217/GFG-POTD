# Trail of ones
class Solution:
    def numberOfConsecutiveOnes(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 2:
            return 1
        
        # Initialize dp array where dp[i] represents the number of binary strings
        # of length i that do not contain consecutive '1's.
        dp = [0] * (n + 1)
        
        # Base cases
        dp[1] = 2  # "0" and "1"
        dp[2] = 3  # "00", "01", "10"
        
        # Fill the dp array using the recurrence relation
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
        # The total number of binary strings of length n is 2^n
        total_strings = pow(2, n, MOD)
        
        # The number of binary strings of length n with consecutive '1's
        result = (total_strings - dp[n] + MOD) % MOD
        
        return result
# Example usage:
sol = Solution()
print(sol.numberOfConsecutiveOnes(2))  # Output: 1
print(sol.numberOfConsecutiveOnes(5))  # Output: 19
