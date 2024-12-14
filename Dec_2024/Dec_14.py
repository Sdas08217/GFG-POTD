class Solution:
    def search(self, arr, key):
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is the target
            if arr[mid] == key:
                return mid
            
            # Determine which half is sorted
            if arr[low] <= arr[mid]:  # Left half is sorted
                if arr[low] <= key < arr[mid]:
                    high = mid - 1  # Search in the left half
                else:
                    low = mid + 1   # Search in the right half
            else:  # Right half is sorted
                if arr[mid] < key <= arr[high]:
                    low = mid + 1   # Search in the right half
                else:
                    high = mid - 1  # Search in the left half
        
        return -1  # Key not found
