# Compare two fractions
class Solution:
    def compareFrac(self, s):
        # Splitting the input string into two fractions
        fraction1, fraction2 = s.split(", ")
        
        # Extracting numerators and denominators
        a, b = map(int, fraction1.split("/"))
        c, d = map(int, fraction2.split("/"))
        
        # Calculating decimal values
        value1 = a / b
        value2 = c / d
        
        # Comparing the decimal values
        if value1 > value2:
            return fraction1
        elif value1 < value2:
            return fraction2
        else:
            return "equal"

# Testing the solution
sol = Solution()
print(sol.compareFrac("5/6, 11/45"))   # Output: "5/6"
print(sol.compareFrac("8/1, 8/1"))     # Output: "equal"
print(sol.compareFrac("10/17, 9/10"))  # Output: "9/10"
