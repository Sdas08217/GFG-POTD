class Solution:
    def findMin(self, arr):
        # Initialize pointers
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # Compare mid with high to determine the search range
            if arr[mid] > arr[high]:
                low = mid + 1  # Minimum is in the right half
            elif arr[mid] < arr[high]:
                high = mid  # Minimum is in the left half or at mid
            else:
                # Handle duplicates: decrement high
                high -= 1
        
        # Return the minimum element
        return arr[low]
