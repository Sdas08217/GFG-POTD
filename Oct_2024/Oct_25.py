# Alternative Sorting
class Solution:
    def alternateSort(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize pointers
        n = len(arr)
        result = []
        left, right = 0, n - 1
        
        # Step 3: Build the result array
        while left <= right:
            if right >= left:
                result.append(arr[right])  # Take the largest
                right -= 1
            if left <= right:
                result.append(arr[left])   # Take the smallest
                left += 1
        
        return result

  # Example usage
arr1 = [7, 1, 2, 3, 4, 5, 6]
arr2 = [1, 6, 9, 4, 3, 7, 8, 2]

# Create an instance of the Solution class
solution = Solution()

# Call the alternateSort method
result1 = solution.alternateSort(arr1)
result2 = solution.alternateSort(arr2)

print("Input:", arr1)
print("Output:", result1)  # Expected output: [7, 1, 6, 2, 5, 3, 4]

print("\nInput:", arr2)
print("Output:", result2)  # Expected output: [9, 1, 8, 2, 7, 3, 6, 4]
