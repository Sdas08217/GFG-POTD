class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        char_map = {}
        start = 0
        max_len = -1

        for end in range(n):
            # Add current character to the map
            char_map[s[end]] = char_map.get(s[end], 0) + 1

            # Shrink window if there are more than k distinct characters
            while len(char_map) > k:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1

            # Check and update max_len if exactly k distinct characters
            if len(char_map) == k:
                max_len = max(max_len, end - start + 1)

        return max_len
