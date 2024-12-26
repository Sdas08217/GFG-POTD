class Solution:
    def twoSum(self, arr, target):
        # Create a set to store elements we have seen
        seen = set()
        # Iterate through the array
        for num in arr:
            # Check if the complement (target - num) exists in the set
            complement = target - num
            if complement in seen:
                return True  # Pair found
            
            # Add the current number to the set
            seen.add(num)
        
        # If no pair is found
        return False
