# Maximum Difference
class Solution:
    def findMaxDiff(self, arr):
        n = len(arr)
        
        # Initialize left and right smaller element arrays with zeros
        ls = [0] * n
        rs = [0] * n
        
        # Stack to find nearest smaller to left
        stack = []
        
        # Compute left smaller array
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            ls[i] = arr[stack[-1]] if stack else 0
            stack.append(i)
        
        # Clear stack to reuse for right smaller
        stack = []
        
        # Compute right smaller array
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            rs[i] = arr[stack[-1]] if stack else 0
            stack.append(i)
        
        # Calculate maximum absolute difference
        max_diff = 0
        for i in range(n):
            max_diff = max(max_diff, abs(ls[i] - rs[i]))
        
        return max_diff

# Example Usage:
arr1 = [2, 1, 8]
arr2 = [2, 4, 8, 7, 7, 9, 3]
solution = Solution()
print(solution.findMaxDiff(arr1))  # Output: 1
print(solution.findMaxDiff(arr2))  # Output: 4
