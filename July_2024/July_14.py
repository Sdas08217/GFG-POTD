# Segregate 0s and 1s
class Solution:
    def segregate0and1(self, arr):
        return arr.sort()

  # Example usage
solution = Solution()
arr = [0, 1, 0, 1, 0, 1]
solution.segregate0and1(arr)
print(arr)  # Output will be: [0, 0, 0, 1, 1, 1]
