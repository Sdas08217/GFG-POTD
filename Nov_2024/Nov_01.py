# Swap and Maximize
class Solution:
    def maxSum(self, arr):
        # Sort the array to easily pick smallest and largest elements
        arr.sort()
        n = len(arr)
        
        # Arrange elements by alternating smallest and largest
        arranged = []
        for i in range(n // 2):
            arranged.append(arr[i])           # Pick from the start (smallest)
            arranged.append(arr[n - i - 1])   # Pick from the end (largest)
        
        if n % 2 != 0:  # If there is a middle element in an odd-length array, add it
            arranged.append(arr[n // 2])
        
        # Calculate the maximum sum of absolute differences
        max_sum = 0
        for i in range(1, n):
            max_sum += abs(arranged[i] - arranged[i - 1])
        
        # Add the circular difference (last element to the first)
        max_sum += abs(arranged[-1] - arranged[0])
        
        return max_sum

  # Example usage
arr = [1, 2, 4, 8]  # Sample input array
solution = Solution()
result = solution.maxSum(arr)
print("Maximum Sum of Absolute Differences:", result)
