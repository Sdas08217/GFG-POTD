class Solution:    
    # Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        # Use a set to store distinct elements from both arrays
        union_set = set(a).union(set(b))
        # Return the size of the set
        return len(union_set)
# Example usage:
solution = Solution()
print(solution.findUnion([1, 2, 3, 4, 5], [1, 2, 3]))  # Output: 5
print(solution.findUnion([85, 25, 1, 32, 54, 6], [85, 2]))  # Output: 7
print(solution.findUnion([1, 2, 1, 1, 2], [2, 2, 1, 2, 1]))  # Output: 2
