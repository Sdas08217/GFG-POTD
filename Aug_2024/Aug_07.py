# K-th element of two Arrays
class Solution:
    def kthElement(self, k, arr1, arr2):
        def kth(arr1, arr2, k):
            if len(arr1) > len(arr2):
                return kth(arr2, arr1, k)
            if len(arr1) == 0:
                return arr2[k-1]
            if k == 1:
                return min(arr1[0], arr2[0])

            i = min(len(arr1), k // 2)
            j = min(len(arr2), k // 2)

            if arr1[i-1] > arr2[j-1]:
                return kth(arr1, arr2[j:], k-j)
            else:
                return kth(arr1[i:], arr2, k-i)

        return kth(arr1, arr2, k)

  # Example usage:
solution = Solution()
print(solution.kthElement(5, [2, 3, 6, 7, 9], [1, 4, 8, 10]))  # Output: 6
print(solution.kthElement(7, [100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892]))  # Output: 256
"""

with open("/mnt/data/kth_element.py", "w") as file:
    file.write(code)
