# Sorting Elements of an Array by Frequency
from collections import Counter

class Solution:
    # Function to sort the array according to frequency of elements.
    def sortByFreq(self, arr):
        # Step 1: Count the frequency of each element
        freq_map = Counter(arr)
        
        # Step 2: Sort based on frequency (high to low) and value (low to high)
        sorted_arr = sorted(arr, key=lambda x: (-freq_map[x], x))
        
        return sorted_arr

  # Example usage:
sol = Solution()

# Test case 1
arr1 = [4, 6, 9, 19, 2, 16, 13, 11, 16, 17, 16, 8, 12, 16, 12, 18]
print(sol.sortByFreq(arr1))  # Expected Output: [16, 16, 16, 16, 12, 12, 2, 4, 6, 8, 9, 11, 13, 17, 18, 19]

# Test case 2
arr2 = [9, 9, 9, 2, 5]
print(sol.sortByFreq(arr2))  # Expected Output: [9, 9, 9, 2, 5]
