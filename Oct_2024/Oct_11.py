# Reorganize The Array
class Solution:
    def rearrange(self, arr):
        result = [-1] * len(arr)
        for value in arr:
            if 0 <= value < len(arr):
                result[value] = value
        return result

  # Example usage
arr = [3, -1, 2, 1, 5, -1, 0]
sol = Solution()
result = sol.rearrange(arr)
print(result)
