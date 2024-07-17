# Longest alternating subsequence 
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        if not arr:
            return 0

        up = 1
        down = 1

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up = down + 1
            elif arr[i] < arr[i - 1]:
                down = up + 1

        return max(up, down)

  # Example usage
solution = Solution()
arr1 = [1, 5, 4]
arr2 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]

print(solution.alternatingMaxLength(arr1))  # Output: 3
print(solution.alternatingMaxLength(arr2))  # Output: 7
