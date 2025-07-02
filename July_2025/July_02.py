class Solution:
    def totalElements(self, arr):
        left = 0
        max_len = 0
        freq_map = {}

        for right in range(len(arr)):
            # Add current element to the frequency map
            freq_map[arr[right]] = freq_map.get(arr[right], 0) + 1

            # If more than 2 distinct elements, shrink the window
            while len(freq_map) > 2:
                freq_map[arr[left]] -= 1
                if freq_map[arr[left]] == 0:
                    del freq_map[arr[left]]
                left += 1

            # Update maximum length
            max_len = max(max_len, right - left + 1)

        return max_len
