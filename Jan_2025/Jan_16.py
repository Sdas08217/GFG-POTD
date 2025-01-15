class Solution:
    def maxLen(self, arr):
        # Initialize variables
        prefix_sum = 0
        max_len = 0
        prefix_map = {}

        # Traverse the array
        for i in range(len(arr)):
            # Replace 0 with -1 for calculation
            prefix_sum += 1 if arr[i] == 1 else -1

            # If prefix_sum is 0, update max_len
            if prefix_sum == 0:
                max_len = i + 1

            # If prefix_sum is seen before, calculate subarray length
            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
            else:
                # Store the first occurrence of the prefix_sum
                prefix_map[prefix_sum] = i

        return max_len

# Example usage
# Create an instance of the Solution class
solution = Solution()

# Test cases
arr1 = [1, 0, 1, 1, 1, 0, 0]
print(solution.maxLen(arr1))  # Output: 6

arr2 = [0, 0, 1, 1, 0]
print(solution.maxLen(arr2))  # Output: 4

arr3 = [0]
print(solution.maxLen(arr3))  # Output: 0
