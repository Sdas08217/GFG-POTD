class Solution:
    def __init__(self):
        # Main stack to hold elements
        self.stack = []
        # Auxiliary stack to hold the minimum values
        self.min_stack = []

    # Add an element to the top of Stack
    def push(self, x):
        self.stack.append(x)
        # If min_stack is empty or x is smaller than or equal to the top, push to min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    # Remove the top element from the Stack
    def pop(self):
        if self.stack:
            popped_value = self.stack.pop()
            # If the popped value is the current minimum, pop from min_stack as well
            if popped_value == self.min_stack[-1]:
                self.min_stack.pop()

    # Returns top element of Stack
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return -1

    # Finds minimum element of Stack
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return -1
