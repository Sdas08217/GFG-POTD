
class Solution:
    def countPairs(self, arr, target):
        # Initialize a hashmap to store frequencies
        freq = {}
        count = 0
        
        # Iterate through the array
        for num in arr:
            complement = target - num
            # Check if complement exists in hashmap
            if complement in freq:
                count += freq[complement]
            
            # Update the hashmap with the current number
            freq[num] = freq.get(num, 0) + 1
        
        return count
