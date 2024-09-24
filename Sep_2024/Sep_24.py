# Smallest window in a string containing all the characters of another string

class Solution:
    
    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    def smallestWindow(self, s, p):
        from collections import Counter

        # Step 1: Frequency count of all characters in p
        p_freq = Counter(p)
        required_chars = len(p_freq)
        
        # Step 2: Initialize variables for sliding window
        start = 0
        min_len = float('inf')
        min_start = 0
        window_count = Counter()
        formed = 0
        
        # Step 3: Use two pointers to slide over string s
        for end in range(len(s)):
            char_end = s[end]
            window_count[char_end] += 1
            
            # If the character is part of p and count matches, increment formed
            if char_end in p_freq and window_count[char_end] == p_freq[char_end]:
                formed += 1
            
            # Step 4: When we have a valid window, try to minimize it
            while start <= end and formed == required_chars:
                # Check if this is the smallest window
                window_size = end - start + 1
                if window_size < min_len:
                    min_len = window_size
                    min_start = start
                
                # Shrink the window from the left
                char_start = s[start]
                window_count[char_start] -= 1
                if char_start in p_freq and window_count[char_start] < p_freq[char_start]:
                    formed -= 1
                start += 1
        
        # Step 5: Return result
        if min_len == float('inf'):
            return "-1"
        return s[min_start:min_start + min_len]

# Example usage
s = "this is a test string"
p = "tist"

sol = Solution()
result = sol.smallestWindow(s, p)
print(f"The smallest window containing all characters of '{p}' in '{s}' is: '{result}'")
