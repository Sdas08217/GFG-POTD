# Partitions with Given Difference

from typing import List

MOD = 10**9 + 7

class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        total_sum = sum(arr)
        
        # If (total_sum + d) is odd, it cannot be split into two equal integer parts
        if (total_sum + d) % 2 != 0:
            return 0
        
        target_sum = (total_sum + d) // 2
        
        # Initialize dp array
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # There is one way to make sum 0, by not selecting any elements
        
        # Fill dp array
        for num in arr:
            for j in range(target_sum, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD
        
        return dp[target_sum]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.countPartitions(4, 3, [5, 2, 6, 4]))  # Output: 1
    print(solution.countPartitions(4, 0, [1, 1, 1, 1]))  # Output: 6
