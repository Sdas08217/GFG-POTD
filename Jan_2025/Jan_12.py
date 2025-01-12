class Solution:
    def maxWater(self, arr):
        n = len(arr)
        if n < 3:
            return 0
        # Initialize arrays to store the left and right maximum heights
        left_max = [0] * n
        right_max = [0] * n
        # Fill left_max array
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], arr[i])
        # Fill right_max array
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])
        # Calculate trapped water
        trapped_water = 0
        for i in range(n):
            trapped_water += max(0, min(left_max[i], right_max[i]) - arr[i])
        return trapped_water
