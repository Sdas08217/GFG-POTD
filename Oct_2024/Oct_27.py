# Triplet Family
class Solution:
    def findTriplet(self, arr):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)
        # Step 2: Iterate over each element as the "third" element
        for i in range(n):
            left, right = 0, i - 1  # Use two pointers on the left part of the array
            # Step 3: Use two-pointer technique to find a valid pair
            while left < right:
                # Check if the sum of arr[left] and arr[right] equals arr[i]
                if arr[left] + arr[right] == arr[i]:
                    return True  # Triplet found
                elif arr[left] + arr[right] < arr[i]:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum
        # No valid triplet found
        return False

  # Example usage
arr = [1, 2, 3, 4, 5]  # Example array
solution = Solution()
result = solution.findTriplet(arr)
print("Triplet found:", result)  # Output should be True if a valid triplet exists
