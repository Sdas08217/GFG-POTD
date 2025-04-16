class Solution:
    def floydWarshall(self, dist):
        n = len(dist)
        INF = 10**9  # better constant for "infinity"

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Make sure we only compute if both paths exist
                    if dist[i][k] < INF and dist[k][j] < INF:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
