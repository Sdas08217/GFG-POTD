# Rotate and delete
class Solution:
    def rotateDelete(self,  arr):
        n = len(arr)
        for k in range(1, n // 2 + 1):
            arr.insert(0, arr.pop())
            arr.pop(-k)
        return arr[0]

  # Example usage:
sol = Solution()
arr = [1, 2, 3, 4, 5, 6]
result = sol.rotateDelete(arr)
print(result)  # Output will be the last remaining element after all deletions and rotations
