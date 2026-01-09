from collections import defaultdict

class Solution:
    def countAtMostK(self, arr, k):
        left = 0
        freq = defaultdict(int)
        ans = 0

        for right in range(len(arr)):
            freq[arr[right]] += 1

            # If distinct elements exceed k, shrink window
            while len(freq) > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            # Count valid subarrays ending at right
            ans += (right - left + 1)

        return ans
