class Solution:
    def subarraySum(self, arr, target):
        left, curr_sum = 0, 0
        
        for right in range(len(arr)):
            # Add the current element to the current sum
            curr_sum += arr[right]
            
            # Adjust the left pointer to ensure the current sum doesn't exceed the target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
            
            # Check if the current sum equals the target
            if curr_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based indices
        
        return [-1]  # If no subarray found
