# Split the Array
MOD = 10**9 + 7

class Solution:
    def countgroup(self, arr):
        n = len(arr)
        
        # Step 1: Calculate the XOR of the entire array
        xor_all = 0
        for num in arr:
            xor_all ^= num
        
        # Step 2: If XOR of all elements is not zero, return 0
        if xor_all != 0:
            return 0
        
        # Step 3: If XOR of all elements is 0, calculate 2^(n-1) % MOD
        # We subtract 1 to exclude the case where one group is empty
        return (pow(2, n-1, MOD) - 1) % MOD

  # Example usage
arr1 = [1, 2, 3]
arr2 = [5, 2, 3, 2]

solution = Solution()

# Call countgroup method for each array
result1 = solution.countgroup(arr1)
result2 = solution.countgroup(arr2)

# Output the results
print(f"Result for arr1: {result1}")  # Output: 3
print(f"Result for arr2: {result2}")  # Output: 0
