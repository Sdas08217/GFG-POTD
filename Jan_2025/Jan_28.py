from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Generate all unique permutations using a set to avoid duplicates
        perm_set = set(permutations(s))
        # Convert each tuple back to a string and return as a sorted list (optional)
        return sorted(["".join(p) for p in perm_set])

# Example usage
solution = Solution()

# Test cases
print(solution.findPermutation("ABC"))  # ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
print(solution.findPermutation("ABSG"))  # ["ABGS", "ABSG", ..., "SGBA"]
print(solution.findPermutation("AAA"))   # ["AAA"]
