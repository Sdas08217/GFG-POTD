class Solution:
    def findTarget(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            if mid > low and arr[mid - 1] == target:
                return mid - 1
            if mid < high and arr[mid + 1] == target:
                return mid + 1

            if target < arr[mid]:
                high = mid - 2
            else:
                low = mid + 2

        return -1
