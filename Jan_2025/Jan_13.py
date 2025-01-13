class Solution:
    def maxWater(self, arr):
        left = 0
        right = len(arr) - 1
        max_area = 0
        
        while left < right:
            # Calculate the area between the two lines at indices left and right
            height = min(arr[left], arr[right])
            width = right - left
            max_area = max(max_area, height * width)
            
            # Move the pointer pointing to the smaller height
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
