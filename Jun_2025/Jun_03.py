from collections import defaultdict

class Solution:
    def countSubstr(self, s, k):
        def count_at_most_k(s, k):
            n = len(s)
            left = 0
            count = 0
            freq = defaultdict(int)

            for right in range(n):
                freq[s[right]] += 1

                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1

                count += (right - left + 1)

            return count

        if k == 0:
            return 0
        return count_at_most_k(s, k) - count_at_most_k(s, k - 1)
