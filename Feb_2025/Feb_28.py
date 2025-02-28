class Solution:
    def evaluate(self, arr):
        stack = []
        for token in arr:
            if token in {'+', '-', '*', '/'}:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = int(operand1 / operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
