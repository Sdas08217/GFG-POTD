class Solution:
    def sumClosest(self, arr, target):
        # If the array has less than 2 elements, no pair exists
        if len(arr) < 2:
            return []
        # Sort the array
        arr.sort()
        
        # Initialize variables
        left, right = 0, len(arr) - 1
        closest_pair = []
        closest_diff = float('inf')
        max_abs_diff = float('-inf')
        
        # Two-pointer approach
        while left < right:
            a, b = arr[left], arr[right]
            current_sum = a + b
            current_diff = abs(target - current_sum)
            abs_diff = abs(b - a)
            
            # Check if the current pair is closer to the target
            if current_diff < closest_diff or (current_diff == closest_diff and abs_diff > max_abs_diff):
                closest_diff = current_diff
                max_abs_diff = abs_diff
                closest_pair = [a, b]
            
            # Move pointers based on the sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If exact match found, return immediately
                return [a, b]
        
        return closest_pair
