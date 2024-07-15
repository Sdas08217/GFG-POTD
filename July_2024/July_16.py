# Remaining String
class Solution:
    def printString(self, s, ch, count):
        # Initialize the count of occurrences of ch
        current_count = 0
        
        # Iterate through the string
        for i in range(len(s)):
            if s[i] == ch:
                current_count += 1
            if current_count == count:
                return s[i+1:]
        
        # If count occurrences of ch is not found
        return ""

  # Example usage:
sol = Solution()
print(sol.printString("Thisisdemostring", 'i', 3))  # Output: "ng"
print(sol.printString("Thisisdemostri", 'i', 3))    # Output: ""
print(sol.printString("abcd", 'x', 2))              # Output: ""
