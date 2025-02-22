class Solution:
    def maxLength(self, s: str) -> int:
        stack = [-1]  # Initialize stack with a base index.
        max_len = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:  # ch == ')'
                stack.pop()  # Pop the last index.
                if not stack:
                    # Stack is empty, push current index as a new base.
                    stack.append(i)
                else:
                    # Calculate valid substring length.
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len
