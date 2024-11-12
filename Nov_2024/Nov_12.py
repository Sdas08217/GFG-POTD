# Meeting Room
class Solution:
    def canAttend(self, arr):
        # Sort meetings by their start times
        arr.sort(key=lambda x: x[0])
        
        # Check for overlaps in the sorted list
        for i in range(1, len(arr)):
            # If the current meeting starts before the previous one ends, return False
            if arr[i][0] < arr[i - 1][1]:
                return False
                
        # If no overlaps are found, return True
        return True

  # Example usage:
meetings = [
    [1, 3],  # Meeting 1 from 1 to 3
    [2, 4],  # Meeting 2 from 2 to 4
    [5, 7],  # Meeting 3 from 5 to 7
    [8, 9]   # Meeting 4 from 8 to 9
]

sol = Solution()
result = sol.canAttend(meetings)
print("Can attend all meetings:", result)
