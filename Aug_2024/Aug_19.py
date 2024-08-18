# Kth Smallest

import random

class Solution:

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quickselect(self, arr, low, high, k):
        if low <= high:
            pivot_index = random.randint(low, high)
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            
            pi = self.partition(arr, low, high)
            
            if pi == k:
                return arr[pi]
            elif pi < k:
                return self.quickselect(arr, pi + 1, high, k)
            else:
                return self.quickselect(arr, low, pi - 1, k)
        return None

    def kthSmallest(self, arr, k):
        # k is 1-based index, so convert it to 0-based index for processing
        return self.quickselect(arr, 0, len(arr) - 1, k - 1)

  # Example usage
solution = Solution()
arr1 = [7, 10, 4, 3, 20, 15]
k1 = 3
print(solution.kthSmallest(arr1, k1))  # Output: 7

arr2 = [7, 10, 4, 20, 15]
k2 = 4
print(solution.kthSmallest(arr2, k2))  # Output: 15

# Additional test case
arr3 = [7, 3, 8, 2, 6, 5, 1, 4]
k3 = 5
print(solution.kthSmallest(arr3, k3))  # Output: 5
