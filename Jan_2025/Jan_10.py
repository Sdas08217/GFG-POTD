from collections import defaultdict
class Solution:
    def countDistinct(self, arr, k):
        result = []
        freq = defaultdict(int)  # To store the frequency of elements in the current window
        distinct_count = 0
        
        # Initialize the first window
        for i in range(k):
            if freq[arr[i]] == 0:
                distinct_count += 1
            freq[arr[i]] += 1
        
        result.append(distinct_count)
        
        # Slide the window
        for i in range(k, len(arr)):
            # Remove the element going out of the window
            freq[arr[i - k]] -= 1
            if freq[arr[i - k]] == 0:
                distinct_count -= 1
            
            # Add the new element coming into the window
            if freq[arr[i]] == 0:
                distinct_count += 1
            freq[arr[i]] += 1
            
            result.append(distinct_count)
        
        return result
