# Path With Minimum Effort

from typing import List
import heapq
class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        pq = []
        n = len(heights)
        m = len(heights[0])
        dist = [[1e9]*m for _ in range(n)]
        dist[0][0] = 0
        heapq.heappush(pq, (0, 0, 0))
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        while pq:
            diff, row, col = heapq.heappop(pq)
            if row == n-1 and col == m-1:
                return diff

            for i in range(4):
                newr = row + dr[i]
                newc = col + dc[i]

                if 0 <= newr < n and 0 <= newc < m:
                    neweffort = max(abs(heights[row][col]-heights[newr][newc]), diff)
                    if neweffort < dist[newr][newc]:
                        dist[newr][newc] = neweffort
                        heapq.heappush(pq, (dist[newr][newc], newr, newc))

        return 0

  # Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    solution = Solution()

    # Define the heights grid
    heights = [
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5]
    ]

    # Get the number of rows and columns
    rows = len(heights)
    columns = len(heights[0])

    # Find the minimum effort
    result = solution.MinimumEffort(rows, columns, heights)

    # Print the result
    print("Minimum effort required:", result)
