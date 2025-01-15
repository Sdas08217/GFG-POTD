class Solution:
    def longestSubarray(self, arr, k):  
        # Initialize variables
        prefix_sum = 0
        max_len = 0
        prefix_map = {}
        
        # Traverse the array
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            # Check if the prefix sum is equal to k
            if prefix_sum == k:
                max_len = i + 1
            
            # Check if (prefix_sum - k) exists in the map
            if prefix_sum - k in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum - k])
            
            # Store prefix_sum in map if it is not already present
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
        
        return max_len

# Example usage
# Create an instance of the Solution class
solution = Solution()

# Test cases
arr1 = [10, 5, 2, 7, 1, -10]
k1 = 15
print(solution.longestSubarray(arr1, k1))  # Output: 6

arr2 = [-5, 8, -14, 2, 4, 12]
k2 = -5
print(solution.longestSubarray(arr2, k2))  # Output: 5

arr3 = [10, -10, 20, 30]
k3 = 5
print(solution.longestSubarray(arr3, k3))  # Output: 0
