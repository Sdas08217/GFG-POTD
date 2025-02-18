from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort points based on their squared Euclidean distance from the origin.
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        # Return the first k points
        return points[:k]
        
