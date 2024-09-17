# Minimize the Heights II
class Solution:
    def getMinDiff(self, arr, k):
        # Sort the array to access elements in increasing order
        arr.sort()
        
        # Initial difference between the largest and smallest towers
        initial_diff = arr[-1] - arr[0]
        
        # Variables to store the maximum and minimum heights after modification
        min_height = arr[0] + k
        max_height = arr[-1] - k
        min_diff = initial_diff
        
        for i in range(len(arr) - 1):
            new_min = min(min_height, arr[i + 1] - k)
            new_max = max(max_height, arr[i] + k)
            
            # Skip if the new minimum is negative
            if new_min < 0:
                continue
            
            # Update the minimum difference
            min_diff = min(min_diff, new_max - new_min)
        
        return min_diff

  # Example usage
solution = Solution()
arr = [1, 15, 10]
k = 6
result = solution.getMinDiff(arr, k)
print(f"The minimum difference is: {result}")
