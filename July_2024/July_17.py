# Construct Binary Tree from Parent Array
class Solution:
    class TreeNode:
        def __init__(self, x):
            self.key = x  # Changed from val to key
            self.left = None
            self.right = None
    
    # Function to construct binary tree from parent array.
    def createTree(self, parent):
        n = len(parent)
        nodes = [self.TreeNode(i) for i in range(n)]
        
        root = None
        
        for i in range(n):
            if parent[i] == -1:
                root = nodes[i]
            else:
                p = parent[i]
                if nodes[p].left is None:
                    nodes[p].left = nodes[i]
                else:
                    nodes[p].right = nodes[i]
        
        return root

# Helper function to perform level order traversal
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        result.append(node.key)  # Changed from val to key
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Test cases
parent1 = [-1, 0, 0, 1, 1, 3, 5]
sol = Solution()
root1 = sol.createTree(parent1)
print(level_order_traversal(root1))  # Expected Output: [0, 1, 2, 3, 4, 5, 6]

parent2 = [2, 0, -1]
root2 = sol.createTree(parent2)
print(level_order_traversal(root2))  # Expected Output: [2, 0, 1]

parent3 = [-1]
root3 = sol.createTree(parent3)
print(level_order_traversal(root3))  # Expected Output: [0]

parent4 = [-1, 0, 1, 2]
root4 = sol.createTree(parent4)
print(level_order_traversal(root4))  # Expected Output: [0, 1, 2, 3]
