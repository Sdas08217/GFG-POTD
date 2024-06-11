# Maximum Tip Calculator
from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        # Create a list of tuples (tipA, tipB, diff)
        orders = [(arr[i], brr[i], abs(arr[i] - brr[i])) for i in range(n)]
        
        # Sort orders based on the absolute difference in descending order
        orders.sort(key=lambda order: order[2], reverse=True)
        
        total_tip = 0
        a_count = 0
        b_count = 0
        
        for tipA, tipB, diff in orders:
            if (tipA >= tipB and a_count < x) or b_count >= y:
                total_tip += tipA
                a_count += 1
            else:
                total_tip += tipB
                b_count += 1
        
        return total_tip
# Example usage:
solution = Solution()
print(solution.maxTip(5, 3, 3, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))  # Output: 21
print(solution.maxTip(8, 4, 4, [1, 4, 3, 2, 7, 5, 9, 6], [1, 2, 3, 6, 5, 4, 9, 8]))  # Output: 43
print(solution.maxTip(7, 3, 4, [8, 7, 15, 19, 16, 16, 18], [1, 7, 15, 11, 12, 31, 9]))  # Output: 110
