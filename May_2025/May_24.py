class Solution:
    def sumSubstrings(self, s):
        n = len(s)
        total_sum = 0
        prev_sum = 0

        for i in range(n):
            num = int(s[i])
            prev_sum = prev_sum * 10 + num * (i + 1)
            total_sum += prev_sum

        return total_sum
