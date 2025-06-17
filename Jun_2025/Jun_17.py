import bisect

class Solution:
    def minimumCoins(self, arr, k):
        arr.sort()
        n = len(arr)

        # Prefix sum of sorted array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        total = prefix[n]
        ans = float('inf')

        for i in range(n):
            base = arr[i]
            max_allowed = base + k

            # Find first index where arr[j] > base + k
            right = bisect.bisect_right(arr, max_allowed)

            # Coins to remove from smaller piles (before i)
            remove_left = prefix[i]

            # Coins to remove from larger piles (after right-1)
            remove_right = total - prefix[right] - (max_allowed * (n - right))

            total_remove = remove_left + remove_right
            ans = min(ans, total_remove)

        return ans
