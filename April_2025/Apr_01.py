class Solution:
     def dfs(self, adj):
         visited = set()
         stack = [0]
         result = []
         while stack:
             node = stack.pop()
             if node not in visited:
                 visited.add(node)
                 result.append(node)
                 # Push neighbors in reverse order to process leftmost first
                 for neighbor in reversed(adj[node]):
                     stack.append(neighbor)
         return result
