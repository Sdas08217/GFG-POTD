class Solution:
    # Function to find the equilibrium point in the array.
    def findEquilibrium(self, arr):
        # Calculate the total sum of the array
        total_sum = sum(arr)
        left_sum = 0  # Initialize the left sum as 0
        
        # Traverse the array
        for i, num in enumerate(arr):
            # Calculate the right sum by subtracting the current element from the total sum
            total_sum -= num
            
            # Check if the left sum equals the right sum
            if left_sum == total_sum:
                return i  # Return the equilibrium index (0-based index)
            
            # Update the left sum
            left_sum += num
        
        return -1  # Return -1 if no equilibrium index is found
