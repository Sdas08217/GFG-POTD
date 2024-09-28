# Total count
class Solution:
    def totalCount(self, k, arr):
        total_parts = 0
        for num in arr:
            # Calculate the number of parts for each element num
            total_parts += (num + k - 1) // k
        return total_parts

# Example usage
solution = Solution()

# Example 1
k1 = 3
arr1 = [5, 8, 10, 13]
print(solution.totalCount(k1, arr1))  # Output: 14

# Example 2
k2 = 4
arr2 = [10, 2, 3, 4, 7]
print(solution.totalCount(k2, arr2))  # Output: 8
