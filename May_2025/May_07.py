from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def Paths(self, root: Optional[Node]) -> List[List[int]]:
        def dfs(node, path, paths):
            if not node:
                return
            path.append(node.data)
            # If it's a leaf node, add the current path to paths
            if not node.left and not node.right:
                paths.append(list(path))
            else:
                # Recurse on left and right children
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)
            # Backtrack
            path.pop()

        result = []
        dfs(root, [], result)
        return result
