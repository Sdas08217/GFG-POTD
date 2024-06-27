# The Palindrome Pattern
class Solution:
    def pattern(self, arr):
        n = len(arr)
        
        # Check rows for palindromes
        for i in range(n):
            if arr[i] == arr[i][::-1]:  # Check if row is palindrome
                return "{} R".format(i)
        
        # Check columns for palindromes
        for j in range(n):
            column = [arr[i][j] for i in range(n)]
            if column == column[::-1]:  # Check if column is palindrome
                return "{} C".format(j)
        
        return "-1"

# Example usage:
solution = Solution()
print(solution.pattern([[1, 0, 0], [0, 1, 0], [1, 1, 0]]))  # Output: "1 R"
print(solution.pattern([[1, 0], [1, 0]]))  # Output: "0 C"
