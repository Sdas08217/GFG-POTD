class Solution:
    def smallestDivisor(self, arr, k):
        def compute_sum(divisor):
            return sum((x + divisor - 1) // divisor for x in arr)

        low, high = 1, max(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            total = compute_sum(mid)

            if total <= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1

        return result
