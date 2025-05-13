class Solution:
    def nCr(self, n, r):
        # Edge cases
        if r > n:
            return 0
        if r == 0 or r == n:
            return 1

        # Use the property C(n, r) = C(n, n - r) for optimization
        r = min(r, n - r)
        result = 1

        for i in range(r):
            result *= (n - i)
            result //= (i + 1)

        return result
