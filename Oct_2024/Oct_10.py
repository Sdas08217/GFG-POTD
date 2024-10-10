# Max distance between same elements
class Solution:
    def maxDistance(self, arr):
        first_occurrence = {}
        max_distance = 0
        
        # Traverse the array
        for i in range(len(arr)):
            if arr[i] in first_occurrence:
                # Calculate the distance and update max_distance if necessary
                max_distance = max(max_distance, i - first_occurrence[arr[i]])
            else:
                # Store the first occurrence of the element
                first_occurrence[arr[i]] = i
        
        return max_distance

  # Example usage
arr = [1, 2, 3, 1, 4, 5, 2, 6]

# Create an instance of the Solution class
solution = Solution()

# Call the maxDistance method with the example array
result = solution.maxDistance(arr)

# Output the result
print("Maximum distance:", result)
