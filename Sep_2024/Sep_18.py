# Parenthesis Checker
class Solution:
    def ispar(self, x):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for char in x:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack
# Example usage
sol = Solution()

# Test cases
print(sol.ispar("()"))       # Output: True
print(sol.ispar("()[]{}"))   # Output: True
print(sol.ispar("(]"))       # Output: False
print(sol.ispar("([)]"))     # Output: False
print(sol.ispar("{[]}"))     # Output: True
  
