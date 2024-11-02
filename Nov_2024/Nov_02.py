# Kth distance
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        seen = set()
        
        for i in range(len(arr)):
            if arr[i] in seen:
                return True
            seen.add(arr[i])
            if i >= k:
                seen.remove(arr[i - k])
        
        return False

  # Example usage
arr = [1, 2, 3, 1, 4, 5]
k = 3
solution = Solution()
result = solution.checkDuplicatesWithinK(arr, k)
print("Contains duplicates within k distance:", result)
