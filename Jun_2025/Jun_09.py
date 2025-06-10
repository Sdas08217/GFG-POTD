class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def isDeadEnd(self, root):
        # Helper DFS function with valid range [min_val, max_val]
        def dfs(node, min_val, max_val):
            if not node:
                return False

            # Dead end condition
            if min_val == max_val:
                return True

            # Recurse for left and right subtrees with updated ranges
            return (dfs(node.left, min_val, node.data - 1) or
                    dfs(node.right, node.data + 1, max_val))

        return dfs(root, 1, float('inf'))
