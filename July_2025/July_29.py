class Solution:
    def asciirange(self, s):
        first_index = {}
        last_index = {}

        # Record first and last occurrence of each character
        for i, ch in enumerate(s):
            if ch not in first_index:
                first_index[ch] = i
            last_index[ch] = i

        result = []

        # Compute ASCII sum between first and last occurrence
        for ch in first_index:
            start = first_index[ch]
            end = last_index[ch]
            if end > start + 1:
                ascii_sum = sum(ord(s[i]) for i in range(start + 1, end))
                if ascii_sum > 0:
                    result.append(ascii_sum)

        return result
