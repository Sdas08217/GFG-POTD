class Solution:
    # Complete the below function
    def countPairs(self, arr, target):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize pointers and count
        left = 0
        right = len(arr) - 1
        count = 0
        
        # Step 3: Use two pointers to find pairs
        while left < right:
            if arr[left] + arr[right] < target:
                # If arr[left] + arr[right] < target, count all pairs from left to right
                count += (right - left)
                left += 1  # Move the left pointer to the right
            else:
                right -= 1  # Move the right pointer to the left
        
        return count

# Example usage:
sol = Solution()
print(sol.countPairs([7, 2, 5, 3], 8))  # Output: 2
print(sol.countPairs([5, 2, 3, 2, 4, 1], 5))  # Output: 4
print(sol.countPairs([2, 1, 8, 3, 4, 7, 6, 5], 7))  # Output: 6
