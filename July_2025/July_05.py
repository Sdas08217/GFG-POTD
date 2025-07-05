class Solution:
    def maxSum(self, arr):
        max_sum = 0
        n = len(arr)

        for i in range(n - 1):
            a, b = arr[i], arr[i + 1]
            smallest = min(a, b)
            second_smallest = max(a, b)
            max_sum = max(max_sum, smallest + second_smallest)

        return max_sum
