# Pairs with difference k
from collections import Counter
class Solution:
    def countPairsWithDiffK(self, arr, k):
        count = 0
        freq = Counter(arr)  # Count frequencies of elements
        for num in freq:
            # Check if num + k exists
            if (num + k) in freq:
                count += freq[num] * freq[num + k]  # Count all valid pairs
        return count
      # Example usage
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 5, 3, 4, 2]
    k = 2
    result = solution.countPairsWithDiffK(arr, k)
    print("Number of pairs with difference", k, "is:", result)
