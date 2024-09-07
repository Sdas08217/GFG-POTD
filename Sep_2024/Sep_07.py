# Nth Natural Number
class Solution:
    def findNth(self, n: int) -> int:
        result = 0
        multiplier = 1
        
        # Convert n to base 9, effectively skipping numbers containing '9'
        while n > 0:
            result += (n % 9) * multiplier
            n //= 9
            multiplier *= 10
        
        return result

# Example usage:
sol = Solution()
n = 19
print(sol.findNth(n))  # Output: 21
