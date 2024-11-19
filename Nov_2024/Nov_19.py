# Next Permutation
class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        # Step 1: Find the pivot
        pivot = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        if pivot == -1:
            # If no pivot is found, reverse the array
            arr.reverse()
            return arr
        # Step 2: Find the rightmost successor to the pivot
        for j in range(n - 1, pivot, -1):
            if arr[j] > arr[pivot]:
                # Swap pivot with successor
                arr[pivot], arr[j] = arr[j], arr[pivot]
                break
        # Step 3: Reverse the subarray to the right of the pivot
        arr[pivot + 1:] = reversed(arr[pivot + 1:])
        return arr
