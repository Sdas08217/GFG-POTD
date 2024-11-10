# Union of Two Sorted Arrays with Distinct Elements
class Solution:
    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        i, j = 0, 0
        result = []
        
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                if len(result) == 0 or result[-1] != b[j]:
                    result.append(b[j])
                j += 1
            else:
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1
        
        # Add remaining elements of a[]
        while i < len(a):
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
        
        # Add remaining elements of b[]
        while j < len(b):
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1
        
        return result

  # Example usage
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]

# Create an instance of the Solution class
solution = Solution()

# Call the findUnion method and print the result
print("Union of arrays:", solution.findUnion(a, b))
