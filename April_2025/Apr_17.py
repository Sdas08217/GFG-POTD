class Solution:
    def findMinCycle(self, V, edges):
        INF = float('inf')
        dist = [[INF] * V for _ in range(V)]
        graph = [[INF] * V for _ in range(V)]

        # Initialize graph with edge weights
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
            graph[u][v] = w
            graph[v][u] = w

        min_cycle = INF

        # Floyd-Warshall + cycle detection
        for k in range(V):
            # Check all pairs before updating distances
            for i in range(k):
                for j in range(i + 1, k):
                    if dist[i][j] != INF and graph[i][k] != INF and graph[j][k] != INF:
                        cycle_len = dist[i][j] + graph[i][k] + graph[j][k]
                        min_cycle = min(min_cycle, cycle_len)

            # Standard Floyd-Warshall update
            for i in range(V):
                for j in range(V):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return min_cycle if min_cycle != INF else -1
