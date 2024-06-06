# Maximum occured integer
class Solution:
    # Complete this function
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, n, l, r, maxx):
        # Step 1: Create a frequency array of size maxx + 2
        freq = [0] * (maxx + 2)
        
        # Step 2: Update the frequency array for each range
        for i in range(n):
            freq[l[i]] += 1
            freq[r[i] + 1] -= 1
        
        # Step 3: Compute the prefix sums to get the actual counts
        max_count = 0
        max_occuring_element = 0
        current_count = 0
        for i in range(maxx + 1):
            current_count += freq[i]
            if current_count > max_count:
                max_count = current_count
                max_occuring_element = i
        
        # Step 4: Return the result
        return max_occuring_element
  # Example usage
sol = Solution()

n1 = 4
l1 = [1, 4, 3, 1]
r1 = [15, 8, 5, 4]
maxx1 = 15
print(sol.maxOccured(n1, l1, r1, maxx1))  # Output: 4

n2 = 5
l2 = [1, 5, 9, 13, 21]
r2 = [15, 8, 12, 20, 30]
maxx2 = 30
print(sol.maxOccured(n2, l2, r2, maxx2))  # Output: 5
