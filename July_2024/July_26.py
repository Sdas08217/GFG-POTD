# K-Pangrams
from collections import Counter
class Solution:
    def kPangram(self,string, k):
        string = string.replace(' ', '')
        mp = Counter(string)
        cnt, total = len(mp.keys()), sum(mp.values())
        return k + cnt >= 26 and total >= 26


# Example usage
string = "the quick brown fox jumps over the lazy dog"
k = 0
print(solution.kPangram(string, k))  # Should return True, as this is already a pangram

string = "the quick brown fox"
k = 10
print(solution.kPangram(string, k))  # Should return True, as adding 10 characters can make it a pangram

string = "abcdef"
k = 20
print(solution.kPangram(string, k))  # Should return False, as even adding 20 characters won't be enough
