class Solution:
    def productExceptSelf(self, arr):
        n = len(arr)
        res = [1] * n  # Initialize result array with 1s
        
        # Compute prefix product for each element
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
        
        # Compute suffix product for each element
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= arr[i]
        
        return res
