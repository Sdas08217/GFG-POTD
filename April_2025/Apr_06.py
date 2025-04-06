from collections import defaultdict, deque

class Solution:
    
    def topoSort(self, V, edges):
        # Step 1: Create adjacency list and compute in-degrees
        adj = defaultdict(list)
        indegree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        # Step 2: Push all vertices with indegree 0 into the queue
        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
        
        # Step 3: Process the queue for topological sorting
        topo_order = []
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: If valid topological sort
        if len(topo_order) == V:
            return topo_order
        else:
            return []  # Not possible (only if graph has cycle, which shouldn't be the case)
