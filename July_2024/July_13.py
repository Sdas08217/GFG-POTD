# Shortest Path in Weighted undirected graph
import heapq

from typing import List

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = [float('inf')] * (n + 1)
        dist[1] = 0
        prev = [-1] * (n + 1)
        heap = [(0, 1)]  # min-heap: (distance, node)

        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
                    heapq.heappush(heap, (alt, v))

        if dist[n] == float('inf'):
            return [-1]

        path = []
        curr = n
        while curr != -1:
            path.append(curr)
            curr = prev[curr]
        path.reverse()

        return [dist[n]] + path

  # Example usage
n = 5
m = 6
edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]

solution = Solution()
result = solution.shortestPath(n, m, edges)
print(result)  # Output: [5, 1, 4, 3, 5]
