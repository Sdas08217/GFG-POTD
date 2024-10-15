# Subarray range with given sum
class Solution:
    
    #Complete this function
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self, arr, tar):
        cum_sum_freq = {0: 1}  # Initialize with sum 0 to handle edge cases
        cum_sum = 0  # Cumulative sum of the elements
        count = 0  # Number of subarrays found with sum equal to target

        for num in arr:
            cum_sum += num  # Update the cumulative sum

            # Check if (cum_sum - tar) exists in the hash map
            if cum_sum - tar in cum_sum_freq:
                count += cum_sum_freq[cum_sum - tar]

            # Update the frequency of the current cumulative sum in the hash map
            cum_sum_freq[cum_sum] = cum_sum_freq.get(cum_sum, 0) + 1

        return count

  # Example usage of the subArraySum function
arr = [10, 2, -2, -20, 10]
target_sum = -10

sol = Solution()
result = sol.subArraySum(arr, target_sum)
print("Number of subarrays with sum equal to", target_sum, ":", result)
