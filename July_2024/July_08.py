# Search in Rotated Sorted Array
class Solution:
    def search(self, arr, target):
        right = len(arr) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            if arr[left] <= arr[mid]:
                if arr[left] <= target and target <= arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] <= target and arr[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

  # Example usage of the Solution class
arr = [4, 5, 6, 7, 0, 1, 2]  # Rotated sorted array
target = 0  # Target value to search for

# Create an instance of the Solution class
solution = Solution()

# Call the search method
result = solution.search(arr, target)

# Print the result
print(f"Index of target {target} is: {result}")  # Expected output is 4, as arr[4] == 0
