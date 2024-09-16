# Longest valid Parentheses
class Solution:
    def maxLength(self, str):
        stack = [-1]  # Initialize stack with base index -1
        max_len = 0

        for i, char in enumerate(str):
            if char == '(':
                stack.append(i)  # Push the index of the opening parenthesis
            else:
                stack.pop()  # Pop the matching opening parenthesis
                if stack:
                    max_len = max(max_len, i - stack[-1])  # Calculate the length
                else:
                    stack.append(i)  # Push the index of unmatched closing parenthesis

        return max_len

  # Example usage
sol = Solution()
test_str = "(()))())("
result = sol.maxLength(test_str)
print(f"Longest valid parentheses substring length: {result}")
