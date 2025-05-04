# Smallest distinct window
class Solution:
    def findSubString(self, str):
        from collections import defaultdict

        n = len(str)
        if n == 0:
            return 0

        # Step 1: Count all unique characters in the string
        unique_chars = set(str)
        total_unique = len(unique_chars)

        # Step 2: Initialize window pointers and character count
        window_count = defaultdict(int)
        formed = 0
        left = 0
        min_len = float('inf')

        # Step 3: Expand the window with 'right' pointer
        for right in range(n):
            window_count[str[right]] += 1
            if window_count[str[right]] == 1:
                formed += 1

            # Step 4: Try to contract the window from the left
            while formed == total_unique:
                min_len = min(min_len, right - left + 1)
                window_count[str[left]] -= 1
                if window_count[str[left]] == 0:
                    formed -= 1
                left += 1

        return min_len
