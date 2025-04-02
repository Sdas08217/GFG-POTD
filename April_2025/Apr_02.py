from collections import deque

class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        V = len(adj)  # Number of vertices
        visited = [False] * V  # To keep track of visited nodes
        bfs_result = []  # List to store BFS traversal order
        queue = deque([0])  # Queue for BFS, starting from vertex 0
        visited[0] = True  # Mark the starting vertex as visited
        
        while queue:
            node = queue.popleft()  # Dequeue a vertex
            bfs_result.append(node)  # Add it to the BFS result
            
            # Traverse neighbors in the given order
            for neighbor in adj[node]:
                if not visited[neighbor]:  # If not visited, enqueue and mark visited
                    queue.append(neighbor)
                    visited[neighbor] = True
        
        return bfs_result

# Example Test Cases
sol = Solution()
adj1 = [[2, 3, 1], [0], [0, 4], [0], [2]]
print(sol.bfs(adj1))  # Output: [0, 2, 3, 1, 4]

adj2 = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
print(sol.bfs(adj2))  # Output: [0, 1, 2, 3, 4]
