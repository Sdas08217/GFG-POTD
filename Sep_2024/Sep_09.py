# Sort 0s, 1s and 2s
class Solution:
    def sort012(self, arr):
        return arr.sort()
# Example Usage
  solution = Solution()
arr = [0, 2, 1, 2, 0, 1]
sorted_arr = solution.sort012(arr)
print(sorted_arr)  # Output will be [0, 0, 1, 1, 2, 2]
