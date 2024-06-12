# Count numbers containing 4
class Solution:
    def countNumberswith4(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if '4' in str(i):
                count += 1
        return count
# Example usage:
sol = Solution()
n = 44
print(sol.countNumberswith4(n))  # Output: 9
