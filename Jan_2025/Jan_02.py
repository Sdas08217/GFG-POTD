class Solution:
    def countSubarrays(self, arr, k):
        # Dictionary to store the frequency of prefix sums
        prefix_sum_count = {0: 1}
        prefix_sum = 0
        count = 0
        
        # Iterate through the array
        for num in arr:
            # Update the prefix sum
            prefix_sum += num
            
            # Check if (prefix_sum - k) exists in the hashmap
            if (prefix_sum - k) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - k]
            
            # Update the hashmap with the current prefix sum
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1
        
        return count
