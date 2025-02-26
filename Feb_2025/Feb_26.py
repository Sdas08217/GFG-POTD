class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        left = [0] * n    # left[i] stores the count of consecutive elements on the left (including arr[i]) that are >= arr[i]
        right = [0] * n   # right[i] stores the count of consecutive elements on the right (including arr[i]) that are > arr[i]
        stack = []
        
        # Compute left array.
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if not stack:
                left[i] = i + 1
            else:
                left[i] = i - stack[-1]
            stack.append(i)
        
        # Clear stack for computing right.
        stack = []
        
        # Compute right array.
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if not stack:
                right[i] = n - i
            else:
                right[i] = stack[-1] - i
            stack.append(i)
        
        # res[k - 1] will hold the maximum of minimums for window size k.
        res = [0] * n
        
        # For each element arr[i], the window size for which it is the minimum is:
        # window_size = left[i] + right[i] - 1.
        # Update the candidate for that window size.
        for i in range(n):
            window_size = left[i] + right[i] - 1
            # window_size is in range [1, n], so index window_size-1
            res[window_size - 1] = max(res[window_size - 1], arr[i])
        
        # For window sizes that didn't get a direct candidate, we fill in by taking the maximum
        # from larger window sizes since a smaller window cannot have a maximum of minimums less than
        # that of a larger window.
        for i in range(n - 2, -1, -1):
            res[i] = max(res[i], res[i + 1])
        
        return res
