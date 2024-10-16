# Two Swaps
class Solution:
    def checkSorted(self, a):
        hash1 = {}
        for i in range(1, len(a)+1):
            hash1[a[i-1]] = i
        
        swap = 0
        for i in range(1, len(a)+1):
            if swap == 2 and i == len(a):
                return True
            if swap > 2:
                return False
            if a[i-1] != i:
                a[i-1], a[hash1[i]-1] = a[hash1[i]-1], a[i-1]
                swap += 1
        return not swap

  #Example Usage
  # Create an instance of the Solution class
solution = Solution()

# Test cases
test_cases = [
    [4, 3, 2, 1],  # Should return True
    [4, 3, 1, 2],  # Should return False
    [3, 1, 2, 4],  # Should return True
    [1, 2, 3, 4],  # Should return True (already sorted)
    [2, 3, 1, 4],  # Should return True (swap 2 with 1 and then 2 with 3)
    [1, 3, 2, 4],  # Should return True (swap 2 with 3 and then back)
]

# Execute the test cases
for arr in test_cases:
    result = solution.checkSorted(arr)
    print(f"Input: {arr}, Output: {result}")
