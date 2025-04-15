class Solution:
    def bellmanFord(self, V, edges, src):
        # Step 1: Initialize distances
        dist = [float('inf')] * V
        dist[src] = 0

        # Step 2: Relax all edges V - 1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative weight cycles
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                return [-1]

        # Step 4: Replace unreachable distances with 100000000
        return [d if d != float('inf') else 100000000 for d in dist]
