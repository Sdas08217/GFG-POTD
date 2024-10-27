# Remove duplicates in array
class Solution:
    def removeDuplicates(self, arr):
        # Define a boolean array for values from 2 to 100
        seen = [False] * 101
        result = []

        # Traverse each element in the array
        for num in arr:
            # Check if the element has already been seen
            if not seen[num]:
                # If not seen, add to result and mark it as seen
                result.append(num)
                seen[num] = True

        return result

  # Example usage
solution = Solution()
arr1 = [2, 2, 3, 3, 7, 5]
arr2 = [2, 2, 5, 5, 7, 7]
print(solution.removeDuplicates(arr1))  # Output: [2, 3, 7, 5]
print(solution.removeDuplicates(arr2))  # Output: [2, 5, 7]
