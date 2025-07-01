class Solution:
    def substrCount(self, s, k):
        from collections import defaultdict
        
        if k > len(s):
            return 0

        count = 0
        freq = defaultdict(int)
        start = 0

        for end in range(len(s)):
            freq[s[end]] += 1

            # Maintain window size of k
            if end - start + 1 > k:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1

            # Check valid window
            if end - start + 1 == k:
                if len(freq) == k - 1:
                    count += 1

        return count
