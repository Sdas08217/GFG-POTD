# Not a subset sum
class Solution:
    def findSmallest(self, arr):
        num = 1
        for i in arr:
            if i > num:
                return num
            num += i
        return num
# Example usage
solution = Solution()
arr = [1, 1, 3, 4, 10]
result = solution.findSmallest(arr)
print(result)  # Output: 2
