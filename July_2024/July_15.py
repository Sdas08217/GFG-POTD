# Smallest number
class Solution:
    def smallestNumber(self, s, d):
        ans = ""
        rem = s

        for i in range(1, d + 1):
            if i == 1:
                sum_remaining = (d - 1) * 9
                if sum_remaining + 9 < s:
                    return "-1"
                dig = max(1, s - sum_remaining)
                s -= dig
                ans += str(dig)
                continue
            
            dig = s - (d - i) * 9
            if dig <= 0:
                ans += "0"
            else:
                ans += str(dig)
                s -= dig

        return ans
