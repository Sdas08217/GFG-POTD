# Sub-arrays with equal number of occurences
class Solution:
    def sameOccurrence(self, arr, x, y):
        # Dictionary to store the frequency of each difference (count_x - count_y)
        diff_count = {0: 1}  # Start with difference 0 (as if there are 0 x's and y's initially)
        diff = 0  # Tracks the difference between counts of x and y
        result = 0

        # Iterate over the array
        for num in arr:
            if num == x:
                diff += 1  # Increment diff when we encounter x
            elif num == y:
                diff -= 1  # Decrement diff when we encounter y

            # If the current diff value has been seen before, it means there are subarrays
            # that end at this index with equal number of x and y
            if diff in diff_count:
                result += diff_count[diff]

            # Update the frequency of the current diff value
            diff_count[diff] = diff_count.get(diff, 0) + 1

        return result

  #Example Usage
  solution = Solution()

# Example array and the two elements x and y
arr = [1, 2, 3, 2, 1, 2, 3]
x = 2
y = 3

# Call the sameOccurrence function and print the result
result = solution.sameOccurrence(arr, x, y)
print(f"The number of subarrays with equal occurrences of {x} and {y} is: {result}")
