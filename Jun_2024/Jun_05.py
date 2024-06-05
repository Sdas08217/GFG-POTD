# Swapping pairs make sum equal
class Solution:
    def findSwapValues(self, a, n, b, m):
        sum_a = sum(a)
        sum_b = sum(b)
        
        # Calculate the difference between sums
        diff = sum_a - sum_b
        
        # If the difference is odd, it's impossible to make the sums equal by swapping
        if diff % 2 != 0:
            return -1
        
        # The value that should be equalized by swapping (half of the difference)
        target = diff // 2
        
        # Create a set for quick lookup for the larger array
        if sum_a > sum_b:
            set_a = set(a)
            for value in b:
                if value + target in set_a:
                    return 1
        else:
            set_b = set(b)
            for value in a:
                if value - target in set_b:
                    return 1
        
        return -1
      # Example usage
solution = Solution()

# Example 1
n1, m1 = 6, 4
a1 = [4, 1, 2, 1, 1, 2]
b1 = [3, 6, 3, 3]
print(solution.findSwapValues(a1, n1, b1, m1))  # Output: 1

# Example 2
n2, m2 = 4, 4
a2 = [5, 7, 4, 6]
b2 = [1, 2, 3, 8]
print(solution.findSwapValues(a2, n2, b2, m2))  # Output: 1
