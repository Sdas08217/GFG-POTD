# Two Smallests in Every Subarray
class Solution:
    def pairWithMaxSum(self, arr):
        n = len(arr)
        
        # If there are less than 2 elements, return -1
        if n < 2:
            return -1
        
        # Initialize max_sum with the smallest possible value
        max_sum = -1
        
        # Traverse the array and find the max sum of adjacent pairs
        for i in range(n - 1):
            max_sum = max(max_sum, arr[i] + arr[i + 1])
        
        return max_sum

# Example usage
arr = [1, 9, 3, 10, 5, 7]
sol = Solution()
result = sol.pairWithMaxSum(arr)
print("The maximum sum of adjacent pairs is:", result)

