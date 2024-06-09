# Convert array into Zig-Zag fashion
from typing import List

class Solution:
    def zigZag(self, n: int, arr: List[int]) -> None:
        flag = True  # Initialize the flag to True for the "<" relation
        
        for i in range(n - 1):
            if flag:  # "<" relation expected
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            else:  # ">" relation expected
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
            # Toggle the flag for next comparison
            flag = not flag

      # Example usage:
arr1 = [4, 3, 7, 8, 6, 2, 1]
n1 = len(arr1)
solution = Solution()
solution.zigZag(n1, arr1)
print(arr1)  # Output: [3, 7, 4, 8, 2, 6, 1]

arr2 = [1, 4, 3, 2]
n2 = len(arr2)
solution.zigZag(n2, arr2)
print(arr2)  # Output: [1, 4, 2, 3]
