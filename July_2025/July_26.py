import collections

class Solution:
    def findMajority(self, arr):
        n = len(arr)
        
        # There can be at most two majority elements
        # Initialize two candidates and their counts
        candidate1 = None
        count1 = 0
        candidate2 = None
        count2 = 0

        # First pass: Find potential candidates
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Second pass: Verify the counts of the potential candidates
        final_count1 = 0
        final_count2 = 0
        
        for num in arr:
            if num == candidate1:
                final_count1 += 1
            elif num == candidate2:
                final_count2 += 1
        
        result = []
        if final_count1 > n // 3:
            result.append(candidate1)
        
        # Ensure candidate1 and candidate2 are not the same number before adding candidate2
        # This handles cases where only one number is a majority or where both candidates ended up being the same.
        if candidate2 is not None and final_count2 > n // 3 and candidate1 != candidate2:
            result.append(candidate2)
            
        result.sort()
        return result
