class Solution:
    def countStrings(self, s): 
        from collections import Counter

        n = len(s)
        freq = Counter(s)
        
        total_swaps = n * (n - 1) // 2
        duplicate_swaps = sum(count * (count - 1) // 2 for count in freq.values())
        
        distinct_strings = total_swaps - duplicate_swaps

        # If there's any duplicate character, we can reach the original string by swapping duplicates
        if any(count > 1 for count in freq.values()):
            return distinct_strings + 1
        else:
            return distinct_strings
