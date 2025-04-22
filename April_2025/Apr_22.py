class Solution:
    def findUnique(self, arr):
        result = 0
        for num in arr:
            result ^= num
        return result
