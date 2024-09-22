# Longest Prefix Suffix
class Solution:
    def lps(self, s: str) -> int:
        n = len(s)
        lps = [0] * n  # Create lps array
        length = 0     # Length of the previous longest prefix suffix
        i = 1
        
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps[-1]  # The value of the last element in lps is the answer

# Example usage of the Solution class and lps method
solution = Solution()

# Test case
input_string = "abab"
result = solution.lps(input_string)

print(f"The length of the longest proper prefix which is also a suffix for '{input_string}' is: {result}")
