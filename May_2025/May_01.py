import math

class Solution:

    def nthRowOfPascalTriangle(self, n):
        # Adjust for 1-based indexing by subtracting 1
        n -= 1
        row = [math.comb(n, k) for k in range(n + 1)]
        return row
