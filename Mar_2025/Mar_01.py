class Solution:
    def decodedString(self, s):
        stack = []
        current_result = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
            elif s[i] == '[':
                stack.append((current_result, num))
                current_result = []
                i += 1
            elif s[i] == ']':
                prev_result, count = stack.pop()
                current_result = prev_result + current_result * count
                i += 1
            else:
                current_result.append(s[i])
                i += 1
        return ''.join(current_result)
