# Number of pairs
class Solution:

    def countPairs(self,arr,brr):
        a = len(arr)
        b = len(brr)
        x = [i ** (1 / i) for i in arr]
        y = [i ** (1 / i) for i in brr]
        x.sort()
        y.sort()
        c, j = 0, 0
        for i in range(a):
            while j < b and x[i] > y[j]:
                j += 1
            c += j
        return c

  # Example usage
arr = [2, 1, 6]
brr = [1, 5]
solution = Solution()
result = solution.countPairs(arr, brr)
print(f"Number of pairs: {result}")
