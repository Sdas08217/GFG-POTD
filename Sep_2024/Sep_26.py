# Roof Top
class Solution:
    
    def maxStep(self, arr):
        n = len(arr)
        cnt = 0
        maxi = 0
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                cnt += 1
            else:
                maxi = max(maxi, cnt)
                cnt = 0
        maxi = max(maxi, cnt)
        return maxi

  # Example 1: array of increasing and decreasing elements
arr1 = [1, 2, 2, 3, 5, 6, 2, 8, 9]
result1 = sol.maxStep(arr1)
print("Maximum number of consecutive steps where arr[i] < arr[i + 1]:", result1)
