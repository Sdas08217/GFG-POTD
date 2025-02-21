class Solution:
    def isBalanced(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}  # Mapping of closing to opening brackets

        for char in s:
            if char in bracket_map.values():  # If it is an opening bracket
                stack.append(char)
            elif char in bracket_map.keys():  # If it is a closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False  # Unmatched or incorrect order
                stack.pop()  # Correct match, remove the opening bracket
            else:
                return False  # Invalid character (though constraints guarantee valid input)
        
        return len(stack) == 0  # Check if any unmatched opening brackets remain
