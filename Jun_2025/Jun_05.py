from collections import defaultdict

class Solution:
    def countPaths(self, edges, V, src, dest):
        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # Step 2: Memoization dictionary to cache results
        dp = [-1] * V  # -1 means not computed yet

        # Step 3: DFS + Memoization
        def dfs(node):
            if node == dest:
                return 1
            if dp[node] != -1:
                return dp[node]

            total = 0
            for neighbor in graph[node]:
                total += dfs(neighbor)

            dp[node] = total
            return total

        return dfs(src)
