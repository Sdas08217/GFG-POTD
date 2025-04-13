class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution():
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(curr):
            if curr in visited:
                return visited[curr]

            # Clone the current node
            copy = Node(curr.val)
            visited[curr] = copy

            # Clone all neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
