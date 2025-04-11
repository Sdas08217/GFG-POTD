import heapq
from collections import defaultdict

class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Undirected graph

        # Step 2: Initialize distance array and priority queue
        dist = [float('inf')] * V
        dist[src] = 0
        min_heap = [(0, src)]  # (distance, node)

        # Step 3: Dijkstra's algorithm using min-heap
        while min_heap:
            d, u = heapq.heappop(min_heap)

            for v, w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(min_heap, (dist[v], v))

        return dist
