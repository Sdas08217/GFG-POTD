class Solution:

    def findMaximum(self, arr):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # Check boundaries to avoid index error
            if mid == 0:
                return arr[0] if arr[0] > arr[1] else arr[1]
            if mid == len(arr) - 1:
                return arr[-1] if arr[-1] > arr[-2] else arr[-2]

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
