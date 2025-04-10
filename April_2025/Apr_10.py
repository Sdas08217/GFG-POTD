import heapq

class Solution:
    def minCost(self, houses):
        n = len(houses)
        in_mst = [False] * n
        min_cost = [float('inf')] * n
        min_cost[0] = 0  # Start from the first house
        heap = [(0, 0)]  # (cost, index)
        total_cost = 0

        while heap:
            cost, u = heapq.heappop(heap)
            if in_mst[u]:
                continue
            in_mst[u] = True
            total_cost += cost

            for v in range(n):
                if not in_mst[v]:
                    dist = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if dist < min_cost[v]:
                        min_cost[v] = dist
                        heapq.heappush(heap, (dist, v))

        return total_cost
