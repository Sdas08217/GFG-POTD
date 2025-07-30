from collections import defaultdict

class Solution:
    def cntSubarrays(self, arr, k):
        """
        Finds the number of subarrays whose sum exactly equals a given number k.

        Args:
            arr: The input array of integers.
            k: The target sum.

        Returns:
            The number of subarrays with sum equal to k.
        """
        count = 0
        current_sum = 0
        # A dictionary to store the frequency of prefix sums.
        # We initialize it with {0: 1} to handle cases where the subarray itself
        # starts from index 0 and its sum is k.
        freq_map = defaultdict(int)
        freq_map[0] = 1

        for num in arr:
            current_sum += num
            # If (current_sum - k) is in the freq_map, it means there's a
            # prefix sum such that the subarray from that point to the current
            # point sums to k.
            if (current_sum - k) in freq_map:
                count += freq_map[current_sum - k]
            
            # Increment the frequency of the current_sum in the map.
            freq_map[current_sum] += 1
        
        return count
