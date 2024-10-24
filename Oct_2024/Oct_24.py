# Modify The Array
class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)

        # Step 1: Modify the array by doubling and setting next element to 0 if consecutive are equal
        for i in range(n - 1):
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] *= 2  # Double the current element
                arr[i + 1] = 0  # Set the next element to 0

        # Step 2: Rearrange the array to move all non-zero elements to the front
        # Using two pointers to shift non-zero elements to the left
        non_zero_index = 0

        for i in range(n):
            if arr[i] != 0:
                arr[non_zero_index] = arr[i]
                non_zero_index += 1

        # Fill the rest of the array with 0s
        for i in range(non_zero_index, n):
            arr[i] = 0

        return arr  # Optional, if needed to return modified array
# Example usage
arr = [2, 2, 0, 4, 4, 8]
solution = Solution()
result = solution.modifyAndRearrangeArr(arr)
print(result)  # Output will be [4, 8, 8, 0, 0, 0]
