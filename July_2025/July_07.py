class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n  # Initialize result with -1s
        stack = []  # Stack to store indices

        # Traverse the array twice to simulate circular behavior
        for i in range(2 * n):
            current = arr[i % n]
            # While the stack is not empty and current element is greater
            while stack and arr[stack[-1]] < current:
                res[stack.pop()] = current
            # Only push indices from the first pass
            if i < n:
                stack.append(i)

        return res
