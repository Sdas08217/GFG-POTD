from collections import defaultdict

class Solution:
    def isBridge(self, V, edges, c, d):
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        time = [0]  # Clock for discovery time
        visited = [False] * V
        disc = [float('inf')] * V
        low = [float('inf')] * V
        found_bridge = [False]

        def dfs(u, parent):
            visited[u] = True
            disc[u] = low[u] = time[0]
            time[0] += 1

            for v in graph[u]:
                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # Check if the edge u-v is a bridge
                    if low[v] > disc[u]:
                        if (u == c and v == d) or (u == d and v == c):
                            found_bridge[0] = True
                elif v != parent:
                    low[u] = min(low[u], disc[v])

        # Handle disconnected graphs by running DFS on all components
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        return 1 if found_bridge[0] else 0  # Return 1 if it's a bridge, else 0
