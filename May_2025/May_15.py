class Solution:
    def countSubstring(self, s):
        # Dictionary to store frequency of characters seen so far
        freq = {}
        count = 0
        
        # Iterate through the string
        for c in s:
            # Add the number of substrings ending with current character
            count += freq.get(c, 0) + 1
            
            # Update the frequency of the current character
            freq[c] = freq.get(c, 0) + 1
        
        return count
