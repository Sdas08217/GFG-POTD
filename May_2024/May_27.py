# Longest subsequence-1
class Solution:
    def longestSubseq(self, n, a):
        # Initialize a dp array with 1s because each element is a subsequence of length 1 by itself
        dp = [1] * n
        
        # Iterate through the array to fill dp array
        for i in range(1, n):
            for j in range(i):
                if abs(a[i] - a[j]) == 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # The result is the maximum value in dp array
        return max(dp)

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 7
    a1 = [10, 9, 4, 5, 4, 8, 6]
    print(sol.longestSubseq(n1, a1))  # Output: 3

    # Example 2
    n2 = 5
    a2 = [1, 2, 3, 4, 5]
    print(sol.longestSubseq(n2, a2))  # Output: 5
