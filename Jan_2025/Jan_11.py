class Solution:
    def longestUniqueSubstr(self, s):
        n = len(s)
        max_len = 0
        start = 0
        char_index = {}
        
        for end in range(n):
            if s[end] in char_index:
                # Update start to skip over the repeated character
                start = max(start, char_index[s[end]] + 1)
            
            # Update the character's last seen index
            char_index[s[end]] = end
            
            # Calculate the length of the current substring
            max_len = max(max_len, end - start + 1)
        
        return max_len
