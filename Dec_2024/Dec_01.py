# Non Repeating Character
class Solution:
    
    # Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self, s: str) -> str:
        # Step 1: Count occurrences of each character
        char_count = {}
        
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Step 2: Find the first non-repeating character
        for char in s:
            if char_count[char] == 1:
                return char
        
        # Step 3: If no non-repeating character, return '$'
        return '$'
