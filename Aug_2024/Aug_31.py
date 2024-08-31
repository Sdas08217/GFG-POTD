# Sorted subsequence of size 3
class Solution:
    def find3Numbers(self, arr):
        smallest = 10**9
        for i in range(0,len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                for j in range(i+1,len(arr)):
                    if arr[i] < arr[j]:
                        for k in range(j+1,len(arr)):
                            if arr[j] < arr[k]:
                                return [arr[i],arr[j],arr[k]]
        return []

  # Example usage:
solution = Solution()

# Test cases
arr1 = [1, 2, 1, 1, 3]
arr2 = [1, 1, 3]
arr3 = [109, 262, 93, 737, 537]
arr4 = [10, 20, 30, 40, 50]
arr5 = [5, 4, 3, 2, 1]

print(solution.find3Numbers(arr1))  # Expected output: [1, 2, 3] or similar valid subsequence
print(solution.find3Numbers(arr2))  # Expected output: [] (no valid subsequence)
print(solution.find3Numbers(arr3))  # Expected output: [109, 262, 737] or similar valid subsequence
print(solution.find3Numbers(arr4))  # Expected output: [10, 20, 30] or similar valid subsequence
print(solution.find3Numbers(arr5))  # Expected output: [] (no valid subsequence)
