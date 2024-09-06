# Kadane's Algorithm
class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize variables
        max_so_far = arr[0]
        current_max = arr[0]
        
        # Traverse the array from the second element
        for i in range(1, len(arr)):
            # Update current_max: max of the current element or adding it to current_max
            current_max = max(arr[i], current_max + arr[i])
            
            # Update max_so_far to the maximum found so far
            max_so_far = max(max_so_far, current_max)
        
        return max_so_far

 # Example Usage:
arr = [1, 2, 3, -2, 5]
sol = Solution()
print(sol.maxSubArraySum(arr))  # Output: 9
