# Product array puzzle
class Solution:
    def productExceptSelf(self, nums):
        #code here
        n = len(nums)

        # Create empty arrays for left, right and the product
        left = [1] * n
        right = [1] * n
        product = [1] * n

        # Fill the left array
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]

        # Fill the right array
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]

        # Fill the product array by multiplying left and right arrays
        for i in range(n):
            product[i] = left[i] * right[i]

        return product

  # Example usage:
nums = [1, 2, 3, 4]
solution = Solution()
result = solution.productExceptSelf(nums)
print(result)  # Output: [24, 12, 8, 6]
