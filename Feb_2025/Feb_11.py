class Solution:
    
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        return self.isBSTUtil(root, float('-inf'), float('inf'))
    
    def isBSTUtil(self, node, min_val, max_val):
        # Base case: If the node is None, it's a valid BST
        if node is None:
            return True
        
        # Check if the node's value violates the BST property
        if not (min_val < node.data < max_val):
            return False
        
        # Recursively check left and right subtrees with updated constraints
        return (self.isBSTUtil(node.left, min_val, node.data) and
                self.isBSTUtil(node.right, node.data, max_val))
