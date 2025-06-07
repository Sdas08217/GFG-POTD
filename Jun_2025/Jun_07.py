class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff_map = {}
        max_len = 0
        curr_sum = 0

        for i in range(n):
            # Calculate the difference of current elements
            diff = a1[i] - a2[i]
            # Add it to the running sum
            curr_sum += diff

            # If the sum is zero, span is from 0 to i
            if curr_sum == 0:
                max_len = i + 1
            # If current sum has been seen before
            elif curr_sum in diff_map:
                max_len = max(max_len, i - diff_map[curr_sum])
            else:
                # Store the first occurrence of this sum
                diff_map[curr_sum] = i

        return max_len
