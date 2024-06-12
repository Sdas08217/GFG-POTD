# Padovan Sequence
class Solution:
    def padovanSequence(self, n):
        MOD = 10**9 + 7
        
        # Base cases
        if n == 0 or n == 1 or n == 2:
            return 1
        
        # Initial Padovan sequence values
        p0, p1, p2 = 1, 1, 1
        
        # Compute Padovan sequence iteratively
        for i in range(3, n + 1):
            p3 = (p1 + p0) % MOD
            p0, p1, p2 = p1, p2, p3
        
        return p2

  # Example usage
sol = Solution()
n = 4
print(sol.padovanSequence(n))  # Output: 2
