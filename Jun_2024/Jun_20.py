# Integral Points Inside Triangle
class Solution:
    def gcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    def triangle_area(self, p, q, r):
        return abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]))

    def boundary_points(self, p, q, r):
        return (self.gcd(abs(p[0] - q[0]), abs(p[1] - q[1])) + 
                self.gcd(abs(q[0] - r[0]), abs(q[1] - r[1])) + 
                self.gcd(abs(r[0] - p[0]), abs(r[1] - p[1])))

    def InternalCount(self, p, q, r):
        return (self.triangle_area(p, q, r) - self.boundary_points(p, q, r) + 2) // 2

  # Define the points of the triangle
p = (1, 1)
q = (5, 3)
r = (3, 7)

# Create an instance of the Solution class
solution = Solution()

# Calculate the number of internal lattice points
internal_points = solution.InternalCount(p, q, r)

# Output the result
print("Number of internal lattice points:", internal_points)
