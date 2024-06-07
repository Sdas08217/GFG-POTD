# Index of an Extra Element
class Solution:
    def findExtra(self, n, a, b):
        low, high = 0, len(b) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Compare elements at the current middle index
            if a[mid] == b[mid]:
                # If they are equal, the extra element is in the right half
                low = mid + 1
            else:
                # If they are not equal, the extra element is in the left half
                high = mid - 1
        
        # The loop exits when low is at the index of the extra element
        return low
# Example usage:
n1 = 7
a1 = [2, 4, 6, 8, 9, 10, 12]
b1 = [2, 4, 6, 8, 10, 12]

n2 = 6
a2 = [3, 5, 7, 8, 11, 13]
b2 = [3, 5, 7, 11, 13]

sol = Solution()
print(sol.findExtra(n1, a1, b1))  # Output: 4
print(sol.findExtra(n2, a2, b2))  # Output: 3
  
