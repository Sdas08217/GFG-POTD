# Maximum product subset of an array
class Solution:
    def findMaxProduct(self, arr):
        MOD = 10**9 + 7
        
        if len(arr) == 1:
            return arr[0]
        
        max_negative = float('-inf')
        count_negative = 0
        count_zero = 0
        product = 1
        has_positive = False
        
        for num in arr:
            if num == 0:
                count_zero += 1
                continue
            if num < 0:
                count_negative += 1
                max_negative = max(max_negative, num)
            else:
                has_positive = True
            
            product = (product * num) % MOD
        
        if count_zero == len(arr):
            return 0
        
        if count_negative % 2 != 0:
            if count_negative == 1 and count_zero + count_negative == len(arr):
                return 0
            product = (product * pow(max_negative, MOD-2, MOD)) % MOD
        
        return product

# Example usage:
sol = Solution()
print(sol.findMaxProduct([-1, -1, -2, 4, 3]))  # Output: 24
print(sol.findMaxProduct([-1, 0]))  # Output: 0
print(sol.findMaxProduct([5]))  # Output: 5
print(sol.findMaxProduct([-1]))  # Output: -1
