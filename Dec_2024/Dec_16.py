class Solution:
    def kthElement(self, a, b, k):
        n, m = len(a), len(b)
        # Ensure that a is the smaller array
        if n > m:
            return self.kthElement(b, a, k)
        # Binary search over the smaller array
        low, high = max(0, k - m), min(k, n)
        while low <= high:
            mid_a = (low + high) // 2
            mid_b = k - mid_a
            left_a = a[mid_a - 1] if mid_a > 0 else float('-inf')
            right_a = a[mid_a] if mid_a < n else float('inf')
            left_b = b[mid_b - 1] if mid_b > 0 else float('-inf')
            right_b = b[mid_b] if mid_b < m else float('inf')
            # Check if partition is correct
            if left_a <= right_b and left_b <= right_a:
                return max(left_a, left_b)
            # Adjust search range
            elif left_a > right_b:
                high = mid_a - 1
            else:
                low = mid_a + 1
        return -1  # Invalid case (shouldn't occur with valid input)
# Example usage
a = [100, 112, 256, 349, 770]
b = [72, 86, 113, 119, 265, 445, 892]
k = 7
solution = Solution()
print(solution.kthElement(a, b, k))  # Output: 256
