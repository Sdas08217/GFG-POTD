class Solution:
     def isCycle(self, V, edges):
         parent = list(range(V))
         rank = [1] * V
         
         def find(x):
             if parent[x] != x:
                 parent[x] = find(parent[x])
             return parent[x]
         
         def union(x, y):
             x_root = find(x)
             y_root = find(y)
             if x_root == y_root:
                 return False  # Already connected
             # Union by rank
             if rank[x_root] < rank[y_root]:
                 parent[x_root] = y_root
             else:
                 parent[y_root] = x_root
                 if rank[x_root] == rank[y_root]:
                     rank[x_root] += 1
             return True
         
         for u, v in edges:
             if find(u) == find(v):
                 return True
             union(u, v)
         
         return False
