# Minimum Cost of ropes
from typing import List
import heapq

class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr: List[int]) -> int:
        # Create a min-heap from the array
        heapq.heapify(arr)
        
        total_cost = 0
        
        # Continue until we have one rope left
        while len(arr) > 1:
            # Pop two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Calculate the cost of connecting them
            cost = first + second
            total_cost += cost
            
            # Push the new rope back into the heap
            heapq.heappush(arr, cost)
        
        return total_cost

  # Example Usage
  arr1 = [4, 3, 2, 6]
arr2 = [4, 2, 7, 6, 9]

sol = Solution()
print(sol.minCost(arr1))  # Output: 29
print(sol.minCost(arr2))  # Output: 62
