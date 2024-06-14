# Armstrong Numbers
class Solution:
    def armstrongNumber(self, n):
        # Extract digits
        d1 = n // 100        # Hundreds place
        d2 = (n // 10) % 10  # Tens place
        d3 = n % 10          # Units place
        
        # Calculate sum of cubes of the digits
        sum_of_cubes = d1**3 + d2**3 + d3**3
        
        # Check if the sum of the cubes is equal to the original number
        if sum_of_cubes == n:
            return "true"
        else:
            return "false"

# Example usage
solution = Solution()
print(solution.armstrongNumber(153))  # Output: true
print(solution.armstrongNumber(372))  # Output: false
