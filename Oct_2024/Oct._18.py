# Single Number
from collections import Counter
class Solution:
    def getSingle(self,arr):
        frequencies = Counter(arr)
        for num, freq in frequencies.items():
            if freq % 2 != 0:
                return num


      # Example usage
arr = [2, 3, 5, 4, 5, 3, 4, 2, 4]
sol = Solution()
result = sol.getSingle(arr)
print("The number that appears an odd number of times is:", result)
