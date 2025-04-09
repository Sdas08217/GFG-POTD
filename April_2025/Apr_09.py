class Solution:
     def articulationPoints(self, V, edges):
         # Build adjacency list
         adj = [[] for _ in range(V)]
         for u, v in edges:
             adj[u].append(v)
             adj[v].append(u)
         
         disc = [-1] * V
         low = [-1] * V
         visited = [False] * V
         parent = [-1] * V
         articulation_points = set()
         time = 0
         
         for u in range(V):
             if not visited[u]:
                 stack = [(u, -1, False)]  # (node, parent, is_processed)
                 
                 while stack:
                     current_u, current_parent, is_processed = stack.pop()
                     
                     if not is_processed:
                         if visited[current_u]:
                             continue
                         # Mark as visited
                         visited[current_u] = True
                         disc[current_u] = time
                         low[current_u] = time
                         parent[current_u] = current_parent
                         time += 1
                         # Push back to stack as processed
                         stack.append((current_u, current_parent, True))
                         # Push children onto stack in reverse order to process in original order
                         for v in reversed(adj[current_u]):
                             if v == current_parent:
                                 continue
                             if not visited[v]:
                                 stack.append((v, current_u, False))
                             else:
                                 # Back edge, update low[current_u]
                                 low[current_u] = min(low[current_u], disc[v])
                     else:
                         children_count = 0
                         # Check all neighbors for children and back edges
                         for v in adj[current_u]:
                             if v == current_parent:
                                 continue
                             if parent[v] == current_u:
                                 # Child node
                                 low[current_u] = min(low[current_u], low[v])
                                 if low[v] >= disc[current_u] and current_parent != -1:
                                     articulation_points.add(current_u)
                                 children_count += 1
                         # Check if current node is root and has >=2 children
                         if current_parent == -1 and children_count >= 2:
                             articulation_points.add(current_u)
         
         if not articulation_points:
             return [-1]
         else:
             return sorted(articulation_points)
