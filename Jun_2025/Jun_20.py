from collections import Counter

class Solution:
    def validgroup(self, arr, k):
        if len(arr) % k != 0:
            return False

        freq = Counter(arr)
        for num in sorted(freq):
            count = freq[num]
            if count > 0:
                for i in range(1, k):
                    next_num = num + i
                    if freq[next_num] < count:
                        return False
                    freq[next_num] -= count
        return True
