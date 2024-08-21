# Shortest path in Undirected Graph
from collections import deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # Step 1: Create an adjacency list for the graph
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Initialize distance array with -1
        dist = [-1] * n
        dist[src] = 0
        
        # Step 3: BFS initialization
        queue = deque([src])
        
        # Step 4: BFS traversal
        while queue:
            node = queue.popleft()
            current_dist = dist[node]
            
            for neighbor in graph[node]:
                if dist[neighbor] == -1:  # Unvisited node
                    dist[neighbor] = current_dist + 1
                    queue.append(neighbor)
        
        return dist

# Example Usage
# Create an instance of the Solution class
solution = Solution()

# Example 1
edges = [[0,1],[0,3],[3,4],[4,5],[5,6],[1,2],[2,6],[6,7],[7,8],[6,8]]
n = 9
m = 10
src = 0
print(solution.shortestPath(edges, n, m, src))  # Output: [0, 1, 2, 1, 2, 3, 3, 4, 4]

# Example 2
edges = [[1,3],[3,0]]
n = 4
m = 2
src = 3
print(solution.shortestPath(edges, n, m, src))  # Output: [1, 1, -1, 0]
  
