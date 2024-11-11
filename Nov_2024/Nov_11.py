# Make array elements unique
class Solution:
    def minIncrements(self, arr):
        arr.sort()
        increments = 0
        
        # Iterate over the sorted array starting from the second element
        for i in range(1, len(arr)):
            # If the current element is less than or equal to the previous element
            if arr[i] <= arr[i - 1]:
                # Calculate the required increment to make it unique
                needed_increment = arr[i - 1] + 1 - arr[i]
                # Add to the increments count
                increments += needed_increment
                # Update the current element to be unique
                arr[i] = arr[i - 1] + 1
                
        return increments

  # Example usage
arr = [3, 2, 1, 2, 1, 7]
solution = Solution()
result = solution.minIncrements(arr)
print("Minimum increments required to make all elements unique:", result)
