# Sum of Middle elements of two sorted arrays
import bisect

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):

        for i in arr2:
            bisect.insort(arr1, i)

        leng = len(arr1)
        return arr1[leng // 2] + arr1[leng // 2 - 1]

  # Example usage
sol = Solution()

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

result = sol.sum_of_middle_elements(arr1, arr2)
print(f"The sum of the middle elements is: {result}")
