# Count ways to N'th Stair(Order does not matter)
class Solution:
    def nthStair(self, n):
        val = 0
        for i in range(0, n + 1, 2):
            val += 1
        return val

# Create an instance of the Solution class
sol = Solution()

# Example usage:
n = 5  # The stair number we want to find the number of ways to reach
result = sol.nthStair(n)

print(f"The number of ways to reach the {n}th stair is: {result}")
