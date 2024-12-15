class Solution:
    def peakElement(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check neighbors for peak condition
            left = arr[mid - 1] if mid > 0 else float('-inf')
            right = arr[mid + 1] if mid < n - 1 else float('-inf')
            
            if arr[mid] > left and arr[mid] > right:
                return mid  # Found a peak element
            elif left > arr[mid]:
                high = mid - 1  # Search in left half
            else:
                low = mid + 1  # Search in right half
        
        return -1  # Should not reach here if input is valid

# Verification Function
def verify_peak(arr, peak_index):
    if not (0 <= peak_index < len(arr)):
        return False
    left = arr[peak_index - 1] if peak_index > 0 else float('-inf')
    right = arr[peak_index + 1] if peak_index < len(arr) - 1 else float('-inf')
    return arr[peak_index] > left and arr[peak_index] > right

# Examples
examples = [
    [1, 2, 4, 5, 7, 8, 3],
    [10, 20, 15, 2, 23, 90, 80],
    [1, 2, 3]
]

solution = Solution()
for arr in examples:
    peak_index = solution.peakElement(arr)
    print(verify_peak(arr, peak_index))  # Should print True for all examples
