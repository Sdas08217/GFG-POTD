# Maximize Array Value After Rearrangement
class Solution:
    def Maximize(self, arr): 
        mod = 10**9 + 7
        n = len(arr)
        arr.sort()  # Sort the array
        
        max_sum = 0
        for i in range(n):
            max_sum = (max_sum + arr[i] * i) % mod  # Multiply and sum, taking modulo
        
        return max_sum

  # Example usage:
arr1 = [5, 3, 2, 4, 1]
arr2 = [1, 2, 3]

sol = Solution()
print(sol.maxSum(arr1))  # Output: 40
print(sol.maxSum(arr2))  # Output: 8
