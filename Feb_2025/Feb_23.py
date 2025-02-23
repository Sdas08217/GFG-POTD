class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        n = len(arr)
        result = [-1] * n  # Initialize result array with -1
        stack = []  # Stack to maintain elements in decreasing order
        
        # Traverse the array from right to left
        for i in range(n-1, -1, -1):
            # Pop smaller or equal elements from the stack
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            
            # If stack is not empty, top of stack is next greater element
            if stack:
                result[i] = stack[-1]
            
            # Push current element onto stack
            stack.append(arr[i])
        
        return result

# Example Usage
arr1 = [1, 3, 2, 4]
sol = Solution()
print(sol.nextLargerElement(arr1))  # Output: [3, 4, 4, -1]

arr2 = [6, 8, 0, 1, 3]
print(sol.nextLargerElement(arr2))  # Output: [8, -1, 1, 3, -1]

arr3 = [10, 20, 30, 50]
print(sol.nextLargerElement(arr3))  # Output: [20, 30, 50, -1]

arr4 = [50, 40, 30, 10]
print(sol.nextLargerElement(arr4))  # Output: [-1, -1, -1, -1]
