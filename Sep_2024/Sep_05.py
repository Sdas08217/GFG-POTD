# Missing in Array
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        
        # Calculate the sum of the first n natural numbers
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of elements in the array
        arr_sum = sum(arr)
        
        # The missing number is the difference between the total sum and the array sum
        missing_number = total_sum - arr_sum
        
        return missing_number

# Example Usage:
sol = Solution()
n = 40
arr = [2, 32, 18, 14, 33, 37, 38, 16, 5, 27, 30, 4, 21, 29, 11, 24, 17, 6, 23, 31, 8, 39, 28, 10, 34, 20, 35, 9, 13, 7, 26, 1, 22, 40, 15, 25, 36, 3, 12]
print(sol.missingNumber(n, arr))  # Output: 19

