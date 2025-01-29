class Solution:
    def power(self, b: float, e: int) -> float:
        # Handle negative exponents
        if e < 0:
            b = 1 / b
            e = -e
        result = 1.0
        base = b
        while e > 0:
            if e % 2 == 1:  # If e is odd
                result *= base
            base *= base  # Square the base
            e //= 2  # Reduce exponent
        return round(result, 5)  # Round to 5 decimal places as required
