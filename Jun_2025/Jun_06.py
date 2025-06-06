class Solution:
    def computeLPSArray(self, pat):
        m = len(pat)
        lps = [0] * m
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, pat, txt):
        n = len(txt)
        m = len(pat)
        lps = self.computeLPSArray(pat)
        result = []

        i = j = 0  # index for txt and pat

        while i < n:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == m:
                result.append(i - j + 1)  # 1-based indexing
                j = lps[j - 1]
            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return result
