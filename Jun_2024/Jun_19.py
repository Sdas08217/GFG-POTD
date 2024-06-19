# Find maximum volume of a cuboid
class Solution:
    def maxVolume(self, p, a):
        x = (p - math.sqrt(p ** 2 - 24 * a)) / 12
        V = (p * x ** 2 - 8 * x ** 3) / 4
        return round(V, 2)

  # Example usage
sol = Solution()
p = 30  # Example value for p
a = 10  # Example value for a
result = sol.maxVolume(p, a)
print(result)  # Output will be the maximum volume rounded to 2 decimal places
